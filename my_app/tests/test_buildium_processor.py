from __future__ import annotations

import base64
import json
from dataclasses import dataclass
from types import SimpleNamespace
from typing import Any, Dict, Mapping
from unittest.mock import Mock

import importlib

import pytest
from fastapi.testclient import TestClient

buildium_processor = importlib.import_module("my_app.tasks.buildium_processor")
buildium_listener = importlib.import_module("my_app.webhooks.buildium_listener")
config = importlib.import_module("my_app.config")
BuildiumAccountContext = importlib.import_module("my_app.services.account_context").BuildiumAccountContext
BuildiumWebhookEnvelope = buildium_listener.BuildiumWebhookEnvelope
VerifiedBuildiumWebhook = importlib.import_module(
    "my_app.webhooks.verification"
).VerifiedBuildiumWebhook


@dataclass(frozen=True)
class _StubAccountContext:
    account_id: str
    metadata: Mapping[str, Any]
    api_secret: str
    webhook_secret: str


def _make_processor(parsed_body: Mapping[str, Any]) -> Any:
    account_context = _StubAccountContext(
        account_id="acct-123",
        metadata={},
        api_secret="",
        webhook_secret="secret",
    )
    envelope = SimpleNamespace(parsed_body=parsed_body, body=b"{}")
    verified = VerifiedBuildiumWebhook(
        account_context=account_context,
        account_id="acct-123",
        envelope=envelope,
        signature="sig",
        verification_scheme="hmac",
    )
    return buildium_processor.BuildiumWebhookProcessor(verified)


def _make_verified_webhook() -> VerifiedBuildiumWebhook:
    account_context = BuildiumAccountContext(
        account_id="acct-queue",
        metadata={"gl_mapping": {"code": "value"}},
        api_secret="api-secret",
        webhook_secret="hook-secret",
    )
    envelope = BuildiumWebhookEnvelope(
        headers={"content-type": "application/json"},
        body=b"{\"event\": \"value\"}",
        parsed_body={"event": "value"},
    )
    return VerifiedBuildiumWebhook(
        account_context=account_context,
        account_id="acct-queue",
        envelope=envelope,
        signature="sig",
        verification_scheme="hmac",
    )


def _base_payload(webhook: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "account_id": "acct-123",
        "api_headers": {"Authorization": "Bearer token"},
        "gl_mapping": {"code": "value"},
        "webhook": webhook,
    }


def test_perform_work_ignores_non_automated_tasks(monkeypatch) -> None:
    processor = _make_processor({})
    webhook_payload = {
        "eventType": "TaskCreated",
        "task": {
            "taskName": "Initiation",
            "taskCategoryName": "General",
        },
    }
    payload = _base_payload(webhook_payload)

    mock_handler = Mock()
    monkeypatch.setattr(
        buildium_processor,
        "_AUTOMATION_ROUTING_TABLE",
        {("taskcreated", "initiation"): mock_handler},
    )

    processor._perform_work(payload)

    mock_handler.assert_not_called()


def test_perform_work_routes_automated_tasks(monkeypatch) -> None:
    processor = _make_processor({})

    initiation_webhook = {
        "eventType": "TaskCreated",
        "task": {
            "taskName": "Initiation",
            "taskCategoryName": "Automated Tasks",
        },
    }
    n1_webhook = {
        "eventType": "TaskStatusChanged",
        "task": {
            "taskName": "N1 Increase",
            "taskCategoryName": "Automated Tasks",
        },
    }

    init_handler = Mock()
    n1_handler = Mock()
    monkeypatch.setattr(
        buildium_processor,
        "_AUTOMATION_ROUTING_TABLE",
        {
            ("taskcreated", "initiation"): init_handler,
            ("taskstatuschanged", "n1increase"): n1_handler,
        },
    )

    processor._perform_work(_base_payload(initiation_webhook))

    init_handler.assert_called_once()
    init_call = init_handler.call_args
    assert init_call.kwargs["account_id"] == "acct-123"
    assert init_call.kwargs["api_headers"] == {"Authorization": "Bearer token"}
    assert init_call.kwargs["gl_mapping"] == {"code": "value"}
    assert init_call.kwargs["webhook"] == initiation_webhook

    processor._perform_work(_base_payload(n1_webhook))

    n1_handler.assert_called_once()
    n1_call = n1_handler.call_args
    assert n1_call.kwargs["account_id"] == "acct-123"
    assert n1_call.kwargs["api_headers"] == {"Authorization": "Bearer token"}
    assert n1_call.kwargs["gl_mapping"] == {"code": "value"}
    assert n1_call.kwargs["webhook"] == n1_webhook


