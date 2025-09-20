"""Async Buildium webhook listener."""

from __future__ import annotations

import base64
import json
import logging
import multiprocessing
from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional

from fastapi import FastAPI, HTTPException, Request, Response, status
import uvicorn

from ..tasks.buildium_processor import (
    BuildiumProcessorError,
    BuildiumWebhookProcessor,
    enqueue_buildium_webhook,
)
from ..services.account_context import BuildiumAccountContext
from .verification import VerifiedBuildiumWebhook, verify_buildium_webhook

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Buildium Webhook Listener",
    description=(
        "Webhook endpoint that accepts Buildium webhook notifications and "
        "queues them for asynchronous processing."
    ),
)


@dataclass(frozen=True)
class BuildiumWebhookEnvelope:
    """Container for the raw webhook request."""

    headers: Mapping[str, str]
    body: bytes
    parsed_body: Optional[Any]


def _extract_metadata(
    headers: Mapping[str, str],
    parsed_body: Optional[Any],
    body: bytes,
) -> Dict[str, Any]:
    """Capture lightweight metadata useful for audit logging."""

    metadata: Dict[str, Any] = {
        "content_type": headers.get("content-type"),
        "content_length": headers.get("content-length"),
        "user_agent": headers.get("user-agent"),
        "payload_bytes": len(body),
    }

    if isinstance(parsed_body, Mapping):
        for key in ("eventType", "event_type"):
            if key in parsed_body:
                metadata["event_type"] = parsed_body[key]
                break
        for key in ("resourceType", "resource_type"):
            if key in parsed_body:
                metadata["resource_type"] = parsed_body[key]
                break
        for key in ("id", "eventId", "event_id"):
            if key in parsed_body:
                metadata["event_id"] = parsed_body[key]
                break

    return metadata


def _deserialize_verified_webhook_task(payload: Mapping[str, Any]) -> VerifiedBuildiumWebhook:
    if not isinstance(payload, Mapping):
        raise ValueError("Task payload must be a JSON object.")

    raw_account_id = payload.get("account_id")
    if not isinstance(raw_account_id, str) or not raw_account_id.strip():
        raise ValueError("Task payload is missing the Buildium account identifier.")
    account_id = raw_account_id.strip()

    account_context_payload = payload.get("account_context")
    if not isinstance(account_context_payload, Mapping):
        raise ValueError("Task payload is missing the account context block.")

    metadata_block = account_context_payload.get("metadata")
    metadata = dict(metadata_block) if isinstance(metadata_block, Mapping) else {}

    account_context = BuildiumAccountContext(
        account_id=str(account_context_payload.get("account_id") or account_id),
        metadata=metadata,
        api_secret=str(account_context_payload.get("api_secret") or ""),
        webhook_secret=str(account_context_payload.get("webhook_secret") or ""),
    )

    envelope_payload = payload.get("envelope")
    if not isinstance(envelope_payload, Mapping):
        raise ValueError("Task payload is missing the webhook envelope block.")

    headers_block = envelope_payload.get("headers")
    headers = (
        {str(key): str(value) for key, value in headers_block.items()}
        if isinstance(headers_block, Mapping)
        else {}
    )

    body_encoded = envelope_payload.get("body") or ""
    if body_encoded:
        try:
            body = base64.b64decode(body_encoded.encode("ascii"))
        except (ValueError, UnicodeDecodeError) as exc:
            raise ValueError("Task payload contains an invalid base64-encoded body.") from exc
    else:
        body = b""

    parsed_body = envelope_payload.get("parsed_body")

    envelope = BuildiumWebhookEnvelope(headers=headers, body=body, parsed_body=parsed_body)

    signature = payload.get("signature")
    verification_scheme = payload.get("verification_scheme")

    return VerifiedBuildiumWebhook(
        account_context=account_context,
        account_id=account_id,
        envelope=envelope,
        signature=str(signature) if signature is not None else "",
        verification_scheme=str(verification_scheme) if verification_scheme is not None else "",
    )


