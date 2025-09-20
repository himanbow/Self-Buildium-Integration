from __future__ import annotations

from types import SimpleNamespace
from typing import Any, Dict, List

import importlib

import pytest


processor = importlib.import_module("my_app.jobs.processor")


class FakeProcessor:
    def __init__(self, verified: Any) -> None:
        self._context = processor.BuildiumProcessingContext(
            api_headers={"Authorization": "Bearer job"},
            gl_mapping={"4000": "Income"},
        )

    @property
    def processing_context(self) -> processor.BuildiumProcessingContext:
        return self._context


class FakeFirestoreClient:
    def __init__(self, account_ids: List[str]) -> None:
        self._account_ids = account_ids

    def collection(self, path: str) -> "FakeFirestoreClient":
        assert path == processor.FIRESTORE_COLLECTION_PATH
        return self

    def stream(self):
        for account_id in self._account_ids:
            yield SimpleNamespace(id=account_id)


@pytest.fixture(autouse=True)
def _reset_registry(monkeypatch: pytest.MonkeyPatch) -> None:
    """Ensure automation registry uses patched handlers during tests."""

    monkeypatch.setattr(processor, "BuildiumWebhookProcessor", FakeProcessor)


def test_run_job_invokes_registered_handlers(monkeypatch: pytest.MonkeyPatch) -> None:
    contexts: Dict[str, Any] = {
        "acct-1": SimpleNamespace(
            account_id="acct-1",
            metadata={},
            api_secret="{}",
            webhook_secret="hook",
        )
    }

    def fake_context(account_id: str, **_: Any) -> Any:
        return contexts[account_id]

    initiation_calls: List[Dict[str, Any]] = []
    n1_calls: List[Dict[str, Any]] = []

    def fake_initiation(**kwargs: Any) -> None:
        initiation_calls.append(kwargs)

    def fake_n1(**kwargs: Any) -> None:
        n1_calls.append(kwargs)

    monkeypatch.setattr(processor, "get_buildium_account_context", fake_context)
    monkeypatch.setitem(
        processor._AUTOMATION_REGISTRY["initiation"], "handler", fake_initiation
    )
    monkeypatch.setitem(
        processor._AUTOMATION_REGISTRY["n1increase"], "handler", fake_n1
    )

    processed = processor.run_job(
        account_ids=["acct-1"],
        firestore_client=SimpleNamespace(name="firestore"),
        secret_manager_client=SimpleNamespace(name="secrets"),
    )

    assert processed == 2
    assert initiation_calls and n1_calls

    init_kwargs = initiation_calls[0]
    assert init_kwargs["account_id"] == "acct-1"
    assert "firestore_client" in init_kwargs
    assert init_kwargs["webhook"]["eventType"] == "TaskCreated"

    n1_kwargs = n1_calls[0]
    assert n1_kwargs["webhook"]["eventType"].lower() == "taskcreated"
    assert n1_kwargs["firestore_client"].name == "firestore"


def test_run_job_supports_status_transition(monkeypatch: pytest.MonkeyPatch) -> None:
    contexts: Dict[str, Any] = {
        "acct-2": SimpleNamespace(
            account_id="acct-2",
            metadata={},
            api_secret="{}",
            webhook_secret="hook",
        )
    }

    def fake_context(account_id: str, **_: Any) -> Any:
        return contexts[account_id]

    recorded: List[Dict[str, Any]] = []

    def fake_n1(**kwargs: Any) -> None:
        recorded.append(kwargs)

    monkeypatch.setattr(processor, "get_buildium_account_context", fake_context)
    monkeypatch.setitem(
        processor._AUTOMATION_REGISTRY["n1increase"], "handler", fake_n1
    )

    processed = processor.run_job(
        account_ids=["acct-2"],
        automations=["n1increase"],
        event_type="taskstatuschanged",
        status=None,
        firestore_client=SimpleNamespace(name="firestore"),
        secret_manager_client=SimpleNamespace(name="secrets"),
    )

    assert processed == 1
    assert recorded
    webhook = recorded[0]["webhook"]
    assert webhook["eventType"] == "TaskStatusChanged"
    assert webhook["task"]["status"] == "Completed"
    assert webhook["changes"]["status"]["newValue"] == "Completed"


def test_fetch_all_account_ids_returns_snapshot_ids() -> None:
    firestore_client = FakeFirestoreClient(["acct-1", "acct-2"])
    account_ids = processor._fetch_all_account_ids(firestore_client)
    assert account_ids == ["acct-1", "acct-2"]


def test_main_invokes_run_job(monkeypatch: pytest.MonkeyPatch) -> None:
    firestore_client = FakeFirestoreClient(["acct-2"])
    secret_client = SimpleNamespace(name="secrets")

    monkeypatch.setattr(
        processor,
        "firestore",
        SimpleNamespace(Client=lambda: firestore_client),
    )
    monkeypatch.setattr(
        processor,
        "secretmanager",
        SimpleNamespace(SecretManagerServiceClient=lambda: secret_client),
    )

    recorded: Dict[str, Any] = {}

    def fake_run_job(**kwargs: Any) -> int:
        recorded.update(kwargs)
        return 7

    monkeypatch.setattr(processor, "run_job", fake_run_job)

    exit_code = processor.main([
        "--account",
        "acct-1",
        "--all-accounts",
        "--automation",
        "n1increase",
        "--event",
        "taskcreated",
    ])

    assert exit_code == 0
    assert recorded["account_ids"] == ["acct-1", "acct-2"]
    assert recorded["automations"] == ["n1increase"]
    assert recorded["event_type"] == "taskcreated"
    assert recorded["firestore_client"] is firestore_client
    assert recorded["secret_manager_client"] is secret_client
