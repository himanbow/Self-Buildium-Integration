"""Background processing for Buildium webhook payloads."""

from __future__ import annotations

import asyncio
import base64
import json
import logging
from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional, Sequence, Set, Tuple
from typing import Protocol

from ..webhooks.verification import VerifiedBuildiumWebhook
from .initiation import handle_initiation_automation
from .n1_increase import handle_n1_increase_automation

logger = logging.getLogger(__name__)


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


def _prepare_buildium_headers(verified_webhook: VerifiedBuildiumWebhook) -> Dict[str, str]:
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
_AUTOMATION_ROUTING_TABLE: Dict[Tuple[str, str], AutomationHandler] = {
    ("taskcreated", "initiation"): handle_initiation_automation,
    ("taskcreated", "n1increase"): handle_n1_increase_automation,
    ("taskstatuschanged", "n1increase"): handle_n1_increase_automation,
}


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


def _extract_task_name(task_data: Mapping[str, Any]) -> Optional[str]:
    for key in ("taskName", "task_name", "name", "task"):
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


def _select_automation_handler(
    *, event_type: Optional[str], task_name: Optional[str]
) -> Optional[AutomationHandler]:
    event_key = _normalize_identifier(event_type)
    task_key = _normalize_identifier(task_name)
    if not event_key or not task_key:
        return None
    return _AUTOMATION_ROUTING_TABLE.get((event_key, task_key))


@dataclass
class BuildiumWebhookProcessor:
    """Prepare and execute a unit of Buildium webhook work."""

    verified_webhook: VerifiedBuildiumWebhook

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
        logger.info(
            "Dispatched Buildium webhook payload for downstream processing.",
            extra={
                **self.metadata,
                "payload_includes_gl_mapping": "gl_mapping" in payload,
            },
        )

        webhook_payload = payload.get("webhook")
        if not isinstance(webhook_payload, Mapping):
            logger.debug(
                "Skipping Buildium webhook without structured task payload.",
                extra={**self.metadata, "has_webhook_mapping": False},
            )
            return

        task_data = _extract_task_data(webhook_payload)
        if task_data is None:
            logger.debug(
                "No task details available in Buildium webhook payload.",
                extra={**self.metadata, "has_task_data": False},
            )
            return

        task_category_name = _extract_task_category_name(task_data)
        if _normalize_identifier(task_category_name) != _AUTOMATED_TASKS_KEY:
            logger.debug(
                "Ignoring non-automated Buildium task payload.",
                extra={
                    **self.metadata,
                    "task_category_name": task_category_name,
                },
            )
            return

        event_type = _extract_event_type(webhook_payload)
        task_name = _extract_task_name(task_data)
        handler = _select_automation_handler(event_type=event_type, task_name=task_name)
        if handler is None:
            logger.info(
                "No automation handler registered for Buildium task payload.",
                extra={
                    **self.metadata,
                    "event_type": event_type,
                    "task_name": task_name,
                },
            )
            return

        account_id = _coerce_string(payload.get("account_id")) or self.verified_webhook.account_id
        raw_api_headers = payload.get("api_headers")
        if isinstance(raw_api_headers, Mapping):
            api_headers = dict(raw_api_headers)
        else:
            api_headers = dict(self._processing_context.api_headers)

        raw_gl_mapping = payload.get("gl_mapping")
        gl_mapping: Mapping[str, Any] = dict(raw_gl_mapping) if isinstance(raw_gl_mapping, Mapping) else {}

        logger.info(
            "Dispatching Buildium automation task to handler.",
            extra={
                **self.metadata,
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


_inflight_tasks: Set[asyncio.Task[None]] = set()


def _on_task_done(task: asyncio.Task[None], *, metadata: Mapping[str, Any]) -> None:
    _inflight_tasks.discard(task)
    try:
        task.result()
    except asyncio.CancelledError:
        logger.info("Buildium webhook processor task cancelled after dispatch.", extra=metadata)
    except Exception:
        logger.exception("Buildium webhook processor task failed.", extra=metadata)


def enqueue_buildium_webhook(
    verified_webhook: VerifiedBuildiumWebhook,
    *,
    loop: Optional[asyncio.AbstractEventLoop] = None,
) -> asyncio.Task[None]:
    """Schedule asynchronous processing for the verified webhook payload."""

    if loop is None:
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError as exc:  # pragma: no cover - defensive
            raise BuildiumProcessorError("No running event loop is available.") from exc

    processor = BuildiumWebhookProcessor(verified_webhook)
    task = loop.create_task(processor.run())
    task.set_name(f"buildium-webhook-{verified_webhook.account_id}")
    _inflight_tasks.add(task)
    task.add_done_callback(lambda t, metadata=processor.metadata: _on_task_done(t, metadata=metadata))
    logger.info(
        "Enqueued Buildium webhook processor task.",
        extra={**processor.metadata, "inflight_processors": len(_inflight_tasks)},
    )
    return task


__all__ = [
    "BuildiumProcessorError",
    "BuildiumProcessingContext",
    "BuildiumWebhookProcessor",
    "enqueue_buildium_webhook",
]
