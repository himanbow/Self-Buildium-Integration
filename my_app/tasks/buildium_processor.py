"""Background processing for Buildium webhook payloads."""

from __future__ import annotations

import asyncio
import base64
import json
import logging
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, List, Mapping, Optional, Sequence, Tuple
from typing import Protocol

from google.api_core import exceptions as google_exceptions
from google.cloud import tasks_v2

from ..config import DEFAULT_GCP_PROJECT_ID
from ..services.account_context import BUILDUM_FIRESTORE_DATABASE

if TYPE_CHECKING:
    from ..webhooks.verification import VerifiedBuildiumWebhook
from .initiation import (
    FIRESTORE_COLLECTION_PATH as INITIATION_COLLECTION_PATH,
    INITIATION_COMPLETED_FIELD,
    handle_initiation_automation,
)
from .n1_increase import handle_n1_increase_automation

logger = logging.getLogger(__name__)

_DEFAULT_CLOUD_TASKS_QUEUE = "buildium-webhooks"
_DEFAULT_CLOUD_TASKS_LOCATION = "us-central1"
_DEFAULT_TASK_HANDLER_URL = "http://localhost:8080/tasks/buildium-webhook"

# Buildium OpenAPI client path configuration for vendored SDK.
_OPENAPI_CLIENT_PATH = Path(__file__).resolve().parents[2] / "clients" / "buildium"
_OPENAPI_CLIENT_PATH_ADDED = False


def _ensure_openapi_client_path() -> None:
    global _OPENAPI_CLIENT_PATH_ADDED
    if _OPENAPI_CLIENT_PATH_ADDED:
        return

    openapi_path = str(_OPENAPI_CLIENT_PATH)
    if os.path.isdir(openapi_path) and openapi_path not in sys.path:
        sys.path.insert(0, openapi_path)

    _OPENAPI_CLIENT_PATH_ADDED = True

CLOUD_TASKS_QUEUE_ENV = "CLOUD_TASKS_QUEUE"
CLOUD_TASKS_LOCATION_ENV = "CLOUD_TASKS_LOCATION"
TASK_HANDLER_URL_ENV = "TASK_HANDLER_URL"

# Legacy/alternate environment variable names that have been used in deployments.
LEGACY_CLOUD_TASKS_QUEUE_ENV = "BUILDUM_TASKS_QUEUE"
LEGACY_CLOUD_TASKS_LOCATION_ENV = "BUILDUM_TASKS_LOCATION"
LEGACY_TASK_HANDLER_URL_ENV = "BUILDUM_TASKS_SERVICE_URL"
CLOUD_RUN_REGION_ENV = "CLOUD_RUN_REGION"

_PROJECT_ID_ENV_CANDIDATES: Tuple[str, ...] = (
    "GOOGLE_CLOUD_PROJECT",
    "CLOUD_RUN_PROJECT",
    "GCP_PROJECT",
    "GCLOUD_PROJECT",
    "PROJECT_ID",
)


def _get_cloud_tasks_queue() -> str:
    """Resolve the Cloud Tasks queue name from environment configuration.

    Honors legacy variable names before falling back to the module default.
    """
    queue = os.getenv(CLOUD_TASKS_QUEUE_ENV)
    if queue:
        return queue

    legacy_queue = os.getenv(LEGACY_CLOUD_TASKS_QUEUE_ENV)
    if legacy_queue:
        logger.info(
            "Using legacy Cloud Tasks queue env var.",
            extra={"env": LEGACY_CLOUD_TASKS_QUEUE_ENV},
        )
        return legacy_queue

    return _DEFAULT_CLOUD_TASKS_QUEUE


