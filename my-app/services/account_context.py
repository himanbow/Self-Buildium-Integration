"""Utilities for resolving Buildium account context."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional

from fastapi import HTTPException, status
from google.api_core import exceptions as google_exceptions
from google.cloud import firestore, secretmanager

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class BuildiumAccountContext:
    """Container for account metadata and resolved secrets."""

    account_id: str
    metadata: Mapping[str, Any]
    api_secret: str
    webhook_secret: str


_FIRESTORE_COLLECTION_PATH = "Buildium/buildium_accounts"


def _access_secret(
    *,
    client: secretmanager.SecretManagerServiceClient,
    secret_name: str,
    account_id: str,
    secret_type: str,
) -> str:
    """Resolve a secret version and return its UTF-8 decoded payload."""

    if not secret_name:
        message = f"Missing {secret_type} secret reference for Buildium account."
        logger.error(
            message,
            extra={"account_id": account_id, "secret_type": secret_type},
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Buildium account configuration is incomplete.",
        )

    try:
        response = client.access_secret_version(request={"name": secret_name})
    except google_exceptions.NotFound as exc:
        message = "Referenced secret was not found in Google Secret Manager."
        logger.error(
            message,
            extra={
                "account_id": account_id,
                "secret_type": secret_type,
                "secret_name": secret_name,
            },
            exc_info=exc,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Buildium account configuration is invalid.",
        ) from exc
    except google_exceptions.GoogleAPICallError as exc:
        message = "Failed to access secret in Google Secret Manager."
        logger.exception(
            message,
            extra={
                "account_id": account_id,
                "secret_type": secret_type,
                "secret_name": secret_name,
            },
        )
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Unable to resolve Buildium account secrets.",
        ) from exc

    try:
        payload = response.payload.data.decode("utf-8")
    except UnicodeDecodeError as exc:
        logger.exception(
            "Secret payload for Buildium account is not valid UTF-8.",
            extra={
                "account_id": account_id,
                "secret_type": secret_type,
                "secret_name": secret_name,
            },
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Buildium account secret payload is invalid.",
        ) from exc
    if not payload:
        logger.warning(
            "Resolved secret payload is empty.",
            extra={
                "account_id": account_id,
                "secret_type": secret_type,
                "secret_name": secret_name,
            },
        )
    return payload


def get_buildium_account_context(
    account_id: str,
    *,
    firestore_client: Optional[firestore.Client] = None,
    secret_manager_client: Optional[secretmanager.SecretManagerServiceClient] = None,
) -> BuildiumAccountContext:
    """Fetch persisted Buildium account metadata and resolve associated secrets."""

    if not account_id:
        logger.error(
            "No Buildium account identifier was provided.",
            extra={"account_id": account_id},
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Buildium account id is required.",
        )

    if firestore_client is None:
        firestore_client = firestore.Client()
    if secret_manager_client is None:
        secret_manager_client = secretmanager.SecretManagerServiceClient()

    try:
        collection_ref = firestore_client.collection(_FIRESTORE_COLLECTION_PATH)
        doc_ref = collection_ref.document(account_id)
    except ValueError as exc:
        logger.exception(
            "Invalid Firestore path configuration for Buildium accounts.",
            extra={
                "account_id": account_id,
                "collection_path": _FIRESTORE_COLLECTION_PATH,
            },
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Buildium account storage path is misconfigured.",
        ) from exc

    document_path = doc_ref.path

    try:
        snapshot = doc_ref.get()
    except google_exceptions.NotFound as exc:
        message = "Buildium account document was not found in Firestore."
        logger.warning(
            message,
            extra={"account_id": account_id, "document_path": document_path},
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Buildium account was not found.",
        ) from exc
    except google_exceptions.GoogleAPICallError as exc:
        message = "Failed to load Buildium account document from Firestore."
        logger.exception(
            message,
            extra={"account_id": account_id, "document_path": document_path},
        )
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Unable to load Buildium account configuration.",
        ) from exc

    if not snapshot.exists:
        logger.warning(
            "Buildium account document does not exist.",
            extra={"account_id": account_id, "document_path": document_path},
        )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Buildium account was not found.",
        )

    metadata: Dict[str, Any] = snapshot.to_dict() or {}

    api_secret_name = (
        metadata.get("api_secret_name")
        or metadata.get("apiSecretName")
        or metadata.get("api_secret_version_name")
        or metadata.get("apiSecretVersionName")
    )
    webhook_secret_name = (
        metadata.get("webhook_secret_name")
        or metadata.get("webhookSecretName")
        or metadata.get("webhook_verification_secret_name")
        or metadata.get("webhookVerificationSecretName")
    )

    api_secret = _access_secret(
        client=secret_manager_client,
        secret_name=api_secret_name,
        account_id=account_id,
        secret_type="api_secret",
    )
    webhook_secret = _access_secret(
        client=secret_manager_client,
        secret_name=webhook_secret_name,
        account_id=account_id,
        secret_type="webhook_secret",
    )

    logger.info(
        "Resolved Buildium account context.",
        extra={
            "account_id": account_id,
            "document_path": document_path,
            "has_api_secret": bool(api_secret),
            "has_webhook_secret": bool(webhook_secret),
        },
    )

    return BuildiumAccountContext(
        account_id=account_id,
        metadata=metadata,
        api_secret=api_secret,
        webhook_secret=webhook_secret,
    )


__all__ = ["BuildiumAccountContext", "get_buildium_account_context"]
