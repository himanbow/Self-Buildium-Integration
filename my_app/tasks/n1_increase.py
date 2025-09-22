"""Automation workflow for Buildium N1 rent increase tasks."""

from __future__ import annotations

import base64
import json
import logging
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from io import BytesIO
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional, Protocol, Sequence
from urllib import request as urllib_request
from zipfile import ZIP_DEFLATED, ZipFile

from ..services.account_context import BUILDUM_FIRESTORE_DATABASE

logger = logging.getLogger(__name__)

FIRESTORE_COLLECTION_PATH = "buildium_accounts"
MAX_PAYLOAD_BYTES = 20 * 1024 * 1024


class BuildiumN1API(Protocol):
    """Interface of Buildium APIs exercised by the N1 automation."""

    def list_eligible_leases(self) -> Sequence[Mapping[str, Any]]:
        ...

    def get_market_rent(self, *, property_id: str, unit_id: str) -> Optional[Mapping[str, Any]]:
        ...

    def get_ontario_increase_rates(self) -> Mapping[str, Any]:
        ...

    def upload_document(
        self,
        *,
        lease_id: str,
        property_id: str,
        filename: str,
        content: bytes,
        content_type: str,
    ) -> Mapping[str, Any]:
        ...

    def update_lease(self, *, lease_id: str, payload: Mapping[str, Any]) -> Mapping[str, Any]:
        ...

    def extend_lease(
        self,
        *,
        lease_id: str,
        end_date: Optional[str],
    ) -> Mapping[str, Any]:
        ...

    def create_task(
        self,
        *,
        category_id: Optional[str],
        name: str,
        description: str,
    ) -> Mapping[str, Any]:
        ...


@dataclass
class RequestsBuildiumAPI:
    """Implementation of :class:`BuildiumN1API` backed by HTTP requests."""

    api_headers: Mapping[str, str]
    base_url: str = "https://api.buildium.com/v1"

    def __post_init__(self) -> None:
        self._base_url = self.base_url.rstrip("/")
        self._headers = dict(self.api_headers)

    def _get(self, path: str, *, params: Optional[Mapping[str, Any]] = None) -> Any:
        url = f"{self._base_url}/{path.lstrip('/')}"
        if params:
            query = "&".join(f"{key}={value}" for key, value in params.items())
            url = f"{url}?{query}"
        request = urllib_request.Request(url, headers=self._headers, method="GET")
        with urllib_request.urlopen(request) as response:  # pragma: no cover - network
            raw = response.read()
        if not raw:
            return {}
        payload = json.loads(raw.decode("utf-8"))
        if isinstance(payload, Mapping) and "items" in payload:
            items = payload.get("items")
            if isinstance(items, Iterable):
                return list(items)
        return payload

    def _post(self, path: str, payload: Mapping[str, Any]) -> Mapping[str, Any]:
        request = urllib_request.Request(
            f"{self._base_url}/{path.lstrip('/')}",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                **self._headers,
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            method="POST",
        )
        with urllib_request.urlopen(request) as response:  # pragma: no cover - network
            raw = response.read()
        if not raw:
            return {}
        data = json.loads(raw.decode("utf-8"))
        return data if isinstance(data, Mapping) else {"response": data}

    def list_eligible_leases(self) -> Sequence[Mapping[str, Any]]:
        leases = self._get("leases", params={"status": "Active"})
        if isinstance(leases, Sequence):
            return list(leases)
        if isinstance(leases, Mapping):
            return list(leases.values())
        return []

    def get_market_rent(self, *, property_id: str, unit_id: str) -> Optional[Mapping[str, Any]]:
        response = self._get(
            "reports/marketrent",
            params={"propertyId": property_id, "unitId": unit_id},
        )
        if isinstance(response, Sequence):
            return dict(response[0]) if response else None
        if isinstance(response, Mapping):
            return dict(response)
        return None

    def get_ontario_increase_rates(self) -> Mapping[str, Any]:
        response = self._get("rentcontrols/ontario")
        return response if isinstance(response, Mapping) else {}

    def upload_document(
        self,
        *,
        lease_id: str,
        property_id: str,
        filename: str,
        content: bytes,
        content_type: str,
    ) -> Mapping[str, Any]:
        payload = {
            "leaseId": lease_id,
            "propertyId": property_id,
            "fileName": filename,
            "contentType": content_type,
            "content": base64.b64encode(content).decode("ascii"),
        }
        return self._post("documents/upload", payload)

    def update_lease(self, *, lease_id: str, payload: Mapping[str, Any]) -> Mapping[str, Any]:
        return self._post(f"leases/{lease_id}/rent", payload)

    def extend_lease(
        self,
        *,
        lease_id: str,
        end_date: Optional[str],
    ) -> Mapping[str, Any]:
        payload: Dict[str, Any] = {"leaseId": lease_id}
        if end_date:
            payload["endDate"] = end_date
        return self._post(f"leases/{lease_id}/extend", payload)

    def create_task(
        self,
        *,
        category_id: Optional[str],
        name: str,
        description: str,
    ) -> Mapping[str, Any]:
        payload: Dict[str, Any] = {"name": name, "description": description}
        if category_id:
            payload["taskCategoryId"] = category_id
        return self._post("tasks", payload)