def _get_cloud_tasks_location() -> str:
    """Resolve the Cloud Tasks location from environment configuration.

    Checks modern and legacy variables as well as the Cloud Run region before
    defaulting to the module constant.
    """
    location = os.getenv(CLOUD_TASKS_LOCATION_ENV)
    if location:
        return location

    legacy_location = os.getenv(LEGACY_CLOUD_TASKS_LOCATION_ENV)
    if legacy_location:
        logger.info(
            "Using legacy Cloud Tasks location env var.",
            extra={"env": LEGACY_CLOUD_TASKS_LOCATION_ENV},
        )
        return legacy_location

    cloud_run_region = os.getenv(CLOUD_RUN_REGION_ENV)
    if cloud_run_region:
        return cloud_run_region

    return _DEFAULT_CLOUD_TASKS_LOCATION


def _get_task_handler_url() -> str:
    """Resolve the Buildium task handler URL from environment configuration.

    Supports historic variable names and defaults to the local development
    endpoint.
    """
    handler_url = os.getenv(TASK_HANDLER_URL_ENV)
    if handler_url:
        return handler_url

    legacy_handler_url = os.getenv(LEGACY_TASK_HANDLER_URL_ENV)
    if legacy_handler_url:
        logger.info(
            "Using legacy task handler URL env var.",
            extra={"env": LEGACY_TASK_HANDLER_URL_ENV},
        )
        return legacy_handler_url

    return _DEFAULT_TASK_HANDLER_URL


class BuildiumProcessorError(RuntimeError):
    """Raised when a Buildium webhook cannot be dispatched for processing."""


@dataclass(frozen=True)
class BuildiumProcessingContext:
    """Supporting context prepared for webhook processing."""

    api_headers: Mapping[str, str]
    gl_mapping: Mapping[str, Any]


def _coerce_string(value: Any) -> Optional[str]:
    if value is None:
        return None
    if isinstance(value, str):
        return value
    try:
        return str(value)
    except Exception:  # pragma: no cover - defensive
        return None


def _coerce_int(value: Any) -> Optional[int]:
    if value is None:
        return None
    if isinstance(value, bool):  # pragma: no cover - defensive guard
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str):
        candidate = value.strip()
        if not candidate:
            return None
        try:
            return int(candidate)
        except ValueError:
            return None
    return None


def _parse_secret_payload(secret_payload: str) -> Optional[Mapping[str, Any]]:
    payload = secret_payload.strip()
    if not payload:
        return None
    try:
        decoded = json.loads(payload)
    except json.JSONDecodeError:
        return None
    return decoded if isinstance(decoded, Mapping) else None


def _extract_from_candidates(
    data: Mapping[str, Any],
    candidates: Sequence[str],
) -> Optional[str]:
    for candidate in candidates:
        if candidate in data:
            value = _coerce_string(data[candidate])
            if value:
                return value
    return None


def _prepare_buildium_headers(verified_webhook: "VerifiedBuildiumWebhook") -> Dict[str, str]:
    """Build Buildium API headers from the stored account context.

    Parses the secret payload to prefer bearer tokens, with fallbacks for
    API keys or basic authentication credentials when necessary.
    """
    headers: Dict[str, str] = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Buildium-Account-Id": verified_webhook.account_id,
    }

    secret_payload = verified_webhook.account_context.api_secret or ""
    parsed_secret = _parse_secret_payload(secret_payload)

    if parsed_secret:
        bearer_token = _extract_from_candidates(
            parsed_secret,
            ("access_token", "token", "bearer_token", "bearerToken"),
        )
        if bearer_token:
            headers["Authorization"] = f"Bearer {bearer_token}".strip()

        api_key = _extract_from_candidates(parsed_secret, ("api_key", "apiKey"))
        if api_key:
            headers["X-Buildium-Api-Key"] = api_key

        client_id = _extract_from_candidates(parsed_secret, ("client_id", "clientId"))
        if client_id:
            headers["X-Buildium-Client-Id"] = client_id

        if "Authorization" not in headers:
            username = _extract_from_candidates(parsed_secret, ("username", "user"))
            password = _extract_from_candidates(parsed_secret, ("password", "pass"))
            if username and password:
                credentials = f"{username}:{password}".encode("utf-8")
                headers["Authorization"] = "Basic " + base64.b64encode(credentials).decode("ascii")
    else:
        token = secret_payload.strip()
        if token:
            headers["Authorization"] = f"Bearer {token}"

    return headers


