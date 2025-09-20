"""Cloud Run job entrypoint for rerunning Buildium automations."""

from __future__ import annotations

import argparse
import logging
from types import SimpleNamespace
from typing import Any, Callable, Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence

from fastapi import HTTPException

from ..services.account_context import BuildiumAccountContext, get_buildium_account_context
from ..tasks import initiation as initiation_tasks
from ..tasks.buildium_processor import BuildiumProcessingContext, BuildiumWebhookProcessor
from ..tasks.initiation import handle_initiation_automation
from ..tasks.n1_increase import handle_n1_increase_automation
from ..webhooks.verification import VerifiedBuildiumWebhook

try:  # pragma: no cover - optional dependency guard
    from google.cloud import firestore, secretmanager
except ImportError:  # pragma: no cover - optional dependency guard
    firestore = None  # type: ignore
    secretmanager = None  # type: ignore


logger = logging.getLogger(__name__)


AutomationHandler = Callable[..., None]
EventBuilder = Callable[[Optional[str]], Mapping[str, Any]]


def _initiation_task_created(_: Optional[str] = None) -> Mapping[str, Any]:
    return {
        "eventType": "TaskCreated",
        "task": {
            "taskName": "Initiation",
            "taskCategoryName": initiation_tasks.AUTOMATED_TASK_CATEGORY_NAME,
        },
    }


def _n1_task_created(_: Optional[str] = None) -> Mapping[str, Any]:
    return {
        "eventType": "TaskCreated",
        "task": {
            "taskName": "N1 Increase",
            "taskCategoryName": initiation_tasks.AUTOMATED_TASK_CATEGORY_NAME,
        },
    }


def _n1_task_status_changed(status: Optional[str]) -> Mapping[str, Any]:
    normalized = (status or "Completed").strip() or "Completed"
    return {
        "eventType": "TaskStatusChanged",
        "task": {
            "taskName": "N1 Increase",
            "taskCategoryName": initiation_tasks.AUTOMATED_TASK_CATEGORY_NAME,
            "status": normalized,
        },
        "changes": {"status": {"newValue": normalized}},
    }


_AUTOMATION_REGISTRY: Dict[str, Dict[str, Any]] = {
    "initiation": {
        "handler": handle_initiation_automation,
        "event_builders": {"taskcreated": _initiation_task_created},
        "requires_firestore": True,
    },
    "n1increase": {
        "handler": handle_n1_increase_automation,
        "event_builders": {
            "taskcreated": _n1_task_created,
            "taskstatuschanged": _n1_task_status_changed,
        },
        "requires_firestore": True,
    },
}


FIRESTORE_COLLECTION_PATH = initiation_tasks.FIRESTORE_COLLECTION_PATH


def _unique(sequence: Iterable[str]) -> List[str]:
    seen: MutableMapping[str, None] = {}
    result: List[str] = []
    for item in sequence:
        value = item.strip()
        if not value or value in seen:
            continue
        seen[value] = None
        result.append(value)
    return result


def _build_processing_context(account_context: BuildiumAccountContext) -> BuildiumProcessingContext:
    envelope = SimpleNamespace(headers={}, body=b"", parsed_body=None)
    verified = VerifiedBuildiumWebhook(
        account_context=account_context,
        account_id=account_context.account_id,
        envelope=envelope,
        signature="job-replay",
        verification_scheme="job",
    )
    processor = BuildiumWebhookProcessor(verified)
    return processor.processing_context


def _fetch_all_account_ids(firestore_client: Any) -> List[str]:
    try:
        collection = firestore_client.collection(FIRESTORE_COLLECTION_PATH)
    except Exception:  # pragma: no cover - defensive
        logger.exception(
            "Unable to access Buildium account collection in Firestore.",
            extra={"collection_path": FIRESTORE_COLLECTION_PATH},
        )
        raise

    account_ids: List[str] = []
    try:
        for snapshot in collection.stream():
            doc_id = getattr(snapshot, "id", None)
            if not doc_id and hasattr(snapshot, "reference"):
                doc_id = getattr(snapshot.reference, "id", None)
            if doc_id:
                account_ids.append(str(doc_id))
            else:
                logger.warning(
                    "Encountered Firestore document without identifier; skipping.",
                    extra={"collection_path": FIRESTORE_COLLECTION_PATH},
                )
    except Exception:  # pragma: no cover - defensive
        logger.exception(
            "Failed to enumerate Buildium accounts from Firestore.",
            extra={"collection_path": FIRESTORE_COLLECTION_PATH},
        )
        raise

    return account_ids


