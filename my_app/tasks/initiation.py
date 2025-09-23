"""Automation workflow for Buildium initiation tasks."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, Mapping, MutableMapping, Optional, Protocol, Sequence
from urllib import request as urllib_request

from ..services.account_context import BUILDUM_FIRESTORE_DATABASE

logger = logging.getLogger(__name__)

FIRESTORE_COLLECTION_PATH = "buildium_accounts"
AUTOMATED_TASK_CATEGORY_NAME = "Automated Tasks"
INITIATION_COMPLETED_FIELD = "initiation_completed"


class BuildiumInitiationAPI(Protocol):
    """Interface for the Buildium APIs leveraged by the initiation workflow."""

    def list_gl_accounts(self) -> Sequence[Mapping[str, Any]]:
        ...

    def list_task_categories(self) -> Sequence[Mapping[str, Any]]:
        ...

    def get_company_profile(self) -> Mapping[str, Any]:
        ...

    def list_document_templates(self) -> Sequence[Mapping[str, Any]]:
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
    """Minimal Buildium API implementation backed by HTTP requests."""

    api_headers: Mapping[str, str]
    base_url: str = "https://api.buildium.com/v1"

    def __post_init__(self) -> None:
        self._base_url = self.base_url.rstrip("/")
        self._headers = dict(self.api_headers)

    def _get(self, path: str) -> Any:
        request = urllib_request.Request(
            f"{self._base_url}/{path.lstrip('/')}",
            method="GET",
            headers=self._headers,
        )
        with urllib_request.urlopen(request) as response:  # pragma: no cover - network
            payload = response.read()
        if not payload:
            return {}
        payload = json.loads(payload.decode("utf-8"))
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

    def list_gl_accounts(self) -> Sequence[Mapping[str, Any]]:
        data = self._get("accounting/glaccounts")
        if isinstance(data, Sequence):
            return list(data)
        if isinstance(data, Mapping):
            return list(data.values())
        return []

    def list_task_categories(self) -> Sequence[Mapping[str, Any]]:
        data = self._get("tasks/categories")
        if isinstance(data, Sequence):
            return list(data)
        if isinstance(data, Mapping):
            return list(data.values())
        return []

    def get_company_profile(self) -> Mapping[str, Any]:
        profile = self._get("company")
        return profile if isinstance(profile, Mapping) else {"raw": profile}

    def list_document_templates(self) -> Sequence[Mapping[str, Any]]:
        data = self._get("documents/templates")
        if isinstance(data, Sequence):
            return list(data)
        if isinstance(data, Mapping):
            return list(data.values())
        return []

    def create_task(
        self,
        *,
        category_id: Optional[str],
        name: str,
        description: str,
    ) -> Mapping[str, Any]:
        payload: Dict[str, Any] = {
            "name": name,
            "description": description,
        }
        if category_id:
            payload["taskCategoryId"] = category_id
        return self._post("tasks", payload)


def _timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def _find_automated_category_id(categories: Sequence[Mapping[str, Any]]) -> Optional[str]:
    """Identify the "Automated Tasks" category regardless of API field naming."""
    for category in categories:
        if not isinstance(category, Mapping):
            continue
        raw_name = str(category.get("name") or category.get("taskCategoryName") or "")
        normalized = "".join(ch for ch in raw_name.lower() if ch.isalnum())
        if normalized == "automatedtasks":
            value = category.get("id") or category.get("taskCategoryId")
            return str(value) if value is not None else None
    return None


def _merge_dict(target: MutableMapping[str, Any], updates: Mapping[str, Any]) -> None:
    """Recursively merge Buildium metadata into the Firestore document payload."""
    for key, value in updates.items():
        if (
            key in target
            and isinstance(target[key], MutableMapping)
            and isinstance(value, Mapping)
        ):
            _merge_dict(target[key], value)
        else:
            target[key] = value


def _select_first_value(
    data: Mapping[str, Any],
    *,
    candidates: Sequence[str],
) -> Optional[Any]:
    """Support tolerant lookups across the many Buildium field aliases."""
    lowered = {key.lower() for key in candidates}
    for key, value in data.items():
        if str(key).lower() in lowered and value is not None:
            return value
    return None


def _normalize_gl_accounts(
    accounts: Sequence[Mapping[str, Any]]
) -> Sequence[Mapping[str, str]]:
    """Coerce Buildium GL payloads into stable id/name pairs for Firestore."""
    normalized: list[Dict[str, str]] = []
    for account in accounts:
        if not isinstance(account, Mapping):
            continue
        normalized_account: Dict[str, str] = {}
        identifier = _select_first_value(
            account,
            candidates=(
                "id",
                "glAccountId",
                "accountId",
            ),
        )
        if identifier is not None:
            normalized_account["id"] = str(identifier)

        name = _select_first_value(
            account,
            candidates=(
                "name",
                "glAccountName",
                "accountName",
                "description",
            ),
        )
        if name is not None:
            normalized_account["name"] = str(name)

        if normalized_account:
            if "id" not in normalized_account:
                # Firestore documents require stable key values, but
                # maintaining entries with a name-only payload still offers
                # value for operators during onboarding.
                normalized_account.setdefault("id", "")
            normalized.append(normalized_account)
    return normalized


def _build_onboarding_description(
    *, company: Mapping[str, Any], gl_accounts: Sequence[Mapping[str, Any]]
) -> str:
    """Summarize key company data in a friendly onboarding checklist."""
    company_name = company.get("name") or company.get("legalName") or "your organization"
    account_lines = []
    for account in gl_accounts[:5]:
        if not isinstance(account, Mapping):
            continue
        name = str(account.get("name") or "").strip()
        identifier = str(account.get("id") or "").strip()
        if name and identifier:
            account_lines.append(f"- {name} (ID: {identifier})")
        elif name:
            account_lines.append(f"- {name}")
        elif identifier:
            account_lines.append(f"- ID: {identifier}")
    sample_accounts = "\n".join(account_lines)
    description = [
        "Welcome to the Naborly automated Buildium workflows!",
        "",
        f"Company: {company_name}",
        "Please upload a high-resolution property management logo and confirm that the following GL accounts are correct:",
    ]
    if sample_accounts:
        description.append(sample_accounts)
    description.extend(
        [
            "",
            "Once the logo and GL mappings are confirmed, reply in this task so we can finalize automation setup.",
        ]
    )
    return "\n".join(description)


def handle_initiation_automation(
    *,
    account_id: str,
    api_headers: Mapping[str, str],
    gl_mapping: Mapping[str, Any],
    webhook: Mapping[str, Any],
    firestore_client: Optional[Any] = None,
    buildium_api: Optional[BuildiumInitiationAPI] = None,
) -> None:
    """Fetch Buildium metadata, merge it into Firestore, and create the onboarding task.

    The handler keeps the account document up to date with GL mappings, company
    context, and templates before opening a checklist assignment for the
    property manager to confirm the configuration."""

    logger.info(
        "Starting Buildium initiation automation handler.",
        extra={
            "account_id": account_id,
            "gl_mapping_keys": sorted(gl_mapping.keys()),
            "headers": sorted(api_headers.keys()),
        },
    )

    if buildium_api is None:
        buildium_api = RequestsBuildiumAPI(api_headers=api_headers)

    if firestore_client is None:
        from google.cloud import firestore  # type: ignore

        firestore_client = firestore.Client(database=BUILDUM_FIRESTORE_DATABASE)

    gl_accounts = list(buildium_api.list_gl_accounts())
    normalized_gl_accounts = list(_normalize_gl_accounts(gl_accounts))
    categories = list(buildium_api.list_task_categories())
    company = dict(buildium_api.get_company_profile())
    templates = list(buildium_api.list_document_templates())

    automated_category_id = _find_automated_category_id(categories)

    logger.debug(
        "Fetched Buildium metadata for initiation workflow.",
        extra={
            "account_id": account_id,
            "gl_account_count": len(normalized_gl_accounts),
            "template_count": len(templates),
            "automated_category_id": automated_category_id,
        },
    )

    try:
        collection = firestore_client.collection(FIRESTORE_COLLECTION_PATH)
        document = collection.document(account_id)
    except Exception:
        logger.exception(
            "Unable to resolve Firestore document for Buildium account.",
            extra={"account_id": account_id},
        )
        raise

    existing: MutableMapping[str, Any] = {}
    try:
        snapshot = document.get()
        if getattr(snapshot, "exists", False):
            existing = snapshot.to_dict() or {}
    except Exception:
        logger.warning(
            "Failed to load existing Buildium account document; continuing with merge.",
            extra={"account_id": account_id},
        )

    updates: Dict[str, Any] = {
        "last_initiation_run": _timestamp(),
        "gl_accounts": normalized_gl_accounts,
        "gl_mapping": dict(gl_mapping),
        "company": company,
        "document_templates": templates,
        INITIATION_COMPLETED_FIELD: True,
    }
    if automated_category_id:
        updates["automated_tasks_category_id"] = automated_category_id

    merged: MutableMapping[str, Any] = dict(existing)
    _merge_dict(merged, updates)

    document.set(dict(merged), merge=True)

    logger.info(
        "Persisted Buildium initiation metadata to Firestore.",
        extra={
            "account_id": account_id,
            "gl_accounts": len(normalized_gl_accounts),
            "templates": len(templates),
        },
    )

    description = _build_onboarding_description(
        company=company, gl_accounts=normalized_gl_accounts
    )
    buildium_api.create_task(
        category_id=automated_category_id,
        name="Automation Onboarding Checklist",
        description=description,
    )

    logger.info(
        "Created Buildium onboarding confirmation task.",
        extra={"account_id": account_id, "category_id": automated_category_id},
    )

__all__ = [
    "handle_initiation_automation",
    "RequestsBuildiumAPI",
    "BuildiumInitiationAPI",
    "FIRESTORE_COLLECTION_PATH",
    "INITIATION_COMPLETED_FIELD",
]

