
"""Utilities for preparing Buildium N1 rent increase payloads."""

from __future__ import annotations

import base64
import importlib
import json
import logging
import sys
import zlib
from dataclasses import dataclass
from decimal import Decimal
from hashlib import sha256
from types import ModuleType
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Sequence

logger = logging.getLogger(__name__)

ENCRYPTION_ALGORITHM = "xor+zlib"
ENCRYPTION_KEY_VERSION = "v1"
ENCRYPTION_SECRET = "buildium-n1"


@dataclass
class LeaseIncreaseContext:
    """Collected data required to compute an N1 schedule."""

    lease: Mapping[str, Any]
    lease_id: str
    property_id: str
    unit_id: str
    property_name: str
    unit_name: str
    lease_notes: Sequence[Mapping[str, Any]]
    building_notes: Sequence[Mapping[str, Any]]
    recurring_transactions: Sequence[Mapping[str, Any]]
    agi_summary: Mapping[str, Any]
    market_rent: Decimal


@dataclass
class GatheredLeases:
    """Eligible leases and any filtered results."""

    eligible: List[LeaseIncreaseContext]
    excluded: List[Mapping[str, Any]]


@dataclass
class N1PreparedData:
    """Final payload details produced for Firestore storage."""

    schedules: List[Mapping[str, Any]]
    payload_chunks: List[Mapping[str, Any]]
    payload_entries: List[Mapping[str, Any]]
    excluded: List[Mapping[str, Any]]


_WORKFLOW_MODULE: Optional[ModuleType] = None


def _workflow() -> ModuleType:
    """Return the :mod:`my_app.tasks.n1_increase` module."""

    global _WORKFLOW_MODULE
    if _WORKFLOW_MODULE is None:
        module = sys.modules.get("my_app.tasks.n1_increase")
        if module is None:
            module = importlib.import_module("my_app.tasks.n1_increase")
        _WORKFLOW_MODULE = module
    return _WORKFLOW_MODULE


def _decimal(value: Any, *, default: Decimal = Decimal("0")) -> Decimal:
    return _workflow()._decimal(value, default=default)


def _to_serializable_decimal(value: Decimal) -> str:
    return _workflow()._to_serializable_decimal(value)


def _extract_identifier(data: Mapping[str, Any], *keys: str) -> Optional[str]:
    return _workflow()._extract_identifier(data, *keys)


def _extract_rent_amount(lease: Mapping[str, Any]) -> Decimal:
    return _workflow()._extract_rent_amount(lease)


def _determine_effective_date(lease: Mapping[str, Any]) -> Optional[str]:
    return _workflow()._determine_effective_date(lease)


def _detect_extended_lease(lease: Mapping[str, Any]) -> bool:
    return _workflow()._detect_extended_lease(lease)


def _determine_extension_end_date(lease: Mapping[str, Any]) -> Optional[str]:
    return _workflow()._determine_extension_end_date(lease)


def _determine_increase_rate(property_id: str, rates: Mapping[str, Any]) -> Decimal:
    return _workflow()._determine_increase_rate(property_id, rates)


def _legal_round(amount: Decimal) -> Decimal:
    return _workflow()._legal_round(amount)


def _normalize(value: Optional[str]) -> Optional[str]:
    return _workflow()._normalize(value)


def prepare_n1_data(
    api: "BuildiumN1API",
    *,
    rates: Mapping[str, Any],
    gl_mapping: Mapping[str, Any],
    max_payload_bytes: int,
    encryption_secret: str = ENCRYPTION_SECRET,
) -> N1PreparedData:
    """Collect schedules, metadata, and encrypted payload entries."""

    gathered = gather_leases_for_increase(api, gl_mapping=gl_mapping)
    schedules = generate_increases(gathered.eligible, rates=rates, gl_mapping=gl_mapping)
    entries = [
        _build_payload_entry(context, schedule, api, gl_mapping)
        for context, schedule in zip(gathered.eligible, schedules)
    ]
    payload_chunks = build_encrypted_chunks(
        entries,
        max_bytes=max_payload_bytes,
        encryption_secret=encryption_secret,
    )
    return N1PreparedData(
        schedules=schedules,
        payload_chunks=payload_chunks,
        payload_entries=entries,
        excluded=gathered.excluded,
    )


