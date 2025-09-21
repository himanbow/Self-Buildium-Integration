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

_SENSITIVE_HEADER_PREFIXES = ("authorization",)
_SENSITIVE_HEADER_KEYS = {
    "buildium-webhook-secret",
    "buildium-webhook-signature",
    "buildium-webhook-token",
    "x-buildium-hmac-sha256",
    "x-buildium-hmacsha256",
    "x-buildium-signature",
    "x-buildium-verification-secret",
    "x-buildium-verification-token",
    "x-buildium-webhook-token",
    "x-buildium-webhook-secret",
    "x-hub-signature",
    "x-hub-signature-256",
}
_BODY_PREVIEW_LIMIT = 2048


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

    header_name: str
    header_value: str
    scheme: str
    timestamp: Optional[str] = None
    timestamp_header_name: Optional[str] = None


_ACCOUNT_ID_HEADER_CANDIDATES: Tuple[str, ...] = (
    "buildium-account-id",
    "buildium-accountid",
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
    "buildium-webhook-signature",
    "x-buildium-hmac-sha256",
    "x-buildium-hmacsha256",
    "x-buildium-signature",
    "x-hub-signature-256",
    "x-hub-signature",
)
_TOKEN_SIGNATURE_HEADERS: Tuple[str, ...] = (
    "buildium-webhook-secret",
    "buildium-webhook-token",
    "x-buildium-verification-secret",
    "x-buildium-verification-token",
    "x-buildium-webhook-token",
    "x-buildium-webhook-secret",
)
_SIGNATURE_TIMESTAMP_HEADERS: Tuple[str, ...] = (
    "buildium-webhook-timestamp",
    "x-buildium-signature-timestamp",
    "x-buildium-request-timestamp",
    "x-buildium-timestamp",
    "x-buildium-webhook-timestamp",
)

_STRUCTURED_SIGNATURE_KEYS = {
    "v1",
    "sig",
    "signature",
    "s",
    "sha256",
    "t",
    "timestamp",
    "alg",
    "algorithm",
}

_SIGNATURE_MAX_AGE_SECONDS = 300


def _normalize_headers(headers: Mapping[str, str]) -> Mapping[str, str]:
    return {key.lower(): value for key, value in headers.items()}


def _summarize_headers_for_logging(headers: Mapping[str, str]) -> Dict[str, str]:
    sanitized: Dict[str, str] = {}
    for key, value in headers.items():
        normalized_key = key.lower()
        if normalized_key.startswith(_SENSITIVE_HEADER_PREFIXES) or normalized_key in _SENSITIVE_HEADER_KEYS:
            sanitized[normalized_key] = "<redacted>"
        else:
            sanitized[normalized_key] = value
    return sanitized


def _preview_body_for_logging(body: bytes, *, limit: int = _BODY_PREVIEW_LIMIT) -> str:
    if not body:
        return ""

    decoded = body.decode("utf-8", "replace")
    if len(decoded) <= limit:
        return decoded

    return f"{decoded[:limit]}… <truncated {len(decoded) - limit} characters>"


def _summarize_signature_metadata(metadata: _SignatureMetadata) -> Dict[str, Any]:
    return {
        "scheme": metadata.scheme,
        "header_name": metadata.header_name,
        "timestamp": metadata.timestamp,
        "timestamp_header_name": metadata.timestamp_header_name,
        "has_value": bool(metadata.header_value),
        "value_length": len(metadata.header_value or ""),
    }


def _lookup_header(
    headers: Mapping[str, str], candidates: Sequence[str]
) -> Tuple[Optional[str], Optional[str]]:
    for candidate in candidates:
        value = headers.get(candidate)
        if value:
            return value, candidate
    return None, None


