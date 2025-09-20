from __future__ import annotations

import asyncio
import base64
import hashlib
import hmac
import json
import sys
import time
import types
from typing import Any, Mapping, Optional

import pytest
from fastapi import HTTPException, status

def _install_google_stubs() -> None:
    google_module = sys.modules.setdefault("google", types.ModuleType("google"))
    if not hasattr(google_module, "__path__"):
        google_module.__path__ = []  # type: ignore[attr-defined]

    api_core_module = sys.modules.setdefault("google.api_core", types.ModuleType("google.api_core"))
    if not hasattr(api_core_module, "__path__"):
        api_core_module.__path__ = []  # type: ignore[attr-defined]

    api_core_exceptions = sys.modules.setdefault(
        "google.api_core.exceptions",
        types.ModuleType("google.api_core.exceptions"),
    )
    if not hasattr(api_core_exceptions, "NotFound"):
        class _FakeGoogleError(Exception):
            pass

        api_core_exceptions.NotFound = _FakeGoogleError  # type: ignore[attr-defined]
        api_core_exceptions.GoogleAPICallError = _FakeGoogleError  # type: ignore[attr-defined]
    api_core_module.exceptions = api_core_exceptions  # type: ignore[attr-defined]

    cloud_module = sys.modules.setdefault("google.cloud", types.ModuleType("google.cloud"))
    if not hasattr(cloud_module, "__path__"):
        cloud_module.__path__ = []  # type: ignore[attr-defined]

    tasks_v2_module = sys.modules.setdefault(
        "google.cloud.tasks_v2",
        types.ModuleType("google.cloud.tasks_v2"),
    )
    if not hasattr(tasks_v2_module, "CloudTasksClient"):
        class _FakeCloudTasksClient:  # pragma: no cover - simple stub
            pass

        tasks_v2_module.CloudTasksClient = _FakeCloudTasksClient  # type: ignore[attr-defined]

    cloud_module.tasks_v2 = tasks_v2_module  # type: ignore[attr-defined]
    google_module.cloud = cloud_module  # type: ignore[attr-defined]

    for submodule in ("firestore", "secretmanager"):
        module_name = f"google.cloud.{submodule}"
        module = sys.modules.setdefault(module_name, types.ModuleType(module_name))
        setattr(cloud_module, submodule, module)


_install_google_stubs()

from my_app.services.account_context import BuildiumAccountContext
import my_app.webhooks.verification as verification


class _FakeEnvelope:
    def __init__(self, headers: Mapping[str, str], body: bytes, parsed_body: Optional[Any]) -> None:
        self.headers = dict(headers)
        self.body = body
        self.parsed_body = parsed_body


def _install_account_context(monkeypatch: pytest.MonkeyPatch, webhook_secret: str) -> None:
    def _fake_get_buildium_account_context(
        account_id: str,
        *,
        firestore_client: Optional[Any] = None,
        secret_manager_client: Optional[Any] = None,
    ) -> BuildiumAccountContext:
        return BuildiumAccountContext(
            account_id=account_id,
            metadata={},
            api_secret="",
            webhook_secret=webhook_secret,
        )

    monkeypatch.setattr(verification, "get_buildium_account_context", _fake_get_buildium_account_context)


def _build_body(account_id: str) -> bytes:
    payload = {"AccountId": account_id}
    return json.dumps(payload, separators=(",", ":")).encode("utf-8")


def test_verify_buildium_webhook_accepts_legacy_hex_signature(monkeypatch: pytest.MonkeyPatch) -> None:
    account_id = "acct-123"
    secret = "legacy-secret"
    _install_account_context(monkeypatch, secret)

    body = _build_body(account_id)
    signature = hmac.new(secret.encode("utf-8"), body, hashlib.sha256).hexdigest()

    envelope = _FakeEnvelope(
        headers={"X-Buildium-Hmac-SHA256": signature},
        body=body,
        parsed_body={"AccountId": account_id},
    )

    verified = asyncio.run(verification.verify_buildium_webhook(envelope))

    assert verified.account_id == account_id
    assert verified.signature == signature
    assert verified.verification_scheme == "hmac"


def test_verify_buildium_webhook_accepts_structured_signature(monkeypatch: pytest.MonkeyPatch) -> None:
    account_id = "acct-789"
    secret = "structured-secret"
    _install_account_context(monkeypatch, secret)

    body = _build_body(account_id)
    timestamp = str(int(time.time()))
    signed_payload = f"{timestamp}.".encode("utf-8") + body
    digest = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).digest()
    signature = base64.b64encode(digest).decode("ascii")

    envelope = _FakeEnvelope(
        headers={
            "X-Buildium-Signature": f"t={timestamp},v1={signature}",
        },
        body=body,
        parsed_body={"AccountId": account_id},
    )

    verified = asyncio.run(verification.verify_buildium_webhook(envelope))

    assert verified.account_id == account_id
    assert verified.signature == signature
    assert verified.verification_scheme == "hmac"


def test_verify_buildium_webhook_accepts_timestamp_headers(monkeypatch: pytest.MonkeyPatch) -> None:
    account_id = "acct-001"
    secret = "timestamp-secret"
    _install_account_context(monkeypatch, secret)

    body = _build_body(account_id)
    timestamp = str(int(time.time()))
    signed_payload = f"{timestamp}.".encode("utf-8") + body
    digest = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).digest()
    signature = base64.b64encode(digest).decode("ascii")

    envelope = _FakeEnvelope(
        headers={
            "Buildium-Webhook-Signature": signature,
            "Buildium-Webhook-Timestamp": timestamp,
        },
        body=body,
        parsed_body={"AccountId": account_id},
    )

    verified = asyncio.run(verification.verify_buildium_webhook(envelope))

    assert verified.account_id == account_id
    assert verified.signature == signature
    assert verified.verification_scheme == "hmac"


def test_verify_buildium_webhook_rejects_stale_timestamp(monkeypatch: pytest.MonkeyPatch) -> None:
    account_id = "acct-456"
    secret = "stale-secret"
    _install_account_context(monkeypatch, secret)

    body = _build_body(account_id)
    timestamp_int = int(time.time()) - (verification._SIGNATURE_MAX_AGE_SECONDS + 10)
    timestamp = str(timestamp_int)
    signed_payload = f"{timestamp}.".encode("utf-8") + body
    digest = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).digest()
    signature = base64.b64encode(digest).decode("ascii")

    envelope = _FakeEnvelope(
        headers={
            "X-Buildium-Signature": f"t={timestamp},v1={signature}",
        },
        body=body,
        parsed_body={"AccountId": account_id},
    )

    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(verification.verify_buildium_webhook(envelope))

    assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED
