from __future__ import annotations

from dataclasses import dataclass
from types import SimpleNamespace
from typing import Any, Mapping
from unittest.mock import Mock

import importlib

buildium_processor = importlib.import_module("my_app.tasks.buildium_processor")
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
    )
    return buildium_processor.BuildiumWebhookProcessor(verified)


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
