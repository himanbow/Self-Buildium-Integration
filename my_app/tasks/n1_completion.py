"""N1 completion workflow service for Buildium automation."""

from __future__ import annotations

import base64
import importlib
import logging
import sys
from collections import defaultdict
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Iterable,
    List,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Tuple,
)

from . import n1_data

logger = logging.getLogger(__name__)

if TYPE_CHECKING:  # pragma: no cover - import for typing only
    from .n1_increase import BuildiumN1API


_WORKFLOW_MODULE: Optional[Any] = None


def _workflow() -> Any:
    """Return the :mod:`my_app.tasks.n1_increase` module."""

    global _WORKFLOW_MODULE
    if _WORKFLOW_MODULE is None:
        module = sys.modules.get("my_app.tasks.n1_increase")
        if module is None:
            module = importlib.import_module("my_app.tasks.n1_increase")
        _WORKFLOW_MODULE = module
    return _WORKFLOW_MODULE


def _coerce_string(value: Any) -> Optional[str]:
    if value is None:
        return None
    if isinstance(value, str):
        stripped = value.strip()
        return stripped or None
    try:
        return str(value)
    except Exception:  # pragma: no cover - defensive
        return None


def ensure_firestore_document(firestore_client: Any, account_id: str) -> Any:
    """Return the Firestore document used for Buildium automation."""

    workflow = _workflow()
    collection = firestore_client.collection(workflow.FIRESTORE_COLLECTION_PATH)
    return collection.document(account_id)


def load_document(document: Any) -> Mapping[str, Any]:
    """Safely deserialize a Firestore document snapshot."""

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


def decode_payload_entries(
    chunks: Sequence[Mapping[str, Any]],
    *,
    encryption_secret: str = n1_data.ENCRYPTION_SECRET,
) -> List[Mapping[str, Any]]:
    """Return the decoded payload entries for stored N1 data."""

    entries: List[Mapping[str, Any]] = []
    for chunk in chunks:
        decoded = n1_data.decode_payload_chunk(
            chunk, encryption_secret=encryption_secret
        )
        for entry in decoded:
            if isinstance(entry, Mapping):
                entries.append(entry)
    return entries


def combine_payload_entries(entries: Sequence[Mapping[str, Any]]) -> List[Mapping[str, Any]]:
    combined: List[Mapping[str, Any]] = []
    for entry in entries:
        if not isinstance(entry, Mapping):
            continue
        schedule = entry.get("schedule")
        if isinstance(schedule, Mapping):
            combined.append(dict(schedule))
    return combined


def map_entries_by_lease(
    entries: Sequence[Mapping[str, Any]]
) -> Dict[str, Mapping[str, Any]]:
    mapping: Dict[str, Mapping[str, Any]] = {}
    for entry in entries:
        if not isinstance(entry, Mapping):
            continue
        lease_id: Optional[str] = None
        schedule = entry.get("schedule")
        if isinstance(schedule, Mapping):
            lease_identifier = schedule.get("lease_id") or schedule.get("leaseId")
            if lease_identifier is not None:
                lease_id = _coerce_string(lease_identifier)
        if lease_id is None:
            lease_block = entry.get("lease")
            if isinstance(lease_block, Mapping):
                lease_identifier = (
                    lease_block.get("id")
                    or lease_block.get("lease_id")
                    or lease_block.get("leaseId")
                )
                if lease_identifier is not None:
                    lease_id = _coerce_string(lease_identifier)
        if lease_id:
            mapping[lease_id] = entry
    return mapping


def render_notice(
    schedule: Mapping[str, Any], payload_entry: Optional[Mapping[str, Any]] = None
) -> bytes:
    from . import n1_notice_pdf

    lease_info: Optional[Mapping[str, Any]] = None
    if isinstance(payload_entry, Mapping):
        lease_candidate = payload_entry.get("lease")
        if isinstance(lease_candidate, Mapping):
            lease_info = lease_candidate
    return n1_notice_pdf.create_n1_notice_pdf(schedule=schedule, lease=lease_info)


def build_serving_description(
    property_name: str, schedules: Sequence[Mapping[str, Any]]
) -> str:
    lines = [
        f"Serve N1 notices for {property_name}.",
        "",
        "Notices to deliver:",
    ]
    for schedule in schedules:
        lines.append(
            f"- Unit {schedule.get('unit_name', '')}: increase to ${schedule.get('new_rent')} "
            f"effective {schedule.get('effective_date', '')}"
        )
    lines.append("")
    lines.append("Update this task once all residents have been served.")
    return "\n".join(lines)