def _extract_account_id(
    *,
    headers: Mapping[str, str],
    parsed_body: Optional[Any],
    body: bytes,
) -> Optional[str]:
    normalized_headers = _normalize_headers(headers)
    header_account_id, header_key = _lookup_header(
        normalized_headers, _ACCOUNT_ID_HEADER_CANDIDATES
    )
    if header_account_id:
        account_id = header_account_id.strip()
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(
                "Account identifier resolved from webhook headers.",
                extra={
                    "account_id_candidate": account_id,
                    "header_key": header_key,
                    "header_value_raw": header_account_id,
                    "headers_raw": dict(normalized_headers),
                },
            )
        return account_id

    if isinstance(parsed_body, Mapping):
        for key in _ACCOUNT_ID_BODY_CANDIDATES:
            value = parsed_body.get(key)
            if value:
                account_id = str(value)
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug(
                        "Account identifier resolved from webhook body field.",
                        extra={
                            "account_id_candidate": account_id,
                            "body_key": key,
                            "parsed_body": parsed_body,
                        },
                    )
                return account_id
        account_block = parsed_body.get("account")
        if isinstance(account_block, Mapping):
            for key in _ACCOUNT_ID_BODY_CANDIDATES:
                value = account_block.get(key)
                if value:
                    account_id = str(value)
                    if logger.isEnabledFor(logging.DEBUG):
                        logger.debug(
                            "Account identifier resolved from webhook account block.",
                            extra={
                                "account_id_candidate": account_id,
                                "account_block_key": key,
                                "account_block": account_block,
                            },
                        )
                    return account_id
    else:
        try:
            decoded = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            decoded = None
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(
                    "Failed to decode webhook body for account identifier lookup.",
                    extra={
                        "decode_error": str(exc),
                        "raw_body": body.decode("utf-8", "replace"),
                    },
                )
        if isinstance(decoded, Mapping):
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(
                    "Decoded webhook body for account identifier lookup.",
                    extra={"decoded_body": decoded},
                )
            for key in _ACCOUNT_ID_BODY_CANDIDATES:
                value = decoded.get(key)
                if value:
                    account_id = str(value)
                    if logger.isEnabledFor(logging.DEBUG):
                        logger.debug(
                            "Account identifier resolved from decoded body payload.",
                            extra={
                                "account_id_candidate": account_id,
                                "body_key": key,
                                "decoded_body": decoded,
                            },
                        )
                    return account_id
            account_block = decoded.get("account")
            if isinstance(account_block, Mapping):
                for key in _ACCOUNT_ID_BODY_CANDIDATES:
                    value = account_block.get(key)
                    if value:
                        account_id = str(value)
                        if logger.isEnabledFor(logging.DEBUG):
                            logger.debug(
                                "Account identifier resolved from decoded account block.",
                                extra={
                                    "account_id_candidate": account_id,
                                    "account_block_key": key,
                                    "account_block": account_block,
                                },
                            )
                        return account_id

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(
            "Failed to extract Buildium account identifier from webhook payload.",
            extra={
                "headers_raw": dict(normalized_headers),
                "body_raw": body.decode("utf-8", "replace"),
                "parsed_body": parsed_body,
            },
        )
    return None


def _extract_signature(
    *,
    headers: Mapping[str, str],
) -> Optional[_SignatureMetadata]:
    normalized_headers = _normalize_headers(headers)

    timestamp, timestamp_header_name = _lookup_header(
        normalized_headers, _SIGNATURE_TIMESTAMP_HEADERS
    )

    for candidate in _HMAC_SIGNATURE_HEADERS:
        signature = normalized_headers.get(candidate)
        if signature:
            return _SignatureMetadata(
                header_name=candidate,
                header_value=signature,
                scheme="hmac",
                timestamp=timestamp,
                timestamp_header_name=timestamp_header_name,
            )

    for candidate in _TOKEN_SIGNATURE_HEADERS:
        signature = normalized_headers.get(candidate)
        if signature:
            return _SignatureMetadata(
                header_name=candidate,
                header_value=signature,
                scheme="token",
                timestamp=timestamp,
                timestamp_header_name=timestamp_header_name,
            )

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
            normalized_key = key.strip().lower()
            if normalized_key not in _STRUCTURED_SIGNATURE_KEYS:
                continue
            structured_pairs[normalized_key] = value.strip()

        if structured_pairs:
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

    return header, None, None, {}


