"""Buildium webhook verification helpers."""

from __future__ import annotations

import asyncio
import functools
import hashlib
import hmac
import json
import logging
from dataclasses import dataclass
from typing import Any, Mapping, Optional, Sequence, Tuple, TYPE_CHECKING

from fastapi import HTTPException, status

from ..services.account_context import (
    BuildiumAccountContext,
    get_buildium_account_context,
)

if TYPE_CHECKING:  # pragma: no cover - imported for type checking only
    from .buildium_listener import BuildiumWebhookEnvelope


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class VerifiedBuildiumWebhook:
    """Container for a webhook that has passed signature verification."""

    account_context: BuildiumAccountContext
    account_id: str
    envelope: "BuildiumWebhookEnvelope"
    signature: str
    verification_scheme: str


_ACCOUNT_ID_HEADER_CANDIDATES: Tuple[str, ...] = (
    "x-buildium-account-id",
    "x-buildium-accountid",
    "x-account-id",
    "x-buildium-account",
)
_ACCOUNT_ID_BODY_CANDIDATES: Tuple[str, ...] = (
    "account_id",
    "accountId",
    "AccountId",
)
_HMAC_SIGNATURE_HEADERS: Tuple[str, ...] = (
    "x-buildium-hmac-sha256",
    "x-buildium-hmacsha256",
    "x-buildium-signature",
    "x-hub-signature-256",
    "x-hub-signature",
)
_TOKEN_SIGNATURE_HEADERS: Tuple[str, ...] = (
    "x-buildium-verification-secret",
    "x-buildium-verification-token",
    "x-buildium-webhook-token",
    "x-buildium-webhook-secret",
)


def _normalize_headers(headers: Mapping[str, str]) -> Mapping[str, str]:
    return {key.lower(): value for key, value in headers.items()}


def _lookup_header(headers: Mapping[str, str], candidates: Sequence[str]) -> Optional[str]:
    for candidate in candidates:
        value = headers.get(candidate)
        if value:
            return value
    return None


def _extract_account_id(
    *,
    headers: Mapping[str, str],
    parsed_body: Optional[Any],
    body: bytes,
) -> Optional[str]:
    normalized_headers = _normalize_headers(headers)
    header_account_id = _lookup_header(normalized_headers, _ACCOUNT_ID_HEADER_CANDIDATES)
    if header_account_id:
        return header_account_id.strip()

    if isinstance(parsed_body, Mapping):
        for key in _ACCOUNT_ID_BODY_CANDIDATES:
            value = parsed_body.get(key)
            if value:
                return str(value)
        account_block = parsed_body.get("account")
        if isinstance(account_block, Mapping):
            for key in _ACCOUNT_ID_BODY_CANDIDATES:
                value = account_block.get(key)
                if value:
                    return str(value)
    else:
        try:
            decoded = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            decoded = None
        if isinstance(decoded, Mapping):
            for key in _ACCOUNT_ID_BODY_CANDIDATES:
                value = decoded.get(key)
                if value:
                    return str(value)

    return None


def _extract_signature(
    *,
    headers: Mapping[str, str],
) -> Tuple[Optional[str], Optional[str]]:
    normalized_headers = _normalize_headers(headers)

    signature = _lookup_header(normalized_headers, _HMAC_SIGNATURE_HEADERS)
    if signature:
        return signature, "hmac"

    signature = _lookup_header(normalized_headers, _TOKEN_SIGNATURE_HEADERS)
    if signature:
        return signature, "token"

    return None, None


def _verify_hmac_signature(
    *,
    signature_header: str,
    webhook_secret: str,
    body: bytes,
    account_id: str,
) -> str:
    if not webhook_secret:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Buildium account is missing a webhook verification secret.",
        )

    provided_signature = signature_header.strip()
    algorithm = "sha256"
    if "=" in provided_signature:
        algorithm, provided_signature = [segment.strip() for segment in provided_signature.split("=", 1)]
        algorithm = algorithm.lower() or "sha256"

    if algorithm not in {"sha256", "hmac-sha256", "hmac_sha256"}:
        logger.warning(
            "Unsupported Buildium webhook signature algorithm.",
            extra={"account_id": account_id, "algorithm": algorithm},
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unsupported Buildium webhook signature algorithm.",
        )

    expected_signature = hmac.new(
        webhook_secret.encode("utf-8"),
        body,
        hashlib.sha256,
    ).hexdigest()

    if not hmac.compare_digest(provided_signature, expected_signature):
        logger.warning(
            "Buildium webhook signature verification failed.",
            extra={"account_id": account_id},
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Buildium webhook signature did not match.",
        )

    return expected_signature


def _verify_token_signature(
    *,
    signature_header: str,
    webhook_secret: str,
    account_id: str,
) -> str:
    if not webhook_secret:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Buildium account is missing a webhook verification secret.",
        )

    if signature_header.strip() != webhook_secret:
        logger.warning(
            "Buildium webhook token verification failed.",
            extra={"account_id": account_id},
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Buildium webhook verification token did not match.",
        )

    return webhook_secret


async def verify_buildium_webhook(
    envelope: "BuildiumWebhookEnvelope",
    *,
    firestore_client: Optional[Any] = None,
    secret_manager_client: Optional[Any] = None,
) -> VerifiedBuildiumWebhook:
    """Validate webhook authenticity and resolve the associated account context."""

    account_id = _extract_account_id(
        headers=envelope.headers,
        parsed_body=envelope.parsed_body,
        body=envelope.body,
    )
    if not account_id:
        logger.warning("Received Buildium webhook without an account identifier.")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Buildium webhook is missing the account identifier.",
        )

    signature_header, scheme = _extract_signature(headers=envelope.headers)
    if not signature_header or not scheme:
        logger.warning(
            "Received Buildium webhook without a verification signature.",
            extra={"account_id": account_id},
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Buildium webhook signature header is required.",
        )

    loop = asyncio.get_running_loop()
    resolver = functools.partial(
        get_buildium_account_context,
        account_id,
        firestore_client=firestore_client,
        secret_manager_client=secret_manager_client,
    )

    if firestore_client is None and secret_manager_client is None:
        account_context = await loop.run_in_executor(None, resolver)
    else:
        account_context = resolver()

    if scheme == "hmac":
        signature = _verify_hmac_signature(
            signature_header=signature_header,
            webhook_secret=account_context.webhook_secret,
            body=envelope.body,
            account_id=account_id,
        )
    else:
        signature = _verify_token_signature(
            signature_header=signature_header,
            webhook_secret=account_context.webhook_secret,
            account_id=account_id,
        )

    logger.info(
        "Verified Buildium webhook signature.",
        extra={
            "account_id": account_id,
            "verification_scheme": scheme,
        },
    )

    return VerifiedBuildiumWebhook(
        account_context=account_context,
        account_id=account_id,
        envelope=envelope,
        signature=signature,
        verification_scheme=scheme,
    )


__all__ = ["VerifiedBuildiumWebhook", "verify_buildium_webhook"]