@app.post("/webhooks/buildium", status_code=status.HTTP_200_OK)
async def handle_buildium_webhook(request: Request) -> Response:
    """Receive a webhook call from Buildium, verify it, and enqueue processing."""

    raw_body = await request.body()
    parsed_body: Optional[Any]
    try:
        parsed_body = await request.json()
    except (json.JSONDecodeError, UnicodeDecodeError):
        parsed_body = None

    headers: Dict[str, str] = dict(request.headers)
    metadata = _extract_metadata(headers=headers, parsed_body=parsed_body, body=raw_body)
    logger.info("Received Buildium webhook", extra={"metadata": metadata})

    envelope = BuildiumWebhookEnvelope(headers=headers, body=raw_body, parsed_body=parsed_body)

    try:
        verified_webhook = await verify_buildium_webhook(envelope)
    except HTTPException as exc:
        logger.warning(
            "Rejected Buildium webhook during verification.",
            extra={"metadata": metadata, "status_code": exc.status_code},
        )
        raise
    except Exception as exc:  # pragma: no cover - defensive guard
        logger.exception(
            "Unexpected failure while verifying Buildium webhook payload.",
            extra={"metadata": metadata},
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to verify Buildium webhook payload.",
        ) from exc

    metadata.update(
        {
            "account_id": verified_webhook.account_id,
            "verification_scheme": verified_webhook.verification_scheme,
        }
    )

    logger.info("Verified Buildium webhook", extra={"metadata": metadata})

    try:
        enqueue_buildium_webhook(verified_webhook)
    except BuildiumProcessorError as exc:
        logger.error(
            "Failed to enqueue Buildium webhook for processing.",
            extra={"metadata": metadata},
        )
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Unable to queue Buildium webhook for processing.",
        ) from exc
    except Exception as exc:  # pragma: no cover - defensive guard
        logger.exception(
            "Unexpected error while scheduling Buildium webhook processing.",
            extra={"metadata": metadata},
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to queue Buildium webhook for processing.",
        ) from exc

    logger.info(
        "Buildium webhook dispatched for asynchronous processing.",
        extra={"metadata": metadata},
    )

    return Response(status_code=status.HTTP_200_OK)


@app.post("/tasks/buildium-webhook", status_code=status.HTTP_204_NO_CONTENT)
async def handle_buildium_webhook_task(request: Request) -> Response:
    """Execute queued Buildium webhook work from Cloud Tasks."""

    try:
        payload = await request.json()
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task payload must be valid JSON.",
        )

    try:
        verified_webhook = _deserialize_verified_webhook_task(payload)
    except ValueError as exc:
        logger.warning(
            "Rejected Buildium webhook task due to invalid payload.",
            extra={"error": str(exc)},
        )
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    except Exception as exc:  # pragma: no cover - defensive guard
        logger.exception("Failed to deserialize Buildium webhook task payload.")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task payload could not be parsed.",
        ) from exc

    processor = BuildiumWebhookProcessor(verified_webhook)

    logger.info(
        "Processing Buildium webhook task from Cloud Tasks.",
        extra=processor.metadata,
    )

    try:
        await processor.run()
    except Exception as exc:
        logger.exception(
            "Buildium webhook task processing failed.",
            extra=processor.metadata,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process Buildium webhook task.",
        ) from exc

    logger.info(
        "Completed Buildium webhook task from Cloud Tasks.",
        extra=processor.metadata,
    )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


def run(host: str = "0.0.0.0", port: int = 8080, workers: Optional[int] = None) -> None:
    """Launch the webhook listener with a concurrent Uvicorn server."""

    if workers is None:
        # Ensure at least two worker processes so multiple Buildium accounts can
        # deliver webhooks concurrently without blocking each other.
        workers = max(2, multiprocessing.cpu_count())

    uvicorn.run(app, host=host, port=port, workers=workers, log_level="info")


__all__ = [
    "app",
    "run",
    "BuildiumWebhookEnvelope",
    "handle_buildium_webhook",
    "handle_buildium_webhook_task",
]
