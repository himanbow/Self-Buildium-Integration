from __future__ import annotations

import base64
import json
import logging
from dataclasses import dataclass
from types import SimpleNamespace
from typing import Any, Dict, Mapping, Optional
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


_AUTOMATED_CATEGORY_ID = "cat-automated"


@dataclass(frozen=True)
class _StubAccountContext:
    account_id: str
    metadata: Mapping[str, Any]
    api_secret: str
    webhook_secret: str


@dataclass
class _StubTasksApi:
    response: Mapping[str, Any]
    side_effect: Optional[Exception] = None
    calls: list[int] | None = None

    def __post_init__(self) -> None:
        self.calls = []

    def get_task_by_id(self, task_id: int) -> Mapping[str, Any]:
        self.calls.append(task_id)
        if self.side_effect is not None:
            raise self.side_effect
        return self.response


def _patch_tasks_api(
    monkeypatch: pytest.MonkeyPatch,
    response: Optional[Mapping[str, Any]],
    *,
    side_effect: Optional[Exception] = None,
):
    captured_headers: Dict[str, Any] = {}

    if response is None:
        def _factory(api_headers: Mapping[str, Any]) -> None:
            captured_headers.clear()
            captured_headers.update(dict(api_headers))
            return None

        monkeypatch.setattr(buildium_processor, "_build_tasks_api", _factory)
        return None, captured_headers

    stub = _StubTasksApi(response=response, side_effect=side_effect)

    def _factory(api_headers: Mapping[str, Any]) -> _StubTasksApi:
        captured_headers.clear()
        captured_headers.update(dict(api_headers))
        return stub

    monkeypatch.setattr(buildium_processor, "_build_tasks_api", _factory)
    return stub, captured_headers