def test_enqueue_buildium_webhook_creates_cloud_task(monkeypatch) -> None:
    verified_webhook = _make_verified_webhook()

    class _DummyClient:
        def __init__(self) -> None:
            self.queue_path_args = None
            self.requests = []

        def queue_path(self, project: str, location: str, queue: str) -> str:
            self.queue_path_args = (project, location, queue)
            return f"projects/{project}/locations/{location}/queues/{queue}"

        def create_task(self, request: Mapping[str, Any]) -> Mapping[str, str]:
            self.requests.append(request)
            return {"name": "tasks/example"}

    client = _DummyClient()

    monkeypatch.setenv("GOOGLE_CLOUD_PROJECT", "test-project")
    monkeypatch.setenv("CLOUD_TASKS_QUEUE", "buildium-webhooks-test")
    monkeypatch.setenv("CLOUD_TASKS_LOCATION", "us-west1")
    monkeypatch.setenv("TASK_HANDLER_URL", "https://example.com/tasks/buildium-webhook")

    response = buildium_processor.enqueue_buildium_webhook(verified_webhook, client=client)

    assert response["name"] == "tasks/example"
    assert client.queue_path_args == ("test-project", "us-west1", "buildium-webhooks-test")
    assert client.requests, "Cloud Tasks request was not issued."

    request = client.requests[0]
    assert request["parent"] == "projects/test-project/locations/us-west1/queues/buildium-webhooks-test"
    http_request = request["task"]["http_request"]
    assert http_request["url"] == "https://example.com/tasks/buildium-webhook"
    assert http_request["http_method"] == buildium_processor.tasks_v2.HttpMethod.POST

    body_payload = json.loads(http_request["body"].decode("utf-8"))
    assert body_payload["account_id"] == "acct-queue"
    assert body_payload["verification_scheme"] == "hmac"
    assert body_payload["signature"] == "sig"
    assert body_payload["account_context"]["metadata"] == {"gl_mapping": {"code": "value"}}
    assert body_payload["envelope"]["headers"] == {"content-type": "application/json"}
    assert body_payload["envelope"]["parsed_body"] == {"event": "value"}
    assert body_payload["envelope"]["body"] == base64.b64encode(b'{"event": "value"}').decode("ascii")


def test_enqueue_buildium_webhook_uses_default_project_id(monkeypatch) -> None:
    verified_webhook = _make_verified_webhook()

    class _DummyClient:
        def __init__(self) -> None:
            self.queue_path_args = None
            self.requests = []

        def queue_path(self, project: str, location: str, queue: str) -> str:
            self.queue_path_args = (project, location, queue)
            return f"projects/{project}/locations/{location}/queues/{queue}"

        def create_task(self, request: Mapping[str, Any]) -> Mapping[str, str]:
            self.requests.append(request)
            return {"name": "tasks/example"}

    client = _DummyClient()

    for env_name in (
        "GOOGLE_CLOUD_PROJECT",
        "CLOUD_RUN_PROJECT",
        "GCP_PROJECT",
        "GCLOUD_PROJECT",
        "PROJECT_ID",
    ):
        monkeypatch.delenv(env_name, raising=False)

    response = buildium_processor.enqueue_buildium_webhook(verified_webhook, client=client)

    assert response["name"] == "tasks/example"
    assert client.queue_path_args == (
        config.DEFAULT_GCP_PROJECT_ID,
        buildium_processor._DEFAULT_CLOUD_TASKS_LOCATION,
        buildium_processor._DEFAULT_CLOUD_TASKS_QUEUE,
    )
    assert client.requests, "Cloud Tasks request was not issued."


def test_handle_buildium_webhook_task_processes_payload(monkeypatch) -> None:
    verified_webhook = _make_verified_webhook()
    payload = buildium_processor._serialize_verified_webhook(verified_webhook)
    test_client = TestClient(buildium_listener.app)

    call_metadata: Dict[str, Any] = {}

    async def _run(self: Any) -> None:  # type: ignore[override]
        call_metadata.update(self.metadata)

    monkeypatch.setattr(buildium_listener.BuildiumWebhookProcessor, "run", _run)

    response = test_client.post("/tasks/buildium-webhook", json=payload)

    assert response.status_code == 204
    assert call_metadata["account_id"] == "acct-queue"


def test_handle_buildium_webhook_task_rejects_invalid_payload() -> None:
    test_client = TestClient(buildium_listener.app)
    response = test_client.post("/tasks/buildium-webhook", json={"invalid": True})
    assert response.status_code == 400