def _coerce_gl_mapping(value: Any) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return dict(value)
    if isinstance(value, str):
        try:
            decoded = json.loads(value)
        except json.JSONDecodeError:
            logger.warning("Unable to parse GL mapping payload as JSON.")
            return {}
        if isinstance(decoded, Mapping):
            return dict(decoded)
    return {}


def _extract_gl_mapping(metadata: Mapping[str, Any]) -> Mapping[str, Any]:
    if not isinstance(metadata, Mapping):
        return {}

    for key in (
        "gl_mapping",
        "glMapping",
        "gl_mappings",
        "glMappings",
        "general_ledger_mapping",
        "generalLedgerMapping",
    ):
        if key in metadata:
            mapping = _coerce_gl_mapping(metadata[key])
            if mapping:
                return mapping
    return {}


def _resolve_project_id() -> Optional[str]:
    for env_name in _PROJECT_ID_ENV_CANDIDATES:
        value = os.getenv(env_name)
        if value:
            return value
    default_project_id = DEFAULT_GCP_PROJECT_ID.strip()
    return default_project_id or None


def _serialize_verified_webhook(verified_webhook: "VerifiedBuildiumWebhook") -> Dict[str, Any]:
    headers: Mapping[str, Any]
    if isinstance(verified_webhook.envelope.headers, Mapping):
        headers = {str(key): str(value) for key, value in verified_webhook.envelope.headers.items()}
    else:  # pragma: no cover - defensive guard
        headers = {}

    body_bytes = verified_webhook.envelope.body or b""
    body_encoded = base64.b64encode(body_bytes).decode("ascii") if body_bytes else ""

    parsed_body = verified_webhook.envelope.parsed_body

    return {
        "account_id": verified_webhook.account_id,
        "verification_scheme": verified_webhook.verification_scheme,
        "signature": verified_webhook.signature,
        "account_context": {
            "account_id": verified_webhook.account_context.account_id,
            "metadata": dict(verified_webhook.account_context.metadata),
            "api_secret": verified_webhook.account_context.api_secret,
            "webhook_secret": verified_webhook.account_context.webhook_secret,
        },
        "envelope": {
            "headers": headers,
            "body": body_encoded,
            "parsed_body": parsed_body,
        },
    }


class AutomationHandler(Protocol):
    def __call__(
        self,
        *,
        account_id: str,
        api_headers: Mapping[str, str],
        gl_mapping: Mapping[str, Any],
        webhook: Mapping[str, Any],
    ) -> None:
        """Handle a routed automation task."""


_AUTOMATED_TASKS_KEY = "automatedtasks"
_INITIATION_AUTOMATION_KEY = ("taskcreated", "ontarioautomationsinitiation")
_AUTOMATION_ROUTING_TABLE: Dict[Tuple[str, str], AutomationHandler] = {
    _INITIATION_AUTOMATION_KEY: handle_initiation_automation,
    ("taskcreated", "n1increase"): handle_n1_increase_automation,
    ("taskstatuschanged", "n1increase"): handle_n1_increase_automation,
}

_TASK_DATA_SOURCE_API = "api"
_TASK_DATA_SOURCE_WEBHOOK = "webhook"

_AUTOMATED_CATEGORY_METADATA_KEY = "automated_tasks_category_id"


