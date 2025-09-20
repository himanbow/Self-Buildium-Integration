"""Async Buildium webhook listener."""

from __future__ import annotations

import json
import logging
import multiprocessing
from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional

from fastapi import FastAPI, HTTPException, Request, Response, status
import uvicorn

from ..tasks.buildium_processor import (
    BuildiumProcessorError,
    enqueue_buildium_webhook,
)
from .verification import verify_buildium_webhook

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


def run(host: str = "0.0.0.0", port: int = 8080, workers: Optional[int] = None) -> None:
    """Launch the webhook listener with a concurrent Uvicorn server."""

    if workers is None:
        # Ensure at least two worker processes so multiple Buildium accounts can
        # deliver webhooks concurrently without blocking each other.
        workers = max(2, multiprocessing.cpu_count())

    uvicorn.run(app, host=host, port=port, workers=workers, log_level="info")


__all__ = ["app", "run", "BuildiumWebhookEnvelope"]