def gather_leases_for_increase(
    api: "BuildiumN1API",
    *,
    gl_mapping: Mapping[str, Any],
) -> GatheredLeases:
    """Return eligible leases along with any filtered entries."""

    leases = list(api.list_eligible_leases())
    eligible: List[LeaseIncreaseContext] = []
    excluded: List[Mapping[str, Any]] = []

    for lease in leases:
        if not isinstance(lease, Mapping):
            continue

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

        lease_notes = _safe_sequence_call(api, "list_lease_notes", lease_id)
        building_notes = _safe_sequence_call(api, "list_building_notes", property_id)

        exclusion = _determine_exclusion(lease, lease_notes, building_notes)
        if exclusion:
            excluded.append({"lease_id": lease_id, "reason": exclusion})
            continue

        recurring = _safe_sequence_call(api, "list_recurring_transactions", lease_id)
        agi_summary = _safe_mapping_call(
            api,
            "get_above_guideline_increase",
            lease_id=str(lease_id),
        )

        market_info = _safe_mapping_call(
            api,
            "get_market_rent",
            property_id=str(property_id),
            unit_id=str(unit_id),
        )
        market_rent = _decimal(
            market_info.get("marketRent")
            or market_info.get("amount")
            or market_info.get("rent")
        )

        context = LeaseIncreaseContext(
            lease=lease,
            lease_id=str(lease_id),
            property_id=str(property_id),
            unit_id=str(unit_id),
            property_name=property_name,
            unit_name=unit_name,
            lease_notes=lease_notes,
            building_notes=building_notes,
            recurring_transactions=recurring,
            agi_summary=agi_summary,
            market_rent=market_rent,
        )
        eligible.append(context)

    return GatheredLeases(eligible=eligible, excluded=excluded)


def generate_increases(
    contexts: Sequence[LeaseIncreaseContext],
    *,
    rates: Mapping[str, Any],
    gl_mapping: Mapping[str, Any],
) -> List[Mapping[str, Any]]:
    """Compute increase schedules for the supplied contexts."""

    schedules: List[Mapping[str, Any]] = []
    for context in contexts:
        schedules.append(_build_schedule(context, rates=rates, gl_mapping=gl_mapping))
    return schedules


def build_encrypted_chunks(
    entries: Sequence[Mapping[str, Any]],
    *,
    max_bytes: int,
    encryption_secret: str = ENCRYPTION_SECRET,
) -> List[Mapping[str, Any]]:
    """Return encrypted payload chunks honouring the size constraint."""

    chunks: List[Mapping[str, Any]] = []
    buffer: List[Mapping[str, Any]] = []

    for entry in entries:
        candidate = buffer + [entry]
        encoded = _encode_entries(candidate, encryption_secret)
        if len(encoded.encode("ascii")) > max_bytes and buffer:
            chunks.append(_encode_chunk(buffer, encryption_secret))
            buffer = [entry]
            continue
        if len(encoded.encode("ascii")) > max_bytes:
            logger.warning(
                "Single entry exceeds maximum payload size; emitting dedicated chunk.",
                extra={"lease_id": entry.get("schedule", {}).get("lease_id")},
            )
            chunks.append(_encode_chunk(candidate, encryption_secret))
            buffer = []
            continue
        buffer = candidate

    if buffer:
        chunks.append(_encode_chunk(buffer, encryption_secret))

    return chunks


def decode_payload_chunk(
    chunk: Mapping[str, Any],
    *,
    encryption_secret: str = ENCRYPTION_SECRET,
) -> List[Mapping[str, Any]]:
    """Decode a stored payload chunk to its JSON representation."""

    payload = chunk.get("payload")
    if not isinstance(payload, str):
        return []

    encryption_info = chunk.get("encryption")
    if isinstance(encryption_info, Mapping):
        algorithm = encryption_info.get("algorithm")
        if algorithm == ENCRYPTION_ALGORITHM:
            try:
                return _decode_encrypted_payload(payload, encryption_secret)
            except Exception:  # pragma: no cover - defensive
                logger.exception("Failed to decode encrypted N1 payload chunk")
                return []

    # Legacy fallback: plain base64 encoded JSON.
    try:
        decoded = base64.b64decode(payload.encode("ascii"))
        data = json.loads(decoded.decode("utf-8"))
    except Exception:
        logger.exception("Failed to decode legacy payload chunk")
        return []

    if isinstance(data, Sequence):
        return [
            {"schedule": dict(item)}
            for item in data
            if isinstance(item, Mapping)
        ]
    if isinstance(data, Mapping):
        return [{"schedule": dict(data)}]
    return []