def _normalize_identifier(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    normalized = "".join(ch for ch in value.lower() if ch.isalnum())
    return normalized or None


def _extract_event_type(webhook: Mapping[str, Any]) -> Optional[str]:
    for key in ("eventType", "event_type", "type"):
        if key in webhook:
            event_type = _coerce_string(webhook[key])
            if event_type:
                return event_type
    event_block = webhook.get("event")
    if isinstance(event_block, Mapping):
        for key in ("eventType", "event_type", "type"):
            event_type = _coerce_string(event_block.get(key))
            if event_type:
                return event_type
    return None


def _extract_task_data(webhook: Mapping[str, Any]) -> Optional[Mapping[str, Any]]:
    for key in ("task", "Task", "resource", "Resource"):
        value = webhook.get(key)
        if isinstance(value, Mapping):
            return value
    return None


def _extract_task_identifier(webhook: Mapping[str, Any]) -> Optional[int]:
    candidates: List[Mapping[str, Any]] = [webhook]
    for key in ("task", "Task", "resource", "Resource", "event", "Event"):
        value = webhook.get(key)
        if isinstance(value, Mapping):
            candidates.append(value)

    id_keys = (
        "taskId",
        "task_id",
        "taskID",
        "id",
        "Id",
        "resourceId",
        "resource_id",
        "ResourceId",
        "ResourceID",
    )

    for candidate in candidates:
        for key in id_keys:
            if key in candidate:
                identifier = _coerce_int(candidate.get(key))
                if identifier is not None:
                    return identifier
    return None


def _extract_task_name(task_data: Mapping[str, Any]) -> Optional[str]:
    for key in ("taskName", "task_name", "name", "task", "title", "Title"):
        if key in task_data:
            task_name = _coerce_string(task_data[key])
            if task_name:
                return task_name
    return None


def _extract_task_category_name(task_data: Mapping[str, Any]) -> Optional[str]:
    for key in (
        "taskCategoryName",
        "task_category_name",
        "categoryName",
        "category",
        "Category",
    ):
        if key in task_data:
            category = task_data[key]
            if isinstance(category, Mapping):
                for nested_key in ("name", "taskCategoryName", "categoryName"):
                    nested_value = _coerce_string(category.get(nested_key))
                    if nested_value:
                        return nested_value
            else:
                category_name = _coerce_string(category)
                if category_name:
                    return category_name
    for key in ("taskCategory", "task_category"):
        category_block = task_data.get(key)
        if isinstance(category_block, Mapping):
            for nested_key in ("name", "taskCategoryName", "categoryName"):
                nested_value = _coerce_string(category_block.get(nested_key))
                if nested_value:
                    return nested_value
    return None


def _extract_task_category_identifier(task_data: Mapping[str, Any]) -> Optional[str]:
    identifier_keys = (
        "taskCategoryId",
        "task_category_id",
        "taskCategoryID",
        "task_categoryid",
        "taskcategoryid",
        "categoryId",
        "category_id",
        "CategoryId",
        "CategoryID",
    )

    def _normalize(value: Any) -> Optional[str]:
        identifier = _coerce_string(value)
        if isinstance(identifier, str):
            identifier = identifier.strip()
        return identifier or None

    for key in identifier_keys:
        if key in task_data:
            normalized = _normalize(task_data.get(key))
            if normalized:
                return normalized

    for key in ("taskCategory", "task_category", "Category", "category"):
        category_block = task_data.get(key)
        if not isinstance(category_block, Mapping):
            continue
        for nested_key in ("id", "Id", "ID", *identifier_keys):
            if nested_key in category_block:
                normalized = _normalize(category_block.get(nested_key))
                if normalized:
                    return normalized
    return None


def _coerce_task_mapping(task: Any) -> Optional[Mapping[str, Any]]:
    if isinstance(task, Mapping):
        return dict(task)

    for method_name in ("model_dump", "dict"):
        method = getattr(task, method_name, None)
        if callable(method):
            try:
                data = method(by_alias=True)
            except TypeError:
                data = method()
            if isinstance(data, Mapping):
                return dict(data)
    return None


def _build_tasks_api(api_headers: Mapping[str, Any]):
    _ensure_openapi_client_path()
    try:
        from openapi_client.api_client import ApiClient
        from openapi_client.api.tasks_api import TasksApi
        from openapi_client.configuration import Configuration
    except Exception:  # pragma: no cover - optional dependency safeguard
        logger.exception("Buildium Tasks API client is unavailable.")
        return None

    configuration = Configuration()
    api_client = ApiClient(configuration=configuration)
    for header_name, header_value in api_headers.items():
        coerced_name = _coerce_string(header_name)
        coerced_value = _coerce_string(header_value)
        if coerced_name and coerced_value:
            api_client.set_default_header(coerced_name, coerced_value)

    return TasksApi(api_client=api_client)


def _fetch_task_data(
    *,
    api_headers: Mapping[str, Any],
    metadata: Mapping[str, Any],
    task_identifier: Optional[int],
    webhook_payload: Mapping[str, Any],
) -> Tuple[Optional[Mapping[str, Any]], str]:
    fallback_data = _extract_task_data(webhook_payload)
    fallback_source = _TASK_DATA_SOURCE_WEBHOOK

    if task_identifier is None:
        if fallback_data is None:
            logger.debug(
                "No task identifier found in Buildium webhook payload.",
                extra={**metadata, "has_task_identifier": False},
            )
        return fallback_data, fallback_source

    tasks_api = _build_tasks_api(api_headers)
    if tasks_api is None:
        logger.warning(
            "Unable to initialize Buildium Tasks API client; using webhook payload data.",
            extra={**metadata, "task_id": task_identifier},
        )
        return fallback_data, fallback_source

    try:
        task = tasks_api.get_task_by_id(task_id=task_identifier)
    except Exception:
        logger.warning(
            "Failed to retrieve Buildium task details from API; using webhook payload data.",
            exc_info=True,
            extra={**metadata, "task_id": task_identifier},
        )
        return fallback_data, fallback_source

    task_data = _coerce_task_mapping(task)
    if not task_data:
        logger.warning(
            "Received empty Buildium task data from API; using webhook payload data.",
            extra={**metadata, "task_id": task_identifier},
        )
        return fallback_data, fallback_source

    return task_data, _TASK_DATA_SOURCE_API


def _select_automation_handler(
    *, event_type: Optional[str], task_name: Optional[str]
) -> Optional[AutomationHandler]:
    """Select the automation handler for a Buildium event/task pair.

    Normalizes identifiers to smooth out whitespace and punctuation
    differences.
    """
    event_key = _normalize_identifier(event_type)
    task_key = _normalize_identifier(task_name)
    if not event_key or not task_key:
        return None
    return _AUTOMATION_ROUTING_TABLE.get((event_key, task_key))


def _requires_automated_category(
    *, event_key: Optional[str], task_key: Optional[str]
) -> bool:
    """Determine whether the automation requires the automated task category."""

    if (event_key, task_key) == _INITIATION_AUTOMATION_KEY:
        return False
    return True


def _has_completed_initiation(*, account_id: str) -> bool:
    """Check Firestore for a flag that the initiation automation has executed."""

    try:
        from google.cloud import firestore  # type: ignore
    except Exception:  # pragma: no cover - optional dependency safeguard
        logger.debug(
            "Firestore client not available when checking initiation status.",
            extra={"account_id": account_id},
        )
        return False

    try:
        client = firestore.Client(database=BUILDUM_FIRESTORE_DATABASE)
        collection = client.collection(INITIATION_COLLECTION_PATH)
        document = collection.document(account_id)
        snapshot = document.get()
    except Exception:
        logger.warning(
            "Unable to determine Buildium initiation status from Firestore.",
            extra={"account_id": account_id},
        )
        return False

    if not getattr(snapshot, "exists", False):
        return False

    try:
        payload = snapshot.to_dict() or {}
    except Exception:
        logger.warning(
            "Unable to decode Buildium initiation Firestore document; assuming not completed.",
            extra={"account_id": account_id},
        )
        return False

    status = payload.get(INITIATION_COMPLETED_FIELD)
    return bool(status)


@dataclass
class BuildiumWebhookProcessor:
    """Prepare and execute a unit of Buildium webhook work."""

    verified_webhook: "VerifiedBuildiumWebhook"

    def __post_init__(self) -> None:
        self._processing_context = BuildiumProcessingContext(
            api_headers=_prepare_buildium_headers(self.verified_webhook),
            gl_mapping=_extract_gl_mapping(self.verified_webhook.account_context.metadata),
        )

    @property
    def processing_context(self) -> BuildiumProcessingContext:
        return self._processing_context

    @property
    def metadata(self) -> Mapping[str, Any]:
        parsed_body = self.verified_webhook.envelope.parsed_body
        event_id: Optional[str] = None
        event_type: Optional[str] = None
        if isinstance(parsed_body, Mapping):
            for key in ("id", "eventId", "event_id"):
                if key in parsed_body:
                    event_id = _coerce_string(parsed_body[key])
                    break
            for key in ("eventType", "event_type", "type"):
                if key in parsed_body:
                    event_type = _coerce_string(parsed_body[key])
                    break

        gl_mapping_keys = sorted(self._processing_context.gl_mapping.keys())
        metadata: Dict[str, Any] = {
            "account_id": self.verified_webhook.account_id,
            "verification_scheme": self.verified_webhook.verification_scheme,
            "gl_mapping_keys": gl_mapping_keys,
            "has_authorization_header": "Authorization" in self._processing_context.api_headers,
            "header_names": sorted(self._processing_context.api_headers.keys()),
        }
        if event_id:
            metadata["event_id"] = event_id
        if event_type:
            metadata["event_type"] = event_type
        return metadata

    async def run(self) -> None:
        try:
            await asyncio.to_thread(self._process)
        except asyncio.CancelledError:
            logger.info(
                "Buildium webhook processor task cancelled.",
                extra=self.metadata,
            )
            raise
        except Exception:
            logger.exception(
                "Unhandled exception while processing Buildium webhook.",
                extra=self.metadata,
            )
            raise

    def _process(self) -> None:
        payload = self._build_work_payload()
        logger.debug(
            "Prepared Buildium webhook work payload.",
            extra={
                **self.metadata,
                "payload_keys": sorted(payload.keys()),
            },
        )
        self._perform_work(payload)

    def _build_work_payload(self) -> Dict[str, Any]:
        payload: Dict[str, Any] = {
            "account_id": self.verified_webhook.account_id,
            "gl_mapping": dict(self._processing_context.gl_mapping),
        }
        parsed_body = self.verified_webhook.envelope.parsed_body
        if isinstance(parsed_body, Mapping):
            payload["webhook"] = dict(parsed_body)
        else:
            payload["webhook"] = self.verified_webhook.envelope.body.decode(
                "utf-8", errors="replace"
            ) if self.verified_webhook.envelope.body else None
        payload["api_headers"] = dict(self._processing_context.api_headers)
        return payload

    def _perform_work(self, payload: Mapping[str, Any]) -> None:
        """Filter for automation tasks and dispatch them to the registered handler.

        Ensures the payload is marked as automated before routing to a matched
        handler. Passes the prepared account headers and GL mapping to the
        handler.
        """
        metadata = dict(self.metadata)
        logger.info(
            "Dispatched Buildium webhook payload for downstream processing.",
            extra={
                **metadata,
                "payload_includes_gl_mapping": "gl_mapping" in payload,
            },
        )

        webhook_payload = payload.get("webhook")

        task_identifier: Optional[int] = None
        event_type: Optional[str] = None
        task_category_name: Optional[str] = None
        task_category_id: Optional[str] = None
        configured_category_id: Optional[str] = None

        account_metadata = self.verified_webhook.account_context.metadata
        if isinstance(account_metadata, Mapping):
            configured_category_id = _coerce_string(
                account_metadata.get(_AUTOMATED_CATEGORY_METADATA_KEY)
            )
            if isinstance(configured_category_id, str):
                configured_category_id = configured_category_id.strip() or None

        def _log_extra(**kwargs: Any) -> Dict[str, Any]:
            return {
                **metadata,
                "task_identifier": task_identifier,
                "event_type": event_type,
                "task_category_name": task_category_name,
                "configured_category_id": configured_category_id,
                **kwargs,
            }

        if not isinstance(webhook_payload, Mapping):
            logger.info(
                "Skipping Buildium webhook without structured task payload.",
                extra=_log_extra(has_webhook_mapping=False),
            )
            return

        webhook_payload = dict(webhook_payload)

        raw_api_headers = payload.get("api_headers")
        if isinstance(raw_api_headers, Mapping):
            api_headers = dict(raw_api_headers)
        else:
            api_headers = dict(self._processing_context.api_headers)

        task_identifier = _extract_task_identifier(webhook_payload)
        event_type = _extract_event_type(webhook_payload)
        task_data, task_data_source = _fetch_task_data(
            api_headers=api_headers,
            metadata=metadata,
            task_identifier=task_identifier,
            webhook_payload=webhook_payload,
        )
        if task_data is None:
            logger.info(
                "No task details available in Buildium webhook payload.",
                extra=_log_extra(has_task_data=False),
            )
            return

        webhook_payload["task"] = dict(task_data)

        task_name = _extract_task_name(task_data)
        task_category_name = _extract_task_category_name(task_data)
        task_category_id = _extract_task_category_identifier(task_data)

        logger.info(
            "Resolved Buildium task details for automation processing.",
            extra=_log_extra(
                task_data_source=task_data_source,
                task_name=task_name,
                task_category_id=task_category_id,
            ),
        )

        event_key = _normalize_identifier(event_type)
        task_key = _normalize_identifier(task_name)
        handler = _select_automation_handler(event_type=event_type, task_name=task_name)
        if handler is None:
            logger.info(
                "No automation handler registered for Buildium task payload.",
                extra={
                    **metadata,
                    "event_type": event_type,
                    "task_name": task_name,
                },
            )
            return

        requires_automated_category = _requires_automated_category(
            event_key=event_key, task_key=task_key
        )
        category_key = _normalize_identifier(task_category_name)
        if requires_automated_category and (category_key != _AUTOMATED_TASKS_KEY):
            logger.info(
                "Ignoring non-automated Buildium task payload.",
                extra=_log_extra(
                    requires_automated_category=requires_automated_category,
                    task_category_key=category_key,
                ),
            )
            return

        account_id = _coerce_string(payload.get("account_id")) or self.verified_webhook.account_id

        raw_gl_mapping = payload.get("gl_mapping")
        gl_mapping: Mapping[str, Any] = dict(raw_gl_mapping) if isinstance(raw_gl_mapping, Mapping) else {}

        if requires_automated_category:
            if not configured_category_id:
                logger.warning(
                    "Skipping Buildium automation without configured task category identifier.",
                    extra=_log_extra(
                        task_category_id=task_category_id,
                        configured_task_category_id=configured_category_id,
                    ),
                )
                return
            if not task_category_id:
                logger.info(
                    "Skipping Buildium automation without task category identifier.",
                    extra=_log_extra(
                        configured_task_category_id=configured_category_id,
                    ),
                )
                return
            if task_category_id != configured_category_id:
                logger.warning(
                    "Ignoring Buildium task with mismatched automation category identifier.",
                    extra=_log_extra(
                        task_category_id=task_category_id,
                        configured_task_category_id=configured_category_id,
                    ),
                )
                return

        if (event_key, task_key) == _INITIATION_AUTOMATION_KEY and _has_completed_initiation(
            account_id=account_id
        ):
            logger.info(
                "Skipping Buildium initiation automation; workflow already completed.",
                extra={**metadata, "account_id": account_id},
            )
            return

        logger.info(
            "Dispatching Buildium automation task to handler.",
            extra={
                **metadata,
                "event_type": event_type,
                "task_name": task_name,
                "task_category_name": task_category_name,
                "handler_name": getattr(handler, "__name__", str(handler)),
            },
        )

        handler(
            account_id=account_id,
            api_headers=api_headers,
            gl_mapping=gl_mapping,
            webhook=webhook_payload,
        )


def enqueue_buildium_webhook(
    verified_webhook: "VerifiedBuildiumWebhook",
    *,
    client: Optional[tasks_v2.CloudTasksClient] = None,
) -> Any:
    """Enqueue the verified webhook for processing via Cloud Tasks.

    Reads the environment-driven queue, location, and handler URL before posting
    the serialized webhook to Cloud Tasks. Raises a ``BuildiumProcessorError``
    when required settings are missing.
    """

    queue_name = _get_cloud_tasks_queue().strip()
    location = _get_cloud_tasks_location().strip()
    handler_url = _get_task_handler_url().strip()
    project_id = _resolve_project_id()

    metadata: Dict[str, Any] = {
        "account_id": verified_webhook.account_id,
        "queue": queue_name or _DEFAULT_CLOUD_TASKS_QUEUE,
        "location": location or _DEFAULT_CLOUD_TASKS_LOCATION,
    }

    if not project_id:
        message = "Google Cloud project identifier is not configured."
        logger.error(message, extra=metadata)
        raise BuildiumProcessorError(message)

    if not queue_name:
        message = "Cloud Tasks queue name is not configured."
        logger.error(message, extra=metadata)
        raise BuildiumProcessorError(message)

    if not location:
        message = "Cloud Tasks location is not configured."
        logger.error(message, extra=metadata)
        raise BuildiumProcessorError(message)

    if not handler_url:
        message = "Task handler URL is not configured."
        logger.error(message, extra=metadata)
        raise BuildiumProcessorError(message)

    if client is None:
        client = tasks_v2.CloudTasksClient()

    try:
        parent = client.queue_path(project_id, location, queue_name)
    except Exception as exc:
        message = "Unable to resolve Cloud Tasks queue path."
        logger.exception(message, extra=metadata)
        raise BuildiumProcessorError(message) from exc

    serialized = _serialize_verified_webhook(verified_webhook)
    body = json.dumps(serialized, default=str).encode("utf-8")
    task: Dict[str, Any] = {
        "http_request": {
            "http_method": tasks_v2.HttpMethod.POST,
            "url": handler_url,
            "headers": {"Content-Type": "application/json"},
            "body": body,
        }
    }

    request = {"parent": parent, "task": task}

    try:
        response = client.create_task(request=request)
    except google_exceptions.NotFound as exc:
        message = (
            "Cloud Tasks queue does not exist. Create the queue or configure "
            "CLOUD_TASKS_QUEUE/CLOUD_TASKS_LOCATION to match an existing queue."
        )
        logger.exception(message, extra={**metadata, "queue_path": parent})
        raise BuildiumProcessorError(message) from exc
    except google_exceptions.GoogleAPICallError as exc:
        message = "Failed to enqueue Buildium webhook task via Cloud Tasks."
        logger.exception(message, extra={**metadata, "queue_path": parent})
        raise BuildiumProcessorError(message) from exc
    except Exception as exc:  # pragma: no cover - defensive guard
        message = "Unexpected error while enqueuing Buildium webhook task."
        logger.exception(message, extra={**metadata, "queue_path": parent})
        raise BuildiumProcessorError(message) from exc

    task_name = getattr(response, "name", None)
    logger.info(
        "Enqueued Buildium webhook task in Cloud Tasks.",
        extra={**metadata, "task_name": task_name, "queue_path": parent},
    )

    return response


__all__ = [
    "BuildiumProcessorError",
    "BuildiumProcessingContext",
    "BuildiumWebhookProcessor",
    "enqueue_buildium_webhook",
    "CLOUD_TASKS_QUEUE_ENV",
    "CLOUD_TASKS_LOCATION_ENV",
    "TASK_HANDLER_URL_ENV",
]
