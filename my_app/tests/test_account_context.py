from __future__ import annotations

from typing import Any, Dict, Mapping, Optional, Tuple

import pytest
from fastapi import HTTPException, status
from google.api_core import exceptions as google_exceptions

import my_app.services.account_context as account_context


class _FakeSecretPayload:
    def __init__(self, data: bytes) -> None:
        self.data = data


class _FakeSecretResponse:
    def __init__(self, payload: bytes) -> None:
        self.payload = _FakeSecretPayload(payload)


class _FakeSecretManagerClient:
    def __init__(self, secrets: Mapping[str, bytes]) -> None:
        self._secrets = dict(secrets)
        self.requests = []

    def access_secret_version(self, request: Mapping[str, Any]) -> _FakeSecretResponse:
        name = request["name"]
        self.requests.append(name)
        if name not in self._secrets:
            raise KeyError(name)
        return _FakeSecretResponse(self._secrets[name])


class _FakeSnapshot:
    def __init__(self, data: Optional[Mapping[str, Any]]) -> None:
        self._data = None if data is None else dict(data)
        self.exists = data is not None

    def to_dict(self) -> Optional[Dict[str, Any]]:
        if self._data is None:
            return None
        return dict(self._data)


class _FakeDocumentReference:
    def __init__(self, document_path: str, data: Optional[Mapping[str, Any]]) -> None:
        self.path = document_path
        self._data = None if data is None else dict(data)

    def get(self) -> _FakeSnapshot:
        return _FakeSnapshot(self._data)


class _FakeCollectionReference:
    def __init__(self, collection_path: str, documents: Mapping[str, Mapping[str, Any]]) -> None:
        self._collection_path = collection_path
        self._documents = {
            document_id: dict(payload) for document_id, payload in documents.items()
        }

    def document(self, document_id: str) -> _FakeDocumentReference:
        document_path = f"{self._collection_path}/{document_id}"
        data = self._documents.get(document_id)
        return _FakeDocumentReference(document_path, data)


class _FakeFirestoreClient:
    def __init__(self, documents: Mapping[str, Mapping[str, Any]]) -> None:
        self._documents = {
            document_id: dict(payload) for document_id, payload in documents.items()
        }

    def collection(self, path: str) -> _FakeCollectionReference:
        assert path == account_context._FIRESTORE_COLLECTION_PATH
        return _FakeCollectionReference(path, self._documents)


def test_get_buildium_account_context_uses_firestore_webhook_secret() -> None:
    account_id = "acct-123"
    firestore_client = _FakeFirestoreClient(
        {
            account_id: {
                "api_secret_name": "projects/example/secrets/api/versions/latest",
                "webhook_secret": "firestore-hook",
                "gl_mapping": {"code": "value"},
            }
        }
    )
    secret_manager_client = _FakeSecretManagerClient(
        {"projects/example/secrets/api/versions/latest": b"api-secret"}
    )

    context = account_context.get_buildium_account_context(
        account_id,
        firestore_client=firestore_client,
        secret_manager_client=secret_manager_client,
    )

    assert context.account_id == account_id
    assert context.api_secret == "api-secret"
    assert context.webhook_secret == "firestore-hook"
    assert context.metadata == {
        "api_secret_name": "projects/example/secrets/api/versions/latest",
        "gl_mapping": {"code": "value"},
    }


def test_get_buildium_account_context_falls_back_to_secret_manager_for_webhook_secret() -> None:
    account_id = "acct-456"
    firestore_client = _FakeFirestoreClient(
        {
            account_id: {
                "api_secret_name": "projects/example/secrets/api/versions/1",
                "webhook_secret_name": "projects/example/secrets/webhook/versions/1",
            }
        }
    )
    secret_manager_client = _FakeSecretManagerClient(
        {
            "projects/example/secrets/api/versions/1": b"api-secret",
            "projects/example/secrets/webhook/versions/1": b"webhook-secret",
        }
    )

    context = account_context.get_buildium_account_context(
        account_id,
        firestore_client=firestore_client,
        secret_manager_client=secret_manager_client,
    )

    assert context.api_secret == "api-secret"
    assert context.webhook_secret == "webhook-secret"
    assert context.metadata == {
        "api_secret_name": "projects/example/secrets/api/versions/1",
        "webhook_secret_name": "projects/example/secrets/webhook/versions/1",
    }


def test_access_secret_permission_denied() -> None:
    class _PermissionDeniedSecretManagerClient:
        def access_secret_version(self, request: Mapping[str, Any]) -> Any:  # pragma: no cover - interface stub
            raise google_exceptions.PermissionDenied(
                "Permission denied on resource project mantler-api-secret."
            )

    client = _PermissionDeniedSecretManagerClient()
    access_secret = getattr(account_context, "_access_secret")

    with pytest.raises(HTTPException) as exc_info:
        access_secret(
            client=client,
            secret_name="projects/example/secrets/api/versions/1",
            account_id="acct-789",
            secret_type="api_secret",
        )

    assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert exc_info.value.detail == "Buildium secret storage is not authorized."


def test_get_secret_project_id_falls_back_to_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SECRET_PROJECT_ID", raising=False)
    monkeypatch.setenv("GOOGLE_CLOUD_PROJECT", "example-project")

    def _fake_default() -> Tuple[Any, Optional[str]]:
        return object(), None

    monkeypatch.setattr(account_context.google.auth, "default", _fake_default)

    get_secret_project_id = getattr(account_context, "_get_secret_project_id")

    project_id = get_secret_project_id(account_id="acct-000", secret_type="api_secret")

    assert project_id == "example-project"