def _verify_hmac_signature(
    *,
    signature_header: str,
    webhook_secret: str,
    body: bytes,
    account_id: str,
    timestamp: Optional[str] = None,
) -> str:
    body_text_for_logging = body.decode("utf-8", "replace")

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(
            "Starting Buildium webhook HMAC verification.",
            extra={
                "account_id": account_id,
                "provided_signature_raw": signature_header,
                "webhook_secret": webhook_secret,
                "body_length": len(body),
                "body_raw": body_text_for_logging,
                "timestamp_header": timestamp,
            },
        )

    if not webhook_secret:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Buildium account is missing a webhook verification secret.",
        )

    provided_signature = signature_header.strip()
    (
        extracted_signature,
        algorithm,
        embedded_timestamp,
        structured_pairs,
    ) = _parse_signature_header(provided_signature)

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(
            "Parsed Buildium webhook signature header.",
            extra={
                "account_id": account_id,
                "provided_signature_stripped": provided_signature,
                "extracted_signature": extracted_signature,
                "algorithm_hint": algorithm,
                "embedded_timestamp": embedded_timestamp,
                "structured_signature_pairs": dict(structured_pairs),
                "timestamp_header": timestamp,
                "webhook_secret": webhook_secret,
            },
        )

    if extracted_signature:
        provided_signature = extracted_signature

    candidate_timestamp = timestamp or embedded_timestamp

    if algorithm:
        normalized_algorithm = algorithm.lower()
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(
                "Normalized Buildium webhook signature algorithm.",
                extra={
                    "account_id": account_id,
                    "algorithm_hint": algorithm,
                    "normalized_algorithm": normalized_algorithm,
                    "webhook_secret": webhook_secret,
                },
            )
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
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(
                "Evaluating Buildium webhook HMAC timestamp.",
                extra={
                    "account_id": account_id,
                    "candidate_timestamp": candidate_timestamp,
                    "header_timestamp": timestamp,
                    "embedded_timestamp": embedded_timestamp,
                    "webhook_secret": webhook_secret,
                },
            )
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
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(
                    "Generated timestamp-influenced HMAC digest candidate.",
                    extra={
                        "account_id": account_id,
                        "timestamp_int": timestamp_int,
                        "webhook_secret": webhook_secret,
                    },
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

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(
            "Computed expected Buildium webhook HMAC signatures.",
            extra={
                "account_id": account_id,
                "expected_signatures": sorted(expected_signatures),
                "message_digest_count": len(message_digests),
                "webhook_secret": webhook_secret,
            },
        )

    for expected_signature in expected_signatures:
        if expected_signature and hmac.compare_digest(provided_signature, expected_signature):
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(
                    "Buildium webhook HMAC signature matched expected digest.",
                    extra={
                        "account_id": account_id,
                        "provided_signature": provided_signature,
                        "matched_signature": expected_signature,
                        "expected_signatures": sorted(expected_signatures),
                        "webhook_secret": webhook_secret,
                    },
                )
            return expected_signature

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(
            "Buildium webhook HMAC signature mismatch.",
            extra={
                "account_id": account_id,
                "provided_signature": provided_signature,
                "expected_signatures": sorted(expected_signatures),
                "webhook_secret": webhook_secret,
                "body_raw": body_text_for_logging,
                "timestamp_header": timestamp,
                "embedded_timestamp": embedded_timestamp,
            },
        )

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
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(
            "Starting Buildium webhook token verification.",
            extra={
                "account_id": account_id,
                "provided_signature_raw": signature_header,
                "webhook_secret": webhook_secret,
            },
        )

    if not webhook_secret:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Buildium account is missing a webhook verification secret.",
        )

    if signature_header.strip() != webhook_secret:
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(
                "Buildium webhook token mismatch detected.",
                extra={
                    "account_id": account_id,
                    "provided_signature": signature_header.strip(),
                    "webhook_secret": webhook_secret,
                },
            )
        logger.warning(
            "Buildium webhook token verification failed.",
            extra={"account_id": account_id},
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Buildium webhook verification token did not match.",
        )

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(
            "Buildium webhook token verification succeeded.",
            extra={
                "account_id": account_id,
                "provided_signature": signature_header.strip(),
                "webhook_secret": webhook_secret,
            },
        )

    return webhook_secret