def _timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def _normalize(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    normalized = "".join(ch for ch in str(value).lower() if ch.isalnum())
    return normalized or None


def _decimal(value: Any, *, default: Decimal = Decimal("0")) -> Decimal:
    try:
        if isinstance(value, Decimal):
            return value
        if value is None:
            return default
        return Decimal(str(value))
    except (InvalidOperation, ValueError):
        return default


def _legal_round(amount: Decimal) -> Decimal:
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def _extract_event_type(webhook: Mapping[str, Any]) -> Optional[str]:
    for key in ("eventType", "type", "event_type"):
        if key in webhook:
            value = webhook[key]
            if isinstance(value, str):
                return value
    event_block = webhook.get("event")
    if isinstance(event_block, Mapping):
        return _extract_event_type(event_block)
    return None


def _extract_task_block(webhook: Mapping[str, Any]) -> Optional[Mapping[str, Any]]:
    for key in ("task", "Task", "resource", "Resource"):
        value = webhook.get(key)
        if isinstance(value, Mapping):
            return value
    return None


def _extract_task_status(task_data: Mapping[str, Any], webhook: Mapping[str, Any]) -> Optional[str]:
    for key in ("status", "taskStatus", "state"):
        value = task_data.get(key)
        if isinstance(value, str):
            return value
    changes = webhook.get("changes")
    if isinstance(changes, Mapping):
        status_block = changes.get("status") or changes.get("taskStatus")
        if isinstance(status_block, Mapping):
            for nested_key in ("newValue", "new", "value"):
                value = status_block.get(nested_key)
                if isinstance(value, str):
                    return value
    return None


def _extract_identifier(data: Mapping[str, Any], *keys: str) -> Optional[str]:
    for key in keys:
        if key in data:
            value = data[key]
            if value is None:
                continue
            if isinstance(value, Mapping):
                candidate = value.get("id") or value.get("ID")
                if candidate is not None:
                    return str(candidate)
            return str(value)
    return None


def _extract_rent_amount(lease: Mapping[str, Any]) -> Decimal:
    rent_block = lease.get("rent") or lease.get("currentRent") or {}
    if isinstance(rent_block, Mapping):
        for key in ("amount", "monthlyAmount", "rent", "value"):
            if key in rent_block:
                return _decimal(rent_block[key])
    for key in ("rent", "currentRent", "monthlyRent"):
        if key in lease:
            return _decimal(lease[key])
    return Decimal("0")


def _determine_effective_date(lease: Mapping[str, Any]) -> Optional[str]:
    for key in (
        "increaseEffectiveDate",
        "effectiveDate",
        "nextIncreaseDate",
        "renewalDate",
        "startDate",
        "leaseStartDate",
    ):
        value = lease.get(key)
        if isinstance(value, str) and value:
            return value
    term = lease.get("term")
    if isinstance(term, Mapping):
        for key in ("startDate", "effectiveDate"):
            value = term.get(key)
            if isinstance(value, str) and value:
                return value
    return None


def _detect_extended_lease(lease: Mapping[str, Any]) -> bool:
    if isinstance(lease.get("extension"), Mapping):
        extension = lease["extension"]
        if bool(extension.get("isExtended") or extension.get("extended")):
            return True
        original = extension.get("originalEndDate")
        end = extension.get("endDate")
        if original and end and original != end:
            return True
    if lease.get("isExtended") or lease.get("extended"):
        return True
    original_end = lease.get("originalEndDate") or lease.get("initialEndDate")
    end_date = lease.get("endDate")
    if original_end and end_date and original_end != end_date:
        return True
    return False


def _determine_extension_end_date(lease: Mapping[str, Any]) -> Optional[str]:
    if isinstance(lease.get("extension"), Mapping):
        value = lease["extension"].get("endDate")
        if isinstance(value, str) and value:
            return value
    for key in ("extensionEndDate", "extendedEndDate", "endDate"):
        value = lease.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def _determine_increase_rate(property_id: str, rates: Mapping[str, Any]) -> Decimal:
    if not isinstance(rates, Mapping):
        return Decimal("0")
    per_property = rates.get("per_property") or rates.get("perProperty") or {}
    if isinstance(per_property, Mapping):
        if property_id in per_property:
            return _decimal(per_property[property_id])
        lower = property_id.lower()
        for key, value in per_property.items():
            if isinstance(key, str) and key.lower() == lower:
                return _decimal(value)
    direct = rates.get(property_id)
    if direct is not None:
        return _decimal(direct)
    default_rate = (
        rates.get("default")
        or rates.get("allowableIncrease")
        or rates.get("rate")
        or rates.get("ontario")
    )
    return _decimal(default_rate)


def _to_serializable_decimal(value: Decimal) -> str:
    return format(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), "f")


