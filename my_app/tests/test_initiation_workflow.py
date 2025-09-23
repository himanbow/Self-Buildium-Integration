from __future__ import annotations

from types import SimpleNamespace
from typing import Any, Dict, List, Mapping, Optional, Sequence

import importlib

initiation = importlib.import_module("my_app.tasks.initiation")


class FakeDocument:
    def __init__(self, path: str) -> None:
        self.path = path
        self.data: Dict[str, Any] = {}

    def get(self) -> Any:
        exists = bool(self.data)

        def _to_dict() -> Dict[str, Any]:
            return dict(self.data)

        return SimpleNamespace(exists=exists, to_dict=_to_dict)

    def set(self, data: Mapping[str, Any], merge: bool = False) -> None:
        if not merge:
            self.data = dict(data)
            return
        for key, value in data.items():
            if (
                key in self.data
                and isinstance(self.data[key], dict)
                and isinstance(value, Mapping)
            ):
                self.data[key].update(value)
            else:
                self.data[key] = value


class FakeCollection:
    def __init__(self, path: str) -> None:
        self.path = path
        self._documents: Dict[str, FakeDocument] = {}

    def document(self, document_id: str) -> FakeDocument:
        if document_id not in self._documents:
            self._documents[document_id] = FakeDocument(
                f"{self.path}/{document_id}"
            )
        return self._documents[document_id]


class FakeFirestore:
    def __init__(self) -> None:
        self.collection_calls: List[str] = []
        self.collection_instance = FakeCollection(initiation.FIRESTORE_COLLECTION_PATH)

    def collection(self, path: str) -> FakeCollection:
        self.collection_calls.append(path)
        return self.collection_instance


class FakeBuildiumAPI:
    def __init__(self) -> None:
        self.created_tasks: List[Mapping[str, Any]] = []

    def list_gl_accounts(self) -> Sequence[Mapping[str, Any]]:
        return [
            {"id": 1, "code": "4000", "name": "Rent Income"},
            {"id": 2, "code": "4100", "name": "Parking Income"},
        ]

    def list_task_categories(self) -> Sequence[Mapping[str, Any]]:
        return [
            {"id": "1", "name": "General"},
            {"id": "2", "name": "Automated Tasks"},
        ]

    def get_company_profile(self) -> Mapping[str, Any]:
        return {"name": "Example PM", "contact": "pm@example.com"}

    def list_document_templates(self) -> Sequence[Mapping[str, Any]]:
        return [
            {"id": "tmp-1", "name": "N1 Template"},
            {"id": "tmp-2", "name": "Notice of Entry"},
        ]

    def create_task(
        self,
        *,
        category_id: Optional[str],
        name: str,
        description: str,
    ) -> Mapping[str, Any]:
        payload = {
            "category_id": category_id,
            "name": name,
            "description": description,
        }
        self.created_tasks.append(payload)
        return payload


def test_handle_initiation_persists_metadata_and_creates_task() -> None:
    firestore = FakeFirestore()
    api = FakeBuildiumAPI()

    initiation.handle_initiation_automation(
        account_id="acct-1",
        api_headers={"Authorization": "Bearer token"},
        gl_mapping={"4000": "Income"},
        webhook={"eventType": "TaskCreated"},
        firestore_client=firestore,
        buildium_api=api,
    )

    document = firestore.collection_instance.document("acct-1")
    persisted = document.data

    assert persisted["automated_tasks_category_id"] == "2"
    assert persisted["company"] == {"name": "Example PM", "contact": "pm@example.com"}
    gl_accounts = persisted["gl_accounts"]
    assert gl_accounts == [
        {"id": "1", "name": "Rent Income"},
        {"id": "2", "name": "Parking Income"},
    ]
    for account in gl_accounts:
        assert set(account.keys()) == {"id", "name"}
        assert isinstance(account["id"], str)
    assert persisted["gl_mapping"] == {"4000": "Income"}
    assert persisted["document_templates"][0]["name"] == "N1 Template"
    assert persisted["initiation_completed"] is True

    assert api.created_tasks, "Expected onboarding task to be created"
    task = api.created_tasks[0]
    assert task["category_id"] == "2"
    assert "logo" in task["description"].lower()
    assert "gl" in task["description"].lower()
    assert "rent income" in task["description"].lower()