async def verify_buildium_webhook(
    envelope: "BuildiumWebhookEnvelope",
    *,
    firestore_client: Optional[Any] = None,
    secret_manager_client: Optional[Any] = None,
) -> VerifiedBuildiumWebhook:
    """Validate webhook authenticity and resolve the associated account context."""

    raw_headers_for_logging = {str(key): str(value) for key, value in envelope.headers.items()}
    body_raw_for_logging = envelope.body.decode("utf-8", "replace")
    headers_for_logging = _summarize_headers_for_logging(envelope.headers)
    body_preview_for_logging = _preview_body_for_logging(envelope.body)

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(
            "Starting Buildium webhook verification.",
            extra={
                "headers_raw": raw_headers_for_logging,
                "body_raw": body_raw_for_logging,
                "body_length": len(envelope.body or b""),
                "parsed_body": envelope.parsed_body,
                "parsed_body_type": type(envelope.parsed_body).__name__
                if envelope.parsed_body is not None
                else None,
            },
        )

    account_id = _extract_account_id(
        headers=envelope.headers,
        parsed_body=envelope.parsed_body,
        body=envelope.body,
    )
    if not account_id:
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(
                "Unable to resolve Buildium account from webhook payload.",
                extra={
                    "headers": headers_for_logging,
                    "body_preview": body_preview_for_logging,
                    "parsed_body_type": type(envelope.parsed_body).__name__
                    if envelope.parsed_body is not None
                    else None,
                },
            )

        logger.warning(
            "Received Buildium webhook without an account identifier.",
            extra={
                "headers": headers_for_logging,
            },
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Buildium webhook is missing the account identifier.",
        )

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(
            "Resolved Buildium account identifier from webhook payload.",
            extra={
                "account_id": account_id,
                "headers": headers_for_logging,
                "body_preview": body_preview_for_logging,
                "parsed_body_type": type(envelope.parsed_body).__name__
                if envelope.parsed_body is not None
                else None,
            },
        )

    signature_metadata = _extract_signature(headers=envelope.headers)
    if not signature_metadata:
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(
                "No Buildium webhook signature header found.",
                extra={
                    "account_id": account_id,
                    "headers_raw": raw_headers_for_logging,
                    "body_raw": body_raw_for_logging,
                },
            )
        logger.warning(
            "Received Buildium webhook without a verification signature.",
            extra={
                "account_id": account_id,
                "headers": headers_for_logging,
            },
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Buildium webhook signature header is required.",
        )

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(
            "Buildium webhook signature metadata captured.",
            extra={
                "account_id": account_id,
                "signature_details": _summarize_signature_metadata(signature_metadata),
                "signature_header_name": signature_metadata.header_name,
                "signature_header_value": signature_metadata.header_value,
                "signature_timestamp": signature_metadata.timestamp,
                "signature_timestamp_header": signature_metadata.timestamp_header_name,
            },
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

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(
            "Resolved Buildium account context for verification.",
            extra={
                "account_id": account_id,
                "account_context": {
                    "account_id": account_context.account_id,
                    "metadata": dict(account_context.metadata),
                    "api_secret": account_context.api_secret,
                    "webhook_secret": account_context.webhook_secret,
                },
            },
        )

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
            "signature_details": _summarize_signature_metadata(signature_metadata),
        },
    )

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(
            "Buildium webhook signature verification completed.",
            extra={
                "account_id": account_id,
                "verification_scheme": signature_metadata.scheme,
                "provided_signature": signature_metadata.header_value,
                "matched_signature": signature,
                "webhook_secret": account_context.webhook_secret,
                "signature_timestamp": signature_metadata.timestamp,
                "signature_timestamp_header": signature_metadata.timestamp_header_name,
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