def _make_processor(
    parsed_body: Mapping[str, Any], *, metadata: Optional[Mapping[str, Any]] = None
) -> Any:
    account_context = _StubAccountContext(
        account_id="acct-123",
        metadata=dict(metadata or {}),
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


def _find_log(caplog, message: str) -> logging.LogRecord:
    return next(record for record in caplog.records if record.getMessage() == message)


def test_perform_work_logs_when_webhook_is_not_mapping(caplog) -> None:
    processor = _make_processor({})
    payload = dict(_base_payload({}))
    payload["webhook"] = "invalid"

    with caplog.at_level(logging.INFO):
        processor._perform_work(payload)

    record = _find_log(
        caplog, "Skipping Buildium webhook without structured task payload."
    )
    assert record.levelno == logging.INFO
    assert record.has_webhook_mapping is False
    assert record.task_identifier is None
    assert record.event_type is None
    assert record.task_category_name is None
    assert record.configured_category_id is None


def test_perform_work_logs_when_task_data_missing(monkeypatch, caplog) -> None:
    processor = _make_processor({})
    webhook_payload = {"eventType": "TaskCreated", "taskId": 555}
    payload = _base_payload(webhook_payload)
    _patch_tasks_api(monkeypatch, response=None)

    with caplog.at_level(logging.INFO):
        processor._perform_work(payload)

    record = _find_log(caplog, "No task details available in Buildium webhook payload.")
    assert record.levelno == logging.INFO
    assert record.has_task_data is False
    assert record.task_identifier == 555
    assert record.event_type == "TaskCreated"
    assert record.task_category_name is None
    assert record.configured_category_id is None


def test_perform_work_ignores_non_automated_tasks(monkeypatch, caplog) -> None:
    processor = _make_processor({}, metadata={"automated_tasks_category_id": _AUTOMATED_CATEGORY_ID})
    webhook_payload = {
        "eventType": "TaskCreated",
        "task": {
            "taskName": "Initiation",
            "taskCategoryName": "General",
            "taskId": 101,
        },
    }
    payload = _base_payload(webhook_payload)

    mock_handler = Mock()
    monkeypatch.setattr(
        buildium_processor,
        "_AUTOMATION_ROUTING_TABLE",
        {("taskcreated", "initiation"): mock_handler},
    )

    stub, headers = _patch_tasks_api(
        monkeypatch,
        {
            "Title": "Initiation",
            "Category": {
                "taskCategoryName": "General",
                "taskCategoryId": "cat-general",
            },
        },
    )

    with caplog.at_level(logging.INFO):
        processor._perform_work(payload)

    mock_handler.assert_not_called()
    assert stub.calls == [101]
    assert headers == {"Authorization": "Bearer token"}

    record = next(
        entry
        for entry in caplog.records
        if entry.getMessage() == "Ignoring non-automated Buildium task payload."
    )
    assert record.levelno == logging.INFO
    assert record.task_identifier == 101
    assert record.event_type == "TaskCreated"
    assert record.task_category_name == "General"
    assert record.configured_category_id == _AUTOMATED_CATEGORY_ID
    assert record.requires_automated_category is True
    assert record.task_category_key == "general"


def test_perform_work_logs_when_category_configuration_missing(monkeypatch, caplog) -> None:
    processor = _make_processor({}, metadata={})
    webhook_payload = {
        "eventType": "TaskCreated",
        "task": {
            "taskName": "N1 Increase",
            "taskCategoryName": "Automated Tasks",
            "taskId": 202,
        },
    }
    payload = _base_payload(webhook_payload)

    mock_handler = Mock()
    monkeypatch.setattr(
        buildium_processor,
        "_AUTOMATION_ROUTING_TABLE",
        {("taskcreated", "n1increase"): mock_handler},
    )

    _patch_tasks_api(
        monkeypatch,
        {
            "Title": "N1 Increase",
            "Category": {
                "taskCategoryName": "Automated Tasks",
                "taskCategoryId": _AUTOMATED_CATEGORY_ID,
            },
        },
    )

    with caplog.at_level(logging.INFO):
        processor._perform_work(payload)

    mock_handler.assert_not_called()

    record = _find_log(
        caplog,
        "Skipping Buildium automation without configured task category identifier.",
    )
    assert record.levelno == logging.WARNING
    assert record.task_identifier == 202
    assert record.event_type == "TaskCreated"
    assert record.task_category_name == "Automated Tasks"
    assert record.configured_category_id is None
    assert record.task_category_id == _AUTOMATED_CATEGORY_ID


def test_perform_work_logs_when_task_category_identifier_missing(
    monkeypatch, caplog
) -> None:
    processor = _make_processor(
        {}, metadata={"automated_tasks_category_id": _AUTOMATED_CATEGORY_ID}
    )
    webhook_payload = {
        "eventType": "TaskCreated",
        "task": {
            "taskName": "N1 Increase",
            "taskCategoryName": "Automated Tasks",
            "taskId": 303,
        },
    }
    payload = _base_payload(webhook_payload)

    mock_handler = Mock()
    monkeypatch.setattr(
        buildium_processor,
        "_AUTOMATION_ROUTING_TABLE",
        {("taskcreated", "n1increase"): mock_handler},
    )

    _patch_tasks_api(
        monkeypatch,
        {
            "Title": "N1 Increase",
            "Category": {"taskCategoryName": "Automated Tasks"},
        },
    )

    with caplog.at_level(logging.INFO):
        processor._perform_work(payload)

    mock_handler.assert_not_called()

    record = _find_log(
        caplog, "Skipping Buildium automation without task category identifier."
    )
    assert record.levelno == logging.INFO
    assert record.task_identifier == 303
    assert record.event_type == "TaskCreated"
    assert record.task_category_name == "Automated Tasks"
    assert record.configured_category_id == _AUTOMATED_CATEGORY_ID


def test_perform_work_logs_when_task_category_identifier_mismatched(
    monkeypatch, caplog
) -> None:
    processor = _make_processor(
        {}, metadata={"automated_tasks_category_id": _AUTOMATED_CATEGORY_ID}
    )
    webhook_payload = {
        "eventType": "TaskCreated",
        "task": {
            "taskName": "N1 Increase",
            "taskCategoryName": "Automated Tasks",
            "taskId": 404,
        },
    }
    payload = _base_payload(webhook_payload)

    mock_handler = Mock()
    monkeypatch.setattr(
        buildium_processor,
        "_AUTOMATION_ROUTING_TABLE",
        {("taskcreated", "n1increase"): mock_handler},
    )

    _patch_tasks_api(
        monkeypatch,
        {
            "Title": "N1 Increase",
            "Category": {
                "taskCategoryName": "Automated Tasks",
                "taskCategoryId": "cat-other",
            },
        },
    )

    with caplog.at_level(logging.INFO):
        processor._perform_work(payload)

    mock_handler.assert_not_called()

    record = _find_log(
        caplog,
        "Ignoring Buildium task with mismatched automation category identifier.",
    )
    assert record.levelno == logging.WARNING
    assert record.task_identifier == 404
    assert record.event_type == "TaskCreated"
    assert record.task_category_name == "Automated Tasks"
    assert record.configured_category_id == _AUTOMATED_CATEGORY_ID
    assert record.task_category_id == "cat-other"


def test_perform_work_routes_automated_tasks(monkeypatch) -> None:
    processor = _make_processor({}, metadata={"automated_tasks_category_id": _AUTOMATED_CATEGORY_ID})

    initiation_webhook = {
        "eventType": "TaskCreated",
        "task": {
            "taskName": "Initiation",
            "taskCategoryName": "Automated Tasks",
            "taskId": 202,
        },
    }
    n1_webhook = {
        "eventType": "TaskStatusChanged",
        "task": {
            "taskName": "N1 Increase",
            "taskCategoryName": "General",
            "taskId": 303,
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

    init_stub, init_headers = _patch_tasks_api(
        monkeypatch,
        {
            "Id": 202,
            "Title": "Initiation",
            "Category": {
                "taskCategoryName": "Automated Tasks",
                "taskCategoryId": _AUTOMATED_CATEGORY_ID,
            },
        },
    )

    processor._perform_work(_base_payload(initiation_webhook))

    init_handler.assert_called_once()
    init_call = init_handler.call_args
    assert init_call.kwargs["account_id"] == "acct-123"
    assert init_call.kwargs["api_headers"] == {"Authorization": "Bearer token"}
    assert init_call.kwargs["gl_mapping"] == {"code": "value"}
    assert init_stub.calls == [202]
    assert init_headers == {"Authorization": "Bearer token"}
    assert init_call.kwargs["webhook"]["task"] == {
        "Id": 202,
        "Title": "Initiation",
        "Category": {
            "taskCategoryName": "Automated Tasks",
            "taskCategoryId": _AUTOMATED_CATEGORY_ID,
        },
    }

    n1_stub, n1_headers = _patch_tasks_api(
        monkeypatch,
        {
            "Id": 303,
            "Title": "N1 Increase",
            "Category": {
                "taskCategoryName": "Automated Tasks",
                "taskCategoryId": _AUTOMATED_CATEGORY_ID,
            },
        },
    )

    processor._perform_work(_base_payload(n1_webhook))

    n1_handler.assert_called_once()
    n1_call = n1_handler.call_args
    assert n1_call.kwargs["account_id"] == "acct-123"
    assert n1_call.kwargs["api_headers"] == {"Authorization": "Bearer token"}
    assert n1_call.kwargs["gl_mapping"] == {"code": "value"}
    assert n1_stub.calls == [303]
    assert n1_headers == {"Authorization": "Bearer token"}
    assert n1_call.kwargs["webhook"]["task"] == {
        "Id": 303,
        "Title": "N1 Increase",
        "Category": {
            "taskCategoryName": "Automated Tasks",
            "taskCategoryId": _AUTOMATED_CATEGORY_ID,
        },
    }


def test_perform_work_skips_when_category_identifier_mismatch(monkeypatch) -> None:
    processor = _make_processor({}, metadata={"automated_tasks_category_id": _AUTOMATED_CATEGORY_ID})

    webhook_payload = {
        "eventType": "TaskStatusChanged",
        "task": {
            "taskName": "N1 Increase",
            "taskCategoryName": "Automated Tasks",
            "taskId": 707,
        },
    }

    mock_handler = Mock()
    monkeypatch.setattr(
        buildium_processor,
        "_AUTOMATION_ROUTING_TABLE",
        {("taskstatuschanged", "n1increase"): mock_handler},
    )

    stub, _ = _patch_tasks_api(
        monkeypatch,
        {
            "Id": 707,
            "Title": "N1 Increase",
            "taskCategoryId": "cat-other",
            "Category": {
                "taskCategoryName": "Automated Tasks",
                "taskCategoryId": "cat-other",
            },
        },
    )

    processor._perform_work(_base_payload(webhook_payload))

    mock_handler.assert_not_called()
    assert stub.calls == [707]


def test_perform_work_routes_initiation_without_category(monkeypatch) -> None:
    processor = _make_processor({}, metadata={"automated_tasks_category_id": _AUTOMATED_CATEGORY_ID})

    initiation_webhook = {
        "eventType": "TaskCreated",
        "task": {
            "taskName": "Ontario Automations Initiation",
            "taskCategoryName": "General",
            "taskId": 401,
        },
    }

    mock_handler = Mock()
    monkeypatch.setattr(
        buildium_processor,
        "_AUTOMATION_ROUTING_TABLE",
        {buildium_processor._INITIATION_AUTOMATION_KEY: mock_handler},
    )
    monkeypatch.setattr(
        buildium_processor,
        "_has_completed_initiation",
        lambda account_id: False,
    )

    stub, _ = _patch_tasks_api(
        monkeypatch,
        {
            "Id": 401,
            "Title": "Ontario Automations Initiation",
            "Category": {
                "taskCategoryName": "General",
                "taskCategoryId": "cat-general",
            },
        },
    )

    processor._perform_work(_base_payload(initiation_webhook))

    mock_handler.assert_called_once()
    assert stub.calls == [401]


def test_perform_work_skips_completed_initiation(monkeypatch) -> None:
    processor = _make_processor({}, metadata={"automated_tasks_category_id": _AUTOMATED_CATEGORY_ID})

    initiation_webhook = {
        "eventType": "TaskCreated",
        "task": {
            "taskName": "Ontario Automations Initiation",
            "taskCategoryName": "General",
            "taskId": 402,
        },
    }

    mock_handler = Mock()

    monkeypatch.setattr(
        buildium_processor,
        "_AUTOMATION_ROUTING_TABLE",
        {buildium_processor._INITIATION_AUTOMATION_KEY: mock_handler},
    )

    def _completed(account_id: str) -> bool:
        assert account_id == "acct-123"
        return True

    monkeypatch.setattr(buildium_processor, "_has_completed_initiation", _completed)

    stub, _ = _patch_tasks_api(
        monkeypatch,
        {
            "Id": 402,
            "Title": "Ontario Automations Initiation",
            "Category": {
                "taskCategoryName": "General",
                "taskCategoryId": "cat-general",
            },
        },
    )

    processor._perform_work(_base_payload(initiation_webhook))

    mock_handler.assert_not_called()
    assert stub.calls == [402]


def test_perform_work_uses_webhook_when_task_fetch_fails(monkeypatch) -> None:
    processor = _make_processor({}, metadata={"automated_tasks_category_id": _AUTOMATED_CATEGORY_ID})

    webhook_payload = {
        "eventType": "TaskStatusChanged",
        "task": {
            "taskName": "N1 Increase",
            "taskCategoryName": "Automated Tasks",
            "taskCategoryId": _AUTOMATED_CATEGORY_ID,
            "taskId": 909,
        },
    }
    payload = _base_payload(webhook_payload)

    mock_handler = Mock()
    monkeypatch.setattr(
        buildium_processor,
        "_AUTOMATION_ROUTING_TABLE",
        {("taskstatuschanged", "n1increase"): mock_handler},
    )

    stub, headers = _patch_tasks_api(
        monkeypatch,
        {
            "Id": 909,
            "Title": "N1 Increase",
            "Category": {
                "taskCategoryName": "Automated Tasks",
                "taskCategoryId": _AUTOMATED_CATEGORY_ID,
            },
        },
        side_effect=RuntimeError("boom"),
    )

    processor._perform_work(payload)

    mock_handler.assert_called_once()
    call = mock_handler.call_args
    assert call.kwargs["webhook"]["task"] == webhook_payload["task"]
    assert stub.calls == [909]
    assert headers == {"Authorization": "Bearer token"}


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
    monkeypatch.delenv("CLOUD_RUN_REGION", raising=False)

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

    monkeypatch.delenv("CLOUD_TASKS_LOCATION", raising=False)
    monkeypatch.delenv("CLOUD_RUN_REGION", raising=False)

    response = buildium_processor.enqueue_buildium_webhook(verified_webhook, client=client)

    assert response["name"] == "tasks/example"
    assert client.queue_path_args == (
        config.DEFAULT_GCP_PROJECT_ID,
        buildium_processor._DEFAULT_CLOUD_TASKS_LOCATION,
        buildium_processor._DEFAULT_CLOUD_TASKS_QUEUE,
    )
    assert client.requests, "Cloud Tasks request was not issued."


def test_enqueue_buildium_webhook_supports_legacy_env_vars(monkeypatch) -> None:
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

    monkeypatch.setenv("GOOGLE_CLOUD_PROJECT", "legacy-project")
    monkeypatch.delenv("CLOUD_TASKS_QUEUE", raising=False)
    monkeypatch.delenv("CLOUD_TASKS_LOCATION", raising=False)
    monkeypatch.delenv("TASK_HANDLER_URL", raising=False)
    monkeypatch.setenv("BUILDUM_TASKS_QUEUE", "legacy-queue")
    monkeypatch.setenv("BUILDUM_TASKS_LOCATION", "northamerica-northeast1")
    monkeypatch.setenv(
        "BUILDUM_TASKS_SERVICE_URL",
        "https://legacy.example.com/tasks/buildium-webhook",
    )

    response = buildium_processor.enqueue_buildium_webhook(verified_webhook, client=client)

    assert response["name"] == "tasks/example"
    assert client.queue_path_args == (
        "legacy-project",
        "northamerica-northeast1",
        "legacy-queue",
    )
    assert client.requests, "Cloud Tasks request was not issued."

    request = client.requests[0]
    assert (
        request["parent"]
        == "projects/legacy-project/locations/northamerica-northeast1/queues/legacy-queue"
    )
    http_request = request["task"]["http_request"]
    assert http_request["url"] == "https://legacy.example.com/tasks/buildium-webhook"


def test_enqueue_buildium_webhook_uses_cloud_run_region(monkeypatch) -> None:
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

    monkeypatch.delenv("CLOUD_TASKS_LOCATION", raising=False)
    monkeypatch.setenv("CLOUD_RUN_REGION", "northamerica-northeast2")

    response = buildium_processor.enqueue_buildium_webhook(verified_webhook, client=client)

    assert response["name"] == "tasks/example"
    assert client.queue_path_args == (
        config.DEFAULT_GCP_PROJECT_ID,
        "northamerica-northeast2",
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