def fulfill_n1_completion(
    *,
    account_id: str,
    firestore_client: Any,
    api_headers: Mapping[str, str],
    buildium_api: Optional["BuildiumN1API"] = None,
    encryption_secret: str = n1_data.ENCRYPTION_SECRET,
) -> None:
    """Complete the N1 automation workflow for a finished Buildium task."""

    workflow = _workflow()
    api = buildium_api or workflow.RequestsBuildiumAPI(api_headers=api_headers)

    document = ensure_firestore_document(firestore_client, account_id)
    data = load_document(document)
    if not data:
        logger.warning(
            "No Firestore data found for completed N1 automation.",
            extra={"account_id": account_id},
        )
        return

    n1_block = dict(data.get("n1_increase") or {})
    schedules: List[Mapping[str, Any]] = list(n1_block.get("schedules") or [])
    payload_chunks = list(n1_block.get("payload_chunks") or [])
    payload_entries = decode_payload_entries(
        payload_chunks, encryption_secret=encryption_secret
    )
    if not schedules and payload_entries:
        schedules = combine_payload_entries(payload_entries)
    if not schedules:
        logger.warning(
            "No prepared schedules available for N1 completion.",
            extra={"account_id": account_id},
        )
        return

    entry_map = map_entries_by_lease(payload_entries)
    ignored_leases = _collect_ignored_leases(n1_block)
    renewal_map = _collect_lease_renewals(n1_block)

    property_groups: Dict[str, List[Tuple[Mapping[str, Any], Optional[Mapping[str, Any]]]]] = defaultdict(list)
    processed_leases: List[str] = []

    for schedule in schedules:
        lease_id = _coerce_string(schedule.get("lease_id") or schedule.get("leaseId"))
        property_id = _coerce_string(
            schedule.get("property_id") or schedule.get("propertyId")
        )
        if not lease_id or not property_id:
            continue
        if lease_id in ignored_leases:
            logger.info(
                "Skipping N1 lease due to ignore flag.",
                extra={"account_id": account_id, "lease_id": lease_id},
            )
            continue

        entry = entry_map.get(lease_id)

        _apply_lease_update(api, lease_id, schedule)
        if _should_extend(schedule):
            _extend_lease(api, lease_id, schedule)

        renewal_payload = renewal_map.get(lease_id)
        if renewal_payload:
            _trigger_lease_renewal(api, lease_id, renewal_payload, schedule, entry)

        notice_bytes = render_notice(schedule, entry)
        api.upload_document(
            lease_id=lease_id,
            property_id=property_id,
            filename=f"N1-{lease_id}.pdf",
            content=notice_bytes,
            content_type="application/pdf",
        )
        property_groups[property_id].append((schedule, entry))
        processed_leases.append(lease_id)

    summary_uploads = _upload_summary_files(api, n1_block.get("summary_files"))

    category_id = _resolve_task_category(api, data, n1_block, document)
    task_updates = _create_or_update_tasks(
        api,
        property_groups,
        category_id,
        n1_block.get("property_tasks"),
    )

    _record_completion(
        document,
        n1_block,
        processed_leases,
        ignored_leases,
        summary_uploads,
        task_updates,
    )

    logger.info(
        "Completed N1 rent increase fulfillment.",
        extra={
            "account_id": account_id,
            "leases_processed": len(processed_leases),
            "properties": len(property_groups),
            "ignored": len(ignored_leases),
        },
    )


def _apply_lease_update(
    api: "BuildiumN1API", lease_id: str, schedule: Mapping[str, Any]
) -> None:
    workflow = _workflow()
    new_rent = workflow._decimal(schedule.get("new_rent"))
    payload = {
        "leaseId": lease_id,
        "newRent": float(new_rent),
    }
    api.update_lease(lease_id=lease_id, payload=payload)


def _should_extend(schedule: Mapping[str, Any]) -> bool:
    value = schedule.get("is_extended")
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        normalized = value.strip().lower()
        return normalized in {"true", "1", "yes"}
    return bool(value)


def _extend_lease(
    api: "BuildiumN1API", lease_id: str, schedule: Mapping[str, Any]
) -> None:
    end_date = schedule.get("extension_end_date")
    if isinstance(end_date, Mapping):
        end_date = end_date.get("value")
    api.extend_lease(
        lease_id=lease_id,
        end_date=_coerce_string(end_date),
    )


def _trigger_lease_renewal(
    api: "BuildiumN1API",
    lease_id: str,
    config: Mapping[str, Any],
    schedule: Mapping[str, Any],
    entry: Optional[Mapping[str, Any]],
) -> None:
    payload = _build_lease_renewal_payload(lease_id, config, schedule, entry)
    if payload:
        api.create_lease_renewal(lease_id=lease_id, payload=payload)


