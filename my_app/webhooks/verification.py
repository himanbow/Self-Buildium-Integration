"""Buildium webhook verification helpers."""

from __future__ import annotations

import asyncio
import base64
import functools
import hashlib
import hmac
import json
import logging
import time
from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional, Sequence, Tuple, TYPE_CHECKING

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


@dataclass(frozen=True)
class _SignatureMetadata:
    """Captured signature header details discovered during extraction."""

    header_value: str
    scheme: str
    timestamp: Optional[str] = None


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
_SIGNATURE_TIMESTAMP_HEADERS: Tuple[str, ...] = (
    "x-buildium-signature-timestamp",
    "x-buildium-request-timestamp",
    "x-buildium-timestamp",
    "x-buildium-webhook-timestamp",
)

_SIGNATURE_MAX_AGE_SECONDS = 300


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
) -> Optional[_SignatureMetadata]:
    normalized_headers = _normalize_headers(headers)

    timestamp = _lookup_header(normalized_headers, _SIGNATURE_TIMESTAMP_HEADERS)

    signature = _lookup_header(normalized_headers, _HMAC_SIGNATURE_HEADERS)
    if signature:
        return _SignatureMetadata(header_value=signature, scheme="hmac", timestamp=timestamp)

    signature = _lookup_header(normalized_headers, _TOKEN_SIGNATURE_HEADERS)
    if signature:
        return _SignatureMetadata(header_value=signature, scheme="token")

    return None


def _parse_signature_header(signature_header: str) -> Tuple[str, Optional[str], Optional[str], Mapping[str, str]]:
    """Parse a structured signature header into components.

    Returns the extracted signature, algorithm hint, timestamp (if embedded), and a
    mapping of any discovered structured key/value pairs.
    """

    header = signature_header.strip()
    if not header:
        return "", None, None, {}

    segments = [segment.strip() for segment in header.split(",") if segment.strip()]
    structured_pairs: Dict[str, str] = {}

    if any("=" in segment for segment in segments):
        for segment in segments:
            if "=" not in segment:
                continue
            key, value = segment.split("=", 1)
            structured_pairs[key.strip().lower()] = value.strip()

        signature = (
            structured_pairs.get("v1")
            or structured_pairs.get("sig")
            or structured_pairs.get("signature")
            or structured_pairs.get("s")
            or structured_pairs.get("sha256")
            or ""
        )
        timestamp = structured_pairs.get("t") or structured_pairs.get("timestamp")
        algorithm = structured_pairs.get("alg") or structured_pairs.get("algorithm")

        if not signature and len(structured_pairs) == 1:
            # Handle values like "sha256=<signature>" where the only key encodes the
            # algorithm name and the value is the signature payload.
            signature = next(iter(structured_pairs.values()))
            algorithm = next(iter(structured_pairs.keys()))

        return signature, algorithm, timestamp, structured_pairs

    if "=" in header:
        algorithm, signature = header.split("=", 1)
        return signature.strip(), algorithm.strip().lower(), None, {}

    return header, None, None, {}


def _verify_hmac_signature(
    *,
    signature_header: str,
    webhook_secret: str,
    body: bytes,
    account_id: str,
    timestamp: Optional[str] = None,
) -> str:
    if not webhook_secret:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Buildium account is missing a webhook verification secret.",
        )

    provided_signature = signature_header.strip()
    extracted_signature, algorithm, embedded_timestamp, _ = _parse_signature_header(provided_signature)
    if extracted_signature:
        provided_signature = extracted_signature

    candidate_timestamp = timestamp or embedded_timestamp

    if algorithm:
        normalized_algorithm = algorithm.lower()
        if normalized_algorithm not in {"sha256", "hmac-sha256", "hmac_sha256"}:
            logger.warning(
                "Unsupported Buildium webhook signature algorithm.",
                extra={"account_id": account_id, "algorithm": normalized_algorithm},
            )
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unsupported Buildium webhook signature algorithm.",
            )

    message_digests = [
        hmac.new(
            webhook_secret.encode("utf-8"),
            body,
            hashlib.sha256,
        ).digest()
    ]

    if candidate_timestamp:
        timestamp_value = candidate_timestamp.strip()
        if not timestamp_value:
            candidate_timestamp = None
        else:
            try:
                timestamp_int = int(timestamp_value)
            except ValueError:
                logger.warning(
                    "Buildium webhook signature timestamp is invalid.",
                    extra={"account_id": account_id, "timestamp": timestamp_value},
                )
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Buildium webhook signature timestamp is invalid.",
                )

            current_timestamp = int(time.time())
            drift = abs(current_timestamp - timestamp_int)
            if drift > _SIGNATURE_MAX_AGE_SECONDS:
                logger.warning(
                    "Buildium webhook signature timestamp is outside the tolerance window.",
                    extra={
                        "account_id": account_id,
                        "timestamp": timestamp_value,
                        "drift_seconds": drift,
                    },
                )
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Buildium webhook signature timestamp is outside the tolerance window.",
                )

            timestamp_bytes = f"{timestamp_int}.".encode("utf-8")
            message_digests.append(
                hmac.new(
                    webhook_secret.encode("utf-8"),
                    timestamp_bytes + body,
                    hashlib.sha256,
                ).digest()
            )

    expected_signatures = set()
    for digest in message_digests:
        hex_signature = digest.hex()
        base64_signature = base64.b64encode(digest).decode("ascii")
        base64_url_signature = base64.urlsafe_b64encode(digest).decode("ascii")

        expected_signatures.add(hex_signature)
        expected_signatures.add(base64_signature)
        expected_signatures.add(base64_signature.rstrip("="))
        expected_signatures.add(base64_url_signature)
        expected_signatures.add(base64_url_signature.rstrip("="))

    for expected_signature in expected_signatures:
        if expected_signature and hmac.compare_digest(provided_signature, expected_signature):
            return expected_signature

    logger.warning(
        "Buildium webhook signature verification failed.",
        extra={"account_id": account_id},
    )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Buildium webhook signature did not match.",
    )


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

    signature_metadata = _extract_signature(headers=envelope.headers)
    if not signature_metadata:
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

    if signature_metadata.scheme == "hmac":
        signature = _verify_hmac_signature(
            signature_header=signature_metadata.header_value,
            webhook_secret=account_context.webhook_secret,
            body=envelope.body,
            account_id=account_id,
            timestamp=signature_metadata.timestamp,
        )
    else:
        signature = _verify_token_signature(
            signature_header=signature_metadata.header_value,
            webhook_secret=account_context.webhook_secret,
            account_id=account_id,
        )

    logger.info(
        "Verified Buildium webhook signature.",
        extra={
            "account_id": account_id,
            "verification_scheme": signature_metadata.scheme,
        },
    )

    return VerifiedBuildiumWebhook(
        account_context=account_context,
        account_id=account_id,
        envelope=envelope,
        signature=signature,
        verification_scheme=signature_metadata.scheme,
    )


__all__ = ["VerifiedBuildiumWebhook", "verify_buildium_webhook"]