def _build_schedule(
    context: LeaseIncreaseContext,
    *,
    rates: Mapping[str, Any],
    gl_mapping: Mapping[str, Any],
) -> Mapping[str, Any]:
    current_rent = _calculate_current_rent(context, gl_mapping)
    legal_rate = _determine_increase_rate(context.property_id, rates)
    agi_percent = _decimal(
        context.agi_summary.get("percent")
        or context.agi_summary.get("percentage")
        or context.agi_summary.get("agiPercent")
    )
    agi_monthly = _decimal(
        context.agi_summary.get("monthlyAmount")
        or context.agi_summary.get("monthly_adjustment")
        or context.agi_summary.get("monthlyIncrease")
        or context.agi_summary.get("agiMonthlyAmount")
    )

    percent_based = _legal_round(current_rent * (legal_rate + agi_percent))
    increase_amount = _legal_round(percent_based + agi_monthly)
    new_rent = _legal_round(current_rent + increase_amount)

    monthly_percent = Decimal("0")
    if current_rent and agi_monthly:
        monthly_percent = (agi_monthly / current_rent).quantize(Decimal("0.0001"))

    total_percent = legal_rate + agi_percent + monthly_percent

    schedule: MutableMapping[str, Any] = {
        "lease_id": context.lease_id,
        "property_id": context.property_id,
        "unit_id": context.unit_id,
        "property_name": context.property_name,
        "unit_name": context.unit_name,
        "current_rent": _to_serializable_decimal(current_rent),
        "new_rent": _to_serializable_decimal(new_rent),
        "increase_rate": str(total_percent),
        "increase_rate_percent": f"{(total_percent * Decimal('100')).quantize(Decimal('0.01'))}%",
        "increase_amount": _to_serializable_decimal(increase_amount),
        "market_rent": _to_serializable_decimal(context.market_rent),
        "agi_amount": _to_serializable_decimal(agi_monthly),
        "agi_percent": f"{((agi_percent + monthly_percent) * Decimal('100')).quantize(Decimal('0.01'))}%",
        "effective_date": _determine_effective_date(context.lease),
        "is_extended": _detect_extended_lease(context.lease),
        "extension_end_date": _determine_extension_end_date(context.lease),
    }
    return dict(schedule)


def _build_payload_entry(
    context: LeaseIncreaseContext,
    schedule: Mapping[str, Any],
    api: "BuildiumN1API",
    gl_mapping: Mapping[str, Any],
) -> Mapping[str, Any]:
    return {
        "schedule": dict(schedule),
        "lease": {
            "id": context.lease_id,
            "property_id": context.property_id,
            "unit_id": context.unit_id,
            "property_name": context.property_name,
            "unit_name": context.unit_name,
            "residents": _extract_residents(context.lease),
            "effective_date": schedule.get("effective_date"),
            "is_extended": schedule.get("is_extended"),
            "extension_end_date": schedule.get("extension_end_date"),
        },
        "notes": {
            "lease": _sanitize_notes(context.lease_notes),
            "building": _sanitize_notes(context.building_notes),
        },
        "recurring_transactions": _sanitize_recurring(context.recurring_transactions, gl_mapping),
        "agi": _sanitize_agi(context.agi_summary, api),
        "market_rent": schedule.get("market_rent"),
    }


def _calculate_current_rent(
    context: LeaseIncreaseContext,
    gl_mapping: Mapping[str, Any],
) -> Decimal:
    rent_charges = Decimal("0")
    found = False
    for txn in context.recurring_transactions:
        if not isinstance(txn, Mapping):
            continue
        if not _is_rent_charge(txn, gl_mapping):
            continue
        rent_charges += _decimal(txn.get("amount"))
        found = True
    if found:
        return rent_charges
    return _extract_rent_amount(context.lease)


def _is_rent_charge(transaction: Mapping[str, Any], gl_mapping: Mapping[str, Any]) -> bool:
    gl_account = str(
        transaction.get("glAccountNumber")
        or transaction.get("glAccount")
        or ""
    ).strip()
    if gl_account and gl_account in gl_mapping:
        return True
    category = _normalize(str(transaction.get("type") or transaction.get("chargeType") or ""))
    if category in {"rent", "leasecharge", "monthlyrent"}:
        return True
    return False