def _render_excel_summary(schedules: Sequence[Mapping[str, Any]]) -> bytes:
    headers = [
        "Property",
        "Unit",
        "Lease",
        "Current Rent",
        "New Rent",
        "Increase",
        "Effective Date",
        "Extended",
    ]

    def _cell(column: str, row: int, value: str, *, numeric: bool = False) -> str:
        if numeric:
            return f'<c r="{column}{row}"><v>{value}</v></c>'
        return (
            f'<c r="{column}{row}" t="inlineStr"><is><t>{value}</t></is></c>'
        )

    column_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    rows = [
        "<row r=\"1\">"
        + "".join(
            _cell(column_letters[idx], 1, header.replace("&", "&amp;"))
            for idx, header in enumerate(headers)
        )
        + "</row>"
    ]

    for row_index, schedule in enumerate(schedules, start=2):
        values = [
            str(schedule.get("property_name", "")),
            str(schedule.get("unit_name", "")),
            str(schedule.get("lease_id", "")),
            _to_serializable_decimal(_decimal(schedule.get("current_rent"))),
            _to_serializable_decimal(_decimal(schedule.get("new_rent"))),
            str(schedule.get("increase_rate_percent", "")),
            str(schedule.get("effective_date", "")),
            "Yes" if schedule.get("is_extended") else "No",
        ]
        row_cells = []
        for idx, value in enumerate(values):
            column = column_letters[idx]
            if idx in (3, 4):
                row_cells.append(_cell(column, row_index, value, numeric=True))
            else:
                row_cells.append(_cell(column, row_index, value.replace("&", "&amp;")))
        rows.append(f"<row r=\"{row_index}\">{''.join(row_cells)}</row>")

    sheet_data = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        "<worksheet xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\">"
        "<sheetData>"
        + "".join(rows)
        + "</sheetData></worksheet>"
    )

    workbook_xml = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        "<workbook xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\" xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\">"
        "<sheets><sheet name=\"N1 Rent Increases\" sheetId=\"1\" r:id=\"rId1\"/></sheets>"
        "</workbook>"
    )

    root_rels = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">"
        "<Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument\" Target=\"xl/workbook.xml\"/>"
        "</Relationships>"
    )

    workbook_rels = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">"
        "<Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet\" Target=\"worksheets/sheet1.xml\"/>"
        "<Relationship Id=\"rId2\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles\" Target=\"styles.xml\"/>"
        "</Relationships>"
    )

    content_types = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        "<Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\">"
        "<Default Extension=\"rels\" ContentType=\"application/vnd.openxmlformats-package.relationships+xml\"/>"
        "<Default Extension=\"xml\" ContentType=\"application/xml\"/>"
        "<Override PartName=\"/xl/workbook.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml\"/>"
        "<Override PartName=\"/xl/worksheets/sheet1.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml\"/>"
        "<Override PartName=\"/xl/styles.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml\"/>"
        "</Types>"
    )

    styles_xml = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        "<styleSheet xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\"></styleSheet>"
    )

    output = BytesIO()
    with ZipFile(output, "w", ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", root_rels)
        zf.writestr("xl/workbook.xml", workbook_xml)
        zf.writestr("xl/_rels/workbook.xml.rels", workbook_rels)
        zf.writestr("xl/worksheets/sheet1.xml", sheet_data)
        zf.writestr("xl/styles.xml", styles_xml)
    return output.getvalue()


def _escape_pdf_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _render_pdf_summary(schedules: Sequence[Mapping[str, Any]]) -> bytes:
    summary_lines = [
        "N1 Rent Increase Summary",
        "--------------------------",
    ]
    for schedule in schedules:
        summary_lines.append(
            f"Property: {schedule.get('property_name', '')} | Unit: {schedule.get('unit_name', '')} | Lease: {schedule.get('lease_id', '')}"
        )
        summary_lines.append(
            f"Current: ${schedule.get('current_rent')} -> New: ${schedule.get('new_rent')} ({schedule.get('increase_rate_percent', '')})"
        )
        summary_lines.append("")

    text = _escape_pdf_text("\n".join(summary_lines))
    stream = f"BT /F1 11 Tf 72 720 Td ({text}) Tj ET".encode("utf-8")

    objects: List[bytes] = []
    objects.append(b"1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n")
    objects.append(b"2 0 obj<</Type/Pages/Count 1/Kids[3 0 R]>>endobj\n")
    objects.append(
        b"3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]/Contents 4 0 R/Resources<</Font<</F1 5 0 R>>>>>>endobj\n"
    )
    objects.append(
        b"4 0 obj<</Length "
        + str(len(stream)).encode("ascii")
        + b">>stream\n"
        + stream
        + b"\nendstream\nendobj\n"
    )
    objects.append(b"5 0 obj<</Type/Font/Subtype/Type1/BaseFont/Helvetica>>endobj\n")

    output = BytesIO()
    output.write(b"%PDF-1.4\n")
    offsets = [0]
    current = output.tell()
    for obj in objects:
        offsets.append(current)
        output.write(obj)
        current += len(obj)

    xref_position = current
    output.write(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    output.write(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.write(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.write(
        (
            "trailer<</Size {size}/Root 1 0 R>>\nstartxref\n{xref}\n%%EOF".format(
                size=len(objects) + 1, xref=xref_position
            )
        ).encode("ascii")
    )
    return output.getvalue()


def _render_notice(schedule: Mapping[str, Any]) -> bytes:
    lines = [
        "Ontario N1 Rent Increase Notice",
        "Property: {property_name}",
        "Unit: {unit_name}",
        "Lease ID: {lease_id}",
        "New Monthly Rent: ${new_rent}",
        "Effective Date: {effective_date}",
    ]
    text = _escape_pdf_text("\n".join(line.format(**schedule) for line in lines))
    stream = f"BT /F1 12 Tf 72 720 Td ({text}) Tj ET".encode("utf-8")

    objects: List[bytes] = []
    objects.append(b"1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n")
    objects.append(b"2 0 obj<</Type/Pages/Count 1/Kids[3 0 R]>>endobj\n")
    objects.append(
        b"3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]/Contents 4 0 R/Resources<</Font<</F1 5 0 R>>>>>>endobj\n"
    )
    objects.append(
        b"4 0 obj<</Length "
        + str(len(stream)).encode("ascii")
        + b">>stream\n"
        + stream
        + b"\nendstream\nendobj\n"
    )
    objects.append(b"5 0 obj<</Type/Font/Subtype/Type1/BaseFont/Helvetica>>endobj\n")

    output = BytesIO()
    output.write(b"%PDF-1.4\n")
    offsets = [0]
    current = output.tell()
    for obj in objects:
        offsets.append(current)
        output.write(obj)
        current += len(obj)

    xref_position = current
    output.write(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    output.write(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.write(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.write(
        (
            "trailer<</Size {size}/Root 1 0 R>>\nstartxref\n{xref}\n%%EOF".format(
                size=len(objects) + 1, xref=xref_position
            )
        ).encode("ascii")
    )
    return output.getvalue()


def _chunk_payload(payload: Sequence[Mapping[str, Any]], *, max_bytes: int = MAX_PAYLOAD_BYTES) -> List[Mapping[str, Any]]:
    chunks: List[Mapping[str, Any]] = []
    current: List[Mapping[str, Any]] = []
    for item in payload:
        test_chunk = current + [item]
        encoded = json.dumps(test_chunk, separators=(",", ":")).encode("utf-8")
        if encoded and len(encoded) > max_bytes:
            if not current:
                # Item itself exceeds max size; force single-item chunk
                encoded = json.dumps([item], separators=(",", ":")).encode("utf-8")
                chunks.append(
                    {
                        "index": len(chunks),
                        "payload": base64.b64encode(encoded).decode("ascii"),
                        "count": 1,
                    }
                )
                current = []
                continue
            chunks.append(
                {
                    "index": len(chunks),
                    "payload": base64.b64encode(
                        json.dumps(current, separators=(",", ":")).encode("utf-8")
                    ).decode("ascii"),
                    "count": len(current),
                }
            )
            current = [item]
        else:
            current.append(item)
    if current:
        chunks.append(
            {
                "index": len(chunks),
                "payload": base64.b64encode(
                    json.dumps(current, separators=(",", ":")).encode("utf-8")
                ).decode("ascii"),
                "count": len(current),
            }
        )
    return chunks


def _combine_payload_chunks(chunks: Sequence[Mapping[str, Any]]) -> List[Mapping[str, Any]]:
    combined: List[Mapping[str, Any]] = []
    for chunk in chunks:
        payload = chunk.get("payload")
        if not isinstance(payload, str):
            continue
        try:
            decoded = base64.b64decode(payload.encode("ascii"))
            combined.extend(json.loads(decoded.decode("utf-8")))
        except Exception:
            logger.exception("Failed to decode payload chunk; skipping")
    return combined


def _prepare_schedule(
    lease: Mapping[str, Any],
    *,
    rates: Mapping[str, Any],
    api: BuildiumN1API,
) -> Mapping[str, Any]:
    lease_id = _extract_identifier(lease, "leaseId", "id", "lease") or ""
    property_block = lease.get("property") if isinstance(lease.get("property"), Mapping) else {}
    property_id = _extract_identifier(lease, "propertyId") or _extract_identifier(property_block or {}, "id") or ""
    unit_block = lease.get("unit") if isinstance(lease.get("unit"), Mapping) else {}
    unit_id = _extract_identifier(lease, "unitId") or _extract_identifier(unit_block or {}, "id") or ""
    property_name = ""
    if isinstance(property_block, Mapping):
        property_name = str(property_block.get("name") or property_block.get("displayName") or "")
    if not property_name:
        property_name = str(lease.get("propertyName") or "")
    unit_name = ""
    if isinstance(unit_block, Mapping):
        unit_name = str(unit_block.get("name") or unit_block.get("number") or "")
    if not unit_name:
        unit_name = str(lease.get("unitName") or "")

    current_rent = _extract_rent_amount(lease)
    rate = _determine_increase_rate(str(property_id), rates)
    increase_amount = _legal_round(current_rent * rate)
    new_rent = _legal_round(current_rent + increase_amount)
    market_rent_info = api.get_market_rent(property_id=str(property_id), unit_id=str(unit_id)) or {}
    market_rent = _decimal(market_rent_info.get("marketRent") or market_rent_info.get("amount"))

    schedule = {
        "lease_id": str(lease_id),
        "property_id": str(property_id),
        "unit_id": str(unit_id),
        "property_name": property_name,
        "unit_name": unit_name,
        "current_rent": _to_serializable_decimal(current_rent),
        "new_rent": _to_serializable_decimal(new_rent),
        "increase_rate": str(rate),
        "increase_rate_percent": f"{(rate * Decimal('100')).quantize(Decimal('0.01'))}%",
        "increase_amount": _to_serializable_decimal(increase_amount),
        "market_rent": _to_serializable_decimal(market_rent),
        "effective_date": _determine_effective_date(lease),
        "is_extended": _detect_extended_lease(lease),
        "extension_end_date": _determine_extension_end_date(lease),
    }
    return schedule


def _build_serving_description(property_name: str, schedules: Sequence[Mapping[str, Any]]) -> str:
    lines = [
        f"Serve N1 notices for {property_name}.",
        "",
        "Notices to deliver:",
    ]
    for schedule in schedules:
        lines.append(
            f"- Unit {schedule.get('unit_name', '')}: increase to ${schedule.get('new_rent')} effective {schedule.get('effective_date', '')}"
        )
    lines.append("")
    lines.append("Update this task once all residents have been served.")
    return "\n".join(lines)


def _persist_schedules(
    *,
    document: Any,
    existing: Mapping[str, Any],
    schedules: Sequence[Mapping[str, Any]],
    payload_chunks: Sequence[Mapping[str, Any]],
    excel_bytes: bytes,
    pdf_bytes: bytes,
) -> None:
    merged: MutableMapping[str, Any] = dict(existing)
    n1_block: MutableMapping[str, Any] = dict(merged.get("n1_increase") or {})
    n1_block.update(
        {
            "generated_at": _timestamp(),
            "lease_count": len(schedules),
            "schedules": list(schedules),
            "payload_chunks": list(payload_chunks),
            "summary_files": {
                "excel": base64.b64encode(excel_bytes).decode("ascii"),
                "pdf": base64.b64encode(pdf_bytes).decode("ascii"),
            },
        }
    )
    merged["n1_increase"] = n1_block
    document.set(dict(merged), merge=True)


def _load_document(document: Any) -> Mapping[str, Any]:
    try:
        snapshot = document.get()
    except Exception:
        logger.exception("Failed to load N1 Firestore document snapshot.")
        return {}
    if not getattr(snapshot, "exists", False):
        return {}
    try:
        return snapshot.to_dict() or {}
    except Exception:
        logger.exception("Unable to deserialize N1 Firestore document snapshot.")
        return {}


def _ensure_firestore_document(firestore_client: Any, account_id: str) -> Any:
    collection = firestore_client.collection(FIRESTORE_COLLECTION_PATH)
    return collection.document(account_id)


def _handle_task_created(
    *,
    account_id: str,
    api_headers: Mapping[str, str],
    gl_mapping: Mapping[str, Any],
    firestore_client: Any,
    buildium_api: Optional[BuildiumN1API],
) -> None:
    api = buildium_api or RequestsBuildiumAPI(api_headers=api_headers)

    leases = list(api.list_eligible_leases())
    rates = api.get_ontario_increase_rates() or {}
    schedules = [
        _prepare_schedule(lease, rates=rates, api=api)
        for lease in leases
    ]

    payload_chunks = _chunk_payload(schedules)
    excel_bytes = _render_excel_summary(schedules)
    pdf_bytes = _render_pdf_summary(schedules)

    document = _ensure_firestore_document(firestore_client, account_id)
    existing = _load_document(document)
    merged_existing = dict(existing)
    merged_existing.setdefault("gl_mapping", dict(gl_mapping))

    _persist_schedules(
        document=document,
        existing=merged_existing,
        schedules=schedules,
        payload_chunks=payload_chunks,
        excel_bytes=excel_bytes,
        pdf_bytes=pdf_bytes,
    )

    logger.info(
        "Prepared N1 rent increase schedules.",
        extra={"account_id": account_id, "lease_count": len(schedules)},
    )


def _handle_task_completed(
    *,
    account_id: str,
    firestore_client: Any,
    buildium_api: Optional[BuildiumN1API],
    api_headers: Mapping[str, str],
) -> None:
    document = _ensure_firestore_document(firestore_client, account_id)
    data = _load_document(document)
    if not data:
        logger.warning(
            "No Firestore data found for completed N1 automation.",
            extra={"account_id": account_id},
        )
        return

    n1_block = data.get("n1_increase") or {}
    schedules: List[Mapping[str, Any]] = list(n1_block.get("schedules") or [])
    if not schedules and n1_block.get("payload_chunks"):
        schedules = _combine_payload_chunks(n1_block.get("payload_chunks"))
    if not schedules:
        logger.warning(
            "No prepared schedules available for N1 completion.",
            extra={"account_id": account_id},
        )
        return

    api = buildium_api or RequestsBuildiumAPI(api_headers=api_headers)

    property_groups: Dict[str, List[Mapping[str, Any]]] = defaultdict(list)
    for schedule in schedules:
        lease_id = str(schedule.get("lease_id"))
        property_id = str(schedule.get("property_id"))
        new_rent = _decimal(schedule.get("new_rent"))
        payload = {
            "leaseId": lease_id,
            "newRent": float(new_rent),
        }
        api.update_lease(lease_id=lease_id, payload=payload)
        if schedule.get("is_extended"):
            api.extend_lease(
                lease_id=lease_id,
                end_date=schedule.get("extension_end_date"),
            )

        notice_bytes = _render_notice(schedule)
        api.upload_document(
            lease_id=lease_id,
            property_id=property_id,
            filename=f"N1-{lease_id}.pdf",
            content=notice_bytes,
            content_type="application/pdf",
        )
        property_groups[property_id].append(schedule)

    category_id = data.get("automated_tasks_category_id") or n1_block.get(
        "automated_tasks_category_id"
    )
    for property_id, schedules_for_property in property_groups.items():
        property_name = schedules_for_property[0].get("property_name", "Property")
        description = _build_serving_description(property_name, schedules_for_property)
        api.create_task(
            category_id=category_id,
            name=f"Serve N1 Notices - {property_name}",
            description=description,
        )

    n1_updates = {
        "n1_increase": {
            **n1_block,
            "completed_at": _timestamp(),
            "forms_uploaded": sum(len(v) for v in property_groups.values()),
        }
    }
    document.set(n1_updates, merge=True)

    logger.info(
        "Completed N1 rent increase fulfillment.",
        extra={
            "account_id": account_id,
            "leases_processed": sum(len(v) for v in property_groups.values()),
            "properties": len(property_groups),
        },
    )


def handle_n1_increase_automation(
    *,
    account_id: str,
    api_headers: Mapping[str, str],
    gl_mapping: Mapping[str, Any],
    webhook: Mapping[str, Any],
    firestore_client: Optional[Any] = None,
    buildium_api: Optional[BuildiumN1API] = None,
) -> None:
    """Handle Buildium N1 automation task events."""

    if firestore_client is None:
        from google.cloud import firestore  # type: ignore

        firestore_client = firestore.Client(database=BUILDUM_FIRESTORE_DATABASE)

    event_type = _extract_event_type(webhook)
    task_block = _extract_task_block(webhook)

    if _normalize(event_type) == "taskcreated":
        _handle_task_created(
            account_id=account_id,
            api_headers=api_headers,
            gl_mapping=gl_mapping,
            firestore_client=firestore_client,
            buildium_api=buildium_api,
        )
        return

    if _normalize(event_type) == "taskstatuschanged" and task_block:
        status = _extract_task_status(task_block, webhook)
        if _normalize(status) == "completed":
            _handle_task_completed(
                account_id=account_id,
                firestore_client=firestore_client,
                buildium_api=buildium_api,
                api_headers=api_headers,
            )
        else:
            logger.info(
                "Ignoring N1 automation status transition.",
                extra={"account_id": account_id, "status": status},
            )


__all__ = [
    "handle_n1_increase_automation",
    "RequestsBuildiumAPI",
    "BuildiumN1API",
]