def _build_lease_renewal_payload(
    lease_id: str,
    config: Mapping[str, Any],
    schedule: Mapping[str, Any],
    entry: Optional[Mapping[str, Any]],
) -> Mapping[str, Any]:
    workflow = _workflow()
    payload: MutableMapping[str, Any] = {}

    if isinstance(config, Mapping):
        base = config.get("payload") if isinstance(config.get("payload"), Mapping) else config
        payload.update({str(k): v for k, v in base.items()})

    payload.setdefault("leaseId", lease_id)

    effective_date = schedule.get("effective_date")
    if not effective_date and isinstance(entry, Mapping):
        lease_block = entry.get("lease")
        if isinstance(lease_block, Mapping):
            effective_date = lease_block.get("effective_date")
    if effective_date and "startDate" not in payload and "start_date" not in payload:
        payload["startDate"] = effective_date

    end_date = schedule.get("extension_end_date")
    if not end_date and isinstance(entry, Mapping):
        lease_block = entry.get("lease")
        if isinstance(lease_block, Mapping):
            end_date = lease_block.get("extension_end_date")
    if end_date and "endDate" not in payload and "end_date" not in payload:
        payload["endDate"] = end_date

    if "rentAmount" not in payload and "rent_amount" not in payload:
        new_rent = workflow._decimal(schedule.get("new_rent"))
        payload["rentAmount"] = float(new_rent)

    return dict(payload)


def _collect_ignored_leases(n1_block: Mapping[str, Any]) -> List[str]:
    ignored: List[str] = []
    for key in ("ignored_leases", "skipped_leases", "excluded_leases"):
        value = n1_block.get(key)
        if isinstance(value, Mapping):
            candidates: Iterable[Any] = value.values()
        else:
            candidates = value or []
        if isinstance(candidates, Iterable) and not isinstance(candidates, (str, bytes)):
            for item in candidates:
                lease_id = None
                if isinstance(item, Mapping):
                    lease_id = (
                        item.get("lease_id")
                        or item.get("leaseId")
                        or item.get("id")
                        or item.get("lease")
                    )
                else:
                    lease_id = item
                candidate = _coerce_string(lease_id)
                if candidate and candidate not in ignored:
                    ignored.append(candidate)
    return ignored


def _collect_lease_renewals(
    n1_block: Mapping[str, Any]
) -> Dict[str, Mapping[str, Any]]:
    renewals: Dict[str, Mapping[str, Any]] = {}
    raw = n1_block.get("lease_renewals")
    if isinstance(raw, Mapping):
        for key, value in raw.items():
            lease_id = _coerce_string(key)
            if not lease_id:
                continue
            if isinstance(value, Mapping):
                renewals[lease_id] = dict(value)
    elif isinstance(raw, Sequence) and not isinstance(raw, (str, bytes)):
        for item in raw:
            if not isinstance(item, Mapping):
                continue
            lease_id = _coerce_string(
                item.get("lease_id") or item.get("leaseId") or item.get("id")
            )
            if lease_id:
                renewals[lease_id] = dict(item)
    return renewals


def _upload_summary_files(
    api: "BuildiumN1API", summary_files: Optional[Mapping[str, Any]]
) -> List[Mapping[str, Any]]:
    uploads: List[Mapping[str, Any]] = []
    if not isinstance(summary_files, Mapping):
        return uploads

    for key, encoded in summary_files.items():
        if not isinstance(encoded, str) or not encoded:
            continue
        try:
            content = base64.b64decode(encoded.encode("ascii"))
        except Exception:  # pragma: no cover - defensive
            logger.exception(
                "Failed to decode stored summary file.", extra={"label": key}
            )
            continue

        filename, content_type = _summary_metadata(key)
        presigned = api.request_presigned_upload(
            filename=filename,
            content_type=content_type,
            metadata={"label": key, "document_type": "n1_summary"},
        )
        if not isinstance(presigned, Mapping):
            continue
        url = _coerce_string(
            presigned.get("url")
            or presigned.get("uploadUrl")
            or presigned.get("href")
        )
        fields = presigned.get("fields")
        if not url:
            continue
        if not isinstance(fields, Mapping):
            fields = {}
        api.upload_to_presigned_url(
            url=url,
            fields=fields,
            content=content,
            content_type=content_type,
        )
        uploads.append({"label": key, "filename": filename})
    return uploads