def _sanitize_notes(notes: Sequence[Mapping[str, Any]]) -> List[Mapping[str, Any]]:
    sanitized: List[Mapping[str, Any]] = []
    for note in notes:
        if not isinstance(note, Mapping):
            continue
        sanitized.append(
            {
                "body": str(note.get("body") or note.get("note") or note.get("text") or ""),
                "created_at": _string_value(note.get("createdAt") or note.get("created_at") or note.get("createdOn")),
                "author": str(note.get("author") or note.get("createdBy") or note.get("user") or ""),
                "type": str(note.get("type") or note.get("category") or ""),
            }
        )
    return sanitized


def _sanitize_recurring(
    transactions: Sequence[Mapping[str, Any]],
    gl_mapping: Mapping[str, Any],
) -> List[Mapping[str, Any]]:
    sanitized: List[Mapping[str, Any]] = []
    for txn in transactions:
        if not isinstance(txn, Mapping):
            continue
        amount = _to_serializable_decimal(_decimal(txn.get("amount")))
        sanitized.append(
            {
                "amount": amount,
                "description": str(txn.get("description") or txn.get("memo") or ""),
                "gl_account_number": str(txn.get("glAccountNumber") or txn.get("glAccount") or ""),
                "type": str(txn.get("type") or txn.get("chargeType") or ""),
                "start_date": _string_value(txn.get("startDate") or txn.get("start_date")),
                "end_date": _string_value(txn.get("endDate") or txn.get("end_date")),
                "is_rent": _is_rent_charge(txn, gl_mapping),
            }
        )
    return sanitized


def _sanitize_agi(summary: Mapping[str, Any], api: "BuildiumN1API") -> Mapping[str, Any]:
    if not isinstance(summary, Mapping):
        return {}
    monthly_amount = _decimal(
        summary.get("monthlyAmount")
        or summary.get("monthly_adjustment")
        or summary.get("monthlyIncrease")
        or summary.get("agiMonthlyAmount")
    )
    percent = _decimal(summary.get("percent") or summary.get("percentage") or summary.get("agiPercent"))
    data: MutableMapping[str, Any] = {
        "monthly_amount": _to_serializable_decimal(monthly_amount),
        "percent": str(percent),
        "description": str(summary.get("description") or summary.get("note") or ""),
        "effective_date": _string_value(summary.get("effectiveDate") or summary.get("startDate")),
    }

    document_id = summary.get("documentId") or summary.get("downloadId") or summary.get("attachmentId")
    if document_id:
        document_content = _resolve_presigned_document(api, str(document_id))
        if document_content:
            data["document"] = {"id": str(document_id), "content": document_content}

    return dict(data)


def _resolve_presigned_document(api: "BuildiumN1API", download_id: str) -> Optional[str]:
    getter = getattr(api, "get_presigned_download", None)
    downloader = getattr(api, "download_presigned_url", None)
    if getter is None or downloader is None:
        return None
    try:
        metadata = getter(download_id)
    except Exception:  # pragma: no cover - defensive
        logger.exception("Failed to resolve presigned download metadata", extra={"download_id": download_id})
        return None
    url = ""
    if isinstance(metadata, Mapping):
        url = str(metadata.get("url") or metadata.get("downloadUrl") or metadata.get("href") or "")
    if not url:
        return None
    try:
        binary = downloader(url)
    except Exception:  # pragma: no cover - defensive
        logger.exception("Failed to download presigned content", extra={"download_id": download_id})
        return None
    if not isinstance(binary, (bytes, bytearray)):
        return None
    return base64.b64encode(bytes(binary)).decode("ascii")


def _extract_residents(lease: Mapping[str, Any]) -> List[str]:
    residents: List[str] = []
    for key in ("residents", "tenants", "occupants"):
        value = lease.get(key)
        if isinstance(value, Sequence) and not isinstance(value, (bytes, str)):
            for item in value:
                if not isinstance(item, Mapping):
                    continue
                for name_key in ("name", "fullName", "full_name", "displayName"):
                    name = item.get(name_key)
                    if name:
                        residents.append(str(name))
                        break
    return residents