def run_job(
    *,
    account_ids: Sequence[str],
    automations: Optional[Sequence[str]] = None,
    event_type: str = "taskcreated",
    status: Optional[str] = None,
    firestore_client: Any,
    secret_manager_client: Any,
) -> int:
    selected_automations = (
        _unique(automations) if automations else list(_AUTOMATION_REGISTRY.keys())
    )
    normalized_event = event_type.strip().lower()
    normalized_status = status.strip() if isinstance(status, str) else None
    if normalized_event == "taskstatuschanged" and not normalized_status:
        normalized_status = "Completed"

    processed = 0
    for account_id in _unique(account_ids):
        try:
            account_context = get_buildium_account_context(
                account_id,
                firestore_client=firestore_client,
                secret_manager_client=secret_manager_client,
            )
        except HTTPException as exc:
            logger.warning(
                "Skipping Buildium account due to configuration error.",
                extra={"account_id": account_id, "status_code": exc.status_code},
            )
            continue
        except Exception:
            logger.exception(
                "Unexpected failure while loading Buildium account context.",
                extra={"account_id": account_id},
            )
            continue

        processing_context = _build_processing_context(account_context)
        for automation in selected_automations:
            config = _AUTOMATION_REGISTRY.get(automation)
            if not config:
                logger.warning(
                    "Skipping unknown Buildium automation.",
                    extra={"account_id": account_id, "automation": automation},
                )
                continue

            event_builders: Dict[str, EventBuilder] = config["event_builders"]
            builder = event_builders.get(normalized_event)
            if builder is None:
                logger.info(
                    "Automation does not handle requested event type; skipping.",
                    extra={
                        "account_id": account_id,
                        "automation": automation,
                        "event_type": normalized_event,
                    },
                )
                continue

            webhook_payload = builder(normalized_status)
            handler: AutomationHandler = config["handler"]
            handler_kwargs: Dict[str, Any] = {
                "account_id": account_id,
                "api_headers": dict(processing_context.api_headers),
                "gl_mapping": dict(processing_context.gl_mapping),
                "webhook": webhook_payload,
            }
            if config.get("requires_firestore"):
                handler_kwargs["firestore_client"] = firestore_client

            logger.info(
                "Dispatching Buildium automation handler.",
                extra={
                    "account_id": account_id,
                    "automation": automation,
                    "event_type": normalized_event,
                },
            )

            try:
                handler(**handler_kwargs)
                processed += 1
            except Exception:
                logger.exception(
                    "Automation handler raised an exception.",
                    extra={
                        "account_id": account_id,
                        "automation": automation,
                        "event_type": normalized_event,
                    },
                )

    return processed


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Run Buildium automation handlers for one or more accounts. "
            "Use this entrypoint when configuring the Cloud Run job."
        )
    )
    parser.add_argument(
        "--account",
        dest="accounts",
        action="append",
        default=[],
        help="Buildium account identifier to process. Provide multiple times to target several accounts.",
    )
    parser.add_argument(
        "--all-accounts",
        action="store_true",
        help="Process every Buildium account document found in Firestore.",
    )
    parser.add_argument(
        "--automation",
        dest="automations",
        action="append",
        choices=sorted(_AUTOMATION_REGISTRY.keys()),
        help="Automation to execute (default: all registered automations).",
    )
    parser.add_argument(
        "--event",
        default="taskcreated",
        choices=["taskcreated", "taskstatuschanged"],
        help="Buildium webhook event type to emulate (default: taskcreated).",
    )
    parser.add_argument(
        "--status",
        help="Task status to include when emulating taskstatuschanged events.",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Python logging level to use for job output (default: INFO).",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    logging.basicConfig(level=getattr(logging, args.log_level.upper(), logging.INFO))

    account_ids: List[str] = list(args.accounts)

    if firestore is None or secretmanager is None:  # pragma: no cover - dependency guard
        parser.error("google-cloud-firestore and google-cloud-secret-manager must be installed.")

    firestore_client = firestore.Client()
    secret_manager_client = secretmanager.SecretManagerServiceClient()

    if args.all_accounts:
        discovered = _fetch_all_account_ids(firestore_client)
        account_ids.extend(discovered)
        logger.info(
            "Discovered Buildium accounts from Firestore.",
            extra={"count": len(discovered)},
        )

    account_ids = _unique(account_ids)
    if not account_ids:
        parser.error("No Buildium accounts were provided or discovered.")

    processed = run_job(
        account_ids=account_ids,
        automations=args.automations,
        event_type=args.event,
        status=args.status,
        firestore_client=firestore_client,
        secret_manager_client=secret_manager_client,
    )

    logger.info(
        "Completed Buildium automation job.",
        extra={"accounts": len(account_ids), "handlers_invoked": processed},
    )

    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())


__all__ = ["main", "run_job", "FIRESTORE_COLLECTION_PATH"]