def _summary_metadata(label: str) -> Tuple[str, str]:
    normalized = (label or "").strip().lower()
    if normalized == "excel":
        return ("N1 Summary.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    if normalized == "pdf":
        return ("N1 Summary.pdf", "application/pdf")
    return (f"N1 Summary - {label}.bin", "application/octet-stream")


def _resolve_task_category(
    api: "BuildiumN1API",
    account_data: Mapping[str, Any],
    n1_block: Mapping[str, Any],
    document: Any,
) -> Optional[str]:
    for source in (n1_block, account_data):
        candidate = source.get("automated_tasks_category_id")
        identifier = _coerce_string(candidate)
        if identifier:
            return identifier

    category_name = _coerce_string(
        n1_block.get("task_category_name")
        or account_data.get("automated_tasks_category_name")
        or "Automation"
    ) or "Automation"

    existing = api.list_task_categories()
    for category in existing:
        name = _coerce_string(
            category.get("name")
            or category.get("taskCategoryName")
            or category.get("displayName")
        )
        identifier = _coerce_string(
            category.get("id")
            or category.get("taskCategoryId")
            or category.get("task_category_id")
        )
        if name and identifier and name.lower() == category_name.lower():
            document.set({"automated_tasks_category_id": identifier}, merge=True)
            return identifier

    created = api.create_task_category(name=category_name)
    identifier = _coerce_string(
        created.get("id")
        or created.get("taskCategoryId")
        or created.get("task_category_id")
        or created.get("category_id")
    )
    if identifier:
        document.set({"automated_tasks_category_id": identifier}, merge=True)
    return identifier


def _create_or_update_tasks(
    api: "BuildiumN1API",
    property_groups: Mapping[str, Sequence[Tuple[Mapping[str, Any], Optional[Mapping[str, Any]]]]],
    category_id: Optional[str],
    existing_tasks: Optional[Mapping[str, Any]],
) -> Dict[str, Mapping[str, Any]]:
    updates: Dict[str, Mapping[str, Any]] = {}

    task_map: Dict[str, Mapping[str, Any]] = {}
    if isinstance(existing_tasks, Mapping):
        for key, value in existing_tasks.items():
            task_map[_coerce_string(key) or ""] = (
                value if isinstance(value, Mapping) else {"task_id": value}
            )

    for property_id, entries in property_groups.items():
        if not entries:
            continue
        schedules = [schedule for schedule, _ in entries]
        property_name = _coerce_string(schedules[0].get("property_name")) or "Property"
        description = build_serving_description(property_name, schedules)

        existing = task_map.get(property_id)
        task_id = _coerce_string(existing.get("task_id")) if isinstance(existing, Mapping) else None

        if task_id:
            api.create_task_history_comment(
                task_id=task_id,
                body="N1 automation completed. Notices uploaded to lease documents.",
            )
            updates[property_id] = {"task_id": task_id, "status": "updated"}
            continue

        created = api.create_task(
            category_id=category_id,
            name=f"Serve N1 Notices - {property_name}",
            description=description,
        )
        new_id = _coerce_string(
            created.get("id")
            or created.get("taskId")
            or created.get("task_id")
        )
        if not new_id:
            continue
        updates[property_id] = {"task_id": new_id, "status": "created"}

    return updates


def _record_completion(
    document: Any,
    n1_block: Mapping[str, Any],
    processed_leases: Sequence[str],
    ignored_leases: Sequence[str],
    summary_uploads: Sequence[Mapping[str, Any]],
    task_updates: Mapping[str, Mapping[str, Any]],
) -> None:
    workflow = _workflow()
    merged: MutableMapping[str, Any] = dict(n1_block)
    merged["completed_at"] = workflow._timestamp()
    merged["forms_uploaded"] = len(processed_leases)
    if ignored_leases:
        merged["ignored_leases"] = list(dict.fromkeys(ignored_leases))
    if summary_uploads:
        merged["summary_uploads"] = list(summary_uploads)
    if task_updates:
        existing = {}
        current = n1_block.get("property_tasks")
        if isinstance(current, Mapping):
            for key, value in current.items():
                existing[_coerce_string(key) or ""] = (
                    value if isinstance(value, Mapping) else {"task_id": value}
                )
        for key, value in task_updates.items():
            existing[_coerce_string(key) or ""] = dict(value)
        merged["property_tasks"] = existing

    document.set({"n1_increase": merged}, merge=True)


__all__ = [
    "ensure_firestore_document",
    "load_document",
    "decode_payload_entries",
    "combine_payload_entries",
    "map_entries_by_lease",
    "render_notice",
    "build_serving_description",
    "fulfill_n1_completion",
]
