"""Utilities for resolving Buildium account context."""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, Mapping, Optional

import google.auth
from google.auth import exceptions as google_auth_exceptions
from fastapi import HTTPException, status

if TYPE_CHECKING:  # pragma: no cover - imported for static analysis only
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


_FIRESTORE_COLLECTION_PATH = "buildium_accounts"
_WEBHOOK_SECRET_METADATA_KEYS = (
    "webhook_secret",
    "webhookSecret",
    "webhook_verification_secret",
    "webhookVerificationSecret",
)
_WEBHOOK_SECRET_NAME_KEYS = (
    "webhook_secret_name",
    "webhookSecretName",
    "webhook_verification_secret_name",
    "webhookVerificationSecretName",
)

_SECRET_PROJECT_ENV_VAR = "SECRET_PROJECT_ID"


def _get_secret_project_id(*, account_id: str, secret_type: str) -> str:
    """Resolve the GCP project id that stores Buildium secrets."""

    project_id = os.getenv(_SECRET_PROJECT_ENV_VAR)
    if project_id:
        return project_id

    try:
        _, project_id = google.auth.default()
    except google_auth_exceptions.DefaultCredentialsError as exc:
        logger.error(
            "Unable to determine GCP project id for Buildium secret access.",
            extra={"account_id": account_id, "secret_type": secret_type},
            exc_info=exc,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Buildium secret storage project is not configured.",
        ) from exc

    if project_id:
        return project_id

    logger.error(
        "Google application default credentials do not specify a project id.",
        extra={"account_id": account_id, "secret_type": secret_type},
    )
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Buildium secret storage project is not configured.",
    )


def _normalize_secret_resource_name(
    secret_reference: str, *, account_id: str, secret_type: str
) -> str:
    """Ensure the provided secret reference is a full Secret Manager resource name."""

    secret_reference = secret_reference.strip()
    if secret_reference.startswith("projects/"):
        return secret_reference

    project_id = _get_secret_project_id(account_id=account_id, secret_type=secret_type)

    if "/versions/" in secret_reference:
        secret_id, version = secret_reference.split("/versions/", 1)
    else:
        secret_id, version = secret_reference, "latest"

    secret_id = secret_id.strip("/")
    version = version.strip("/") or "latest"

    if not secret_id:
        logger.error(
            "Secret identifier is empty after normalization.",
            extra={"account_id": account_id, "secret_type": secret_type},
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Buildium secret configuration is invalid.",
        )

    return f"projects/{project_id}/secrets/{secret_id}/versions/{version}"


def _access_secret(
    *,
    client: secretmanager.SecretManagerServiceClient,
    secret_name: str,
    account_id: str,
    secret_type: str,
) -> str:
    from google.api_core import exceptions as google_exceptions

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

    normalized_secret_name = _normalize_secret_resource_name(
        secret_name,
        account_id=account_id,
        secret_type=secret_type,
    )

    try:
        response = client.access_secret_version(request={"name": normalized_secret_name})
    except (google_exceptions.PermissionDenied, google_exceptions.Forbidden) as exc:
        message = "Access to Buildium secret in Google Secret Manager was denied."
        logger.error(
            message,
            extra={
                "account_id": account_id,
                "secret_type": secret_type,
                "secret_name": normalized_secret_name,
            },
            exc_info=exc,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Buildium secret storage is not authorized.",
        ) from exc
    except google_exceptions.NotFound as exc:
        message = "Referenced secret was not found in Google Secret Manager."
        logger.error(
            message,
            extra={
                "account_id": account_id,
                "secret_type": secret_type,
                "secret_name": normalized_secret_name,
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
                "secret_name": normalized_secret_name,
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
                "secret_name": normalized_secret_name,
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
    from google.api_core import exceptions as google_exceptions
    from google.cloud import firestore, secretmanager

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
    sanitized_metadata = dict(metadata)

    api_secret_name = (
        metadata.get("api_secret_name")
        or metadata.get("apiSecretName")
        or metadata.get("api_secret_version_name")
        or metadata.get("apiSecretVersionName")
    )

    api_secret = _access_secret(
        client=secret_manager_client,
        secret_name=api_secret_name,
        account_id=account_id,
        secret_type="api_secret",
    )

    webhook_secret = None
    webhook_secret_source = "firestore"
    for key in _WEBHOOK_SECRET_METADATA_KEYS:
        candidate = metadata.get(key)
        if candidate is None:
            continue
        if not isinstance(candidate, str):
            logger.error(
                "Webhook secret stored in Firestore is not a string.",
                extra={
                    "account_id": account_id,
                    "document_path": document_path,
                    "metadata_key": key,
                    "metadata_type": type(candidate).__name__,
                },
            )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Buildium account webhook secret is invalid.",
            )
        if not candidate:
            # Treat empty strings as missing values and continue searching.
            continue
        webhook_secret = candidate
        sanitized_metadata.pop(key, None)
        break

    if webhook_secret is None:
        webhook_secret_source = "secret_manager"
        webhook_secret_name = None
        for key in _WEBHOOK_SECRET_NAME_KEYS:
            value = metadata.get(key)
            if value:
                webhook_secret_name = value
                break
        webhook_secret = _access_secret(
            client=secret_manager_client,
            secret_name=webhook_secret_name,
            account_id=account_id,
            secret_type="webhook_secret",
        )
    elif webhook_secret_source == "firestore":
        # Remove any legacy secret name metadata when the direct secret is stored.
        for key in _WEBHOOK_SECRET_NAME_KEYS:
            sanitized_metadata.pop(key, None)

    logger.info(
        "Resolved Buildium account context.",
        extra={
            "account_id": account_id,
            "document_path": document_path,
            "has_api_secret": bool(api_secret),
            "has_webhook_secret": bool(webhook_secret),
            "webhook_secret_source": webhook_secret_source,
        },
    )

    return BuildiumAccountContext(
        account_id=account_id,
        metadata=sanitized_metadata,
        api_secret=api_secret,
        webhook_secret=webhook_secret,
    )


__all__ = ["BuildiumAccountContext", "get_buildium_account_context"]