def _determine_exclusion(
    lease: Mapping[str, Any],
    lease_notes: Sequence[Mapping[str, Any]],
    building_notes: Sequence[Mapping[str, Any]],
) -> Optional[str]:
    if lease.get("allowRentIncrease") is False:
        return "blocked:flagged"
    for key in ("rentIncreaseEligible", "eligibleForIncrease", "allowIncrease"):
        value = lease.get(key)
        if value is False:
            return f"blocked:{key}"

    if _contains_blocking_note(lease_notes):
        return "blocked:lease_note"
    if _contains_blocking_note(building_notes):
        return "blocked:building_note"
    return None


def _contains_blocking_note(notes: Sequence[Mapping[str, Any]]) -> bool:
    for note in notes:
        if not isinstance(note, Mapping):
            continue
        text = str(note.get("body") or note.get("text") or note.get("note") or "")
        normalized = (_normalize(text) or "")
        if any(token in normalized for token in ("donotincrease", "skipn1", "n1block", "n1hold")):
            return True
    return False


def _safe_sequence_call(api: Any, method_name: str, *args: Any, **kwargs: Any) -> List[Mapping[str, Any]]:
    method = getattr(api, method_name, None)
    if method is None:
        return []
    try:
        result = method(*args, **kwargs)
    except Exception:  # pragma: no cover - defensive
        logger.exception("Failed to call Buildium API sequence method", extra={"method": method_name})
        return []
    return _coerce_sequence(result)


def _safe_mapping_call(api: Any, method_name: str, *args: Any, **kwargs: Any) -> Mapping[str, Any]:
    method = getattr(api, method_name, None)
    if method is None:
        return {}
    try:
        result = method(*args, **kwargs)
    except Exception:  # pragma: no cover - defensive
        logger.exception("Failed to call Buildium API mapping method", extra={"method": method_name})
        return {}
    if isinstance(result, Mapping):
        return dict(result)
    return {}


def _coerce_sequence(value: Any) -> List[Mapping[str, Any]]:
    if isinstance(value, Mapping):
        items = value.get("items")
        if isinstance(items, Iterable):
            return [dict(item) for item in items if isinstance(item, Mapping)]
        return [dict(value)]
    if isinstance(value, Sequence) and not isinstance(value, (bytes, str)):
        return [dict(item) for item in value if isinstance(item, Mapping)]
    return []


def _string_value(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _encode_entries(entries: Sequence[Mapping[str, Any]], secret: str) -> str:
    serialized = json.dumps(entries, separators=(",", ":"), default=str).encode("utf-8")
    compressed = zlib.compress(serialized)
    key = sha256(secret.encode("utf-8")).digest()
    encrypted = bytes(b ^ key[idx % len(key)] for idx, b in enumerate(compressed))
    return base64.b64encode(encrypted).decode("ascii")


def _encode_chunk(entries: Sequence[Mapping[str, Any]], secret: str) -> Mapping[str, Any]:
    return {
        "payload": _encode_entries(entries, secret),
        "count": len(entries),
        "encryption": {
            "algorithm": ENCRYPTION_ALGORITHM,
            "key_version": ENCRYPTION_KEY_VERSION,
        },
    }


def _decode_encrypted_payload(payload: str, secret: str) -> List[Mapping[str, Any]]:
    encrypted = base64.b64decode(payload.encode("ascii"))
    key = sha256(secret.encode("utf-8")).digest()
    compressed = bytes(b ^ key[idx % len(key)] for idx, b in enumerate(encrypted))
    serialized = zlib.decompress(compressed)
    data = json.loads(serialized.decode("utf-8"))
    if isinstance(data, Sequence) and not isinstance(data, (bytes, str)):
        return [
            _ensure_schedule_mapping(item)
            for item in data
            if isinstance(item, Mapping)
        ]
    if isinstance(data, Mapping):
        return [_ensure_schedule_mapping(data)]
    return []


def _ensure_schedule_mapping(item: Mapping[str, Any]) -> Mapping[str, Any]:
    if "schedule" in item and isinstance(item["schedule"], Mapping):
        schedule = dict(item["schedule"])
    else:
        schedule = dict(item)
    return {**dict(item), "schedule": schedule}


__all__ = [
    "LeaseIncreaseContext",
    "GatheredLeases",
    "N1PreparedData",
    "prepare_n1_data",
    "gather_leases_for_increase",
    "generate_increases",
    "build_encrypted_chunks",
    "decode_payload_chunk",
]
