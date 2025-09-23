from __future__ import annotations

import base64
from collections import defaultdict
from io import BytesIO
from types import SimpleNamespace
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple
from zipfile import ZipFile

import importlib

from PyPDF2 import PdfReader

n1_increase = importlib.import_module("my_app.tasks.n1_increase")
n1_data_module = importlib.import_module("my_app.tasks.n1_data")


class FakeDocument:
    def __init__(self, path: str, initial: Optional[Mapping[str, Any]] = None) -> None:
        self.path = path
        self.data: Dict[str, Any] = dict(initial or {})

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
            if key in self.data and isinstance(self.data[key], dict) and isinstance(value, Mapping):
                self.data[key].update(dict(value))
            else:
                self.data[key] = dict(value) if isinstance(value, Mapping) else value


class FakeCollection:
    def __init__(self, path: str, initial: Optional[Mapping[str, Any]] = None) -> None:
        self.path = path
        self._documents: Dict[str, FakeDocument] = {}
        self._initial = dict(initial or {})

    def document(self, document_id: str) -> FakeDocument:
        if document_id not in self._documents:
            self._documents[document_id] = FakeDocument(
                f"{self.path}/{document_id}",
                self._initial.get(document_id),
            )
        return self._documents[document_id]


class FakeFirestore:
    def __init__(self, initial_docs: Optional[Mapping[str, Any]] = None) -> None:
        self.collection_instance = FakeCollection(
            n1_increase.FIRESTORE_COLLECTION_PATH, initial_docs
        )

    def collection(self, path: str) -> FakeCollection:
        assert path == n1_increase.FIRESTORE_COLLECTION_PATH
        return self.collection_instance


class FakeBuildiumAPI:
    def __init__(self) -> None:
        self.leases: List[Mapping[str, Any]] = [
            {
                "leaseId": "lease-1",
                "property": {"id": "prop-1", "name": "Property One"},
                "unit": {"id": "unit-1", "name": "101"},
                "rent": {"amount": "1200"},
                "increaseEffectiveDate": "2024-09-01",
            },
            {
                "leaseId": "lease-2",
                "property": {"id": "prop-2", "name": "Property Two"},
                "unit": {"id": "unit-2", "name": "201"},
                "rent": {"amount": "1500"},
                "increaseEffectiveDate": "2024-09-01",
                "extension": {"extended": True, "endDate": "2025-08-31"},
            },
        ]
        self.market_rent: Dict[Tuple[str, str], Mapping[str, Any]] = {
            ("prop-1", "unit-1"): {"marketRent": "1400"},
            ("prop-2", "unit-2"): {"marketRent": "1650"},
        }
        self.lease_notes: Dict[str, List[Mapping[str, Any]]] = {
            "lease-1": [],
            "lease-2": [],
        }
        self.building_notes: Dict[str, List[Mapping[str, Any]]] = {
            "prop-1": [],
            "prop-2": [],
        }
        self.recurring_transactions: Dict[str, List[Mapping[str, Any]]] = {
            "lease-1": [
                {"amount": "1200", "glAccountNumber": "4000", "description": "Rent"}
            ],
            "lease-2": [
                {"amount": "1500", "glAccountNumber": "4000", "description": "Rent"}
            ],
        }
        self.agi_summaries: Dict[str, Mapping[str, Any]] = {
            "lease-1": {},
            "lease-2": {},
        }
        self.presigned_urls: Dict[str, Mapping[str, Any]] = {}
        self.downloaded_files: Dict[str, bytes] = {}
        self.uploaded_documents: List[Mapping[str, Any]] = []
        self.updated_leases: List[Mapping[str, Any]] = []
        self.extended_leases: List[Mapping[str, Any]] = []
        self.created_tasks: List[Mapping[str, Any]] = []
        self.task_categories: List[Mapping[str, Any]] = [
            {"id": "cat-1", "name": "Automation"}
        ]
        self.task_comments: List[Mapping[str, Any]] = []
        self.lease_renewals: List[Mapping[str, Any]] = []
        self.presign_requests: List[Mapping[str, Any]] = []
        self.presigned_uploads: List[Mapping[str, Any]] = []
        self._next_task_id = 1

    def list_eligible_leases(self) -> Sequence[Mapping[str, Any]]:
        return list(self.leases)

    def get_market_rent(self, *, property_id: str, unit_id: str) -> Optional[Mapping[str, Any]]:
        return self.market_rent.get((property_id, unit_id))

    def get_ontario_increase_rates(self) -> Mapping[str, Any]:
        return {"default": "0.025", "per_property": {"prop-1": "0.03"}}

    def list_lease_notes(self, lease_id: str) -> Sequence[Mapping[str, Any]]:
        return list(self.lease_notes.get(lease_id, []))

    def list_building_notes(self, property_id: str) -> Sequence[Mapping[str, Any]]:
        return list(self.building_notes.get(property_id, []))

    def list_recurring_transactions(self, lease_id: str) -> Sequence[Mapping[str, Any]]:
        return list(self.recurring_transactions.get(lease_id, []))

    def get_above_guideline_increase(self, *, lease_id: str) -> Mapping[str, Any]:
        return dict(self.agi_summaries.get(lease_id, {}))

    def get_presigned_download(self, download_id: str) -> Mapping[str, Any]:
        return dict(self.presigned_urls.get(download_id, {}))

    def download_presigned_url(self, url: str) -> bytes:
        return bytes(self.downloaded_files.get(url, b""))

    def upload_document(
        self,
        *,
        lease_id: str,
        property_id: str,
        filename: str,
        content: bytes,
        content_type: str,
    ) -> Mapping[str, Any]:
        self.uploaded_documents.append(
            {
                "lease_id": lease_id,
                "property_id": property_id,
                "filename": filename,
                "content": content,
                "content_type": content_type,
            }
        )
        return {}

    def update_lease(self, *, lease_id: str, payload: Mapping[str, Any]) -> Mapping[str, Any]:
        self.updated_leases.append({"lease_id": lease_id, "payload": dict(payload)})
        return payload

    def extend_lease(self, *, lease_id: str, end_date: Optional[str]) -> Mapping[str, Any]:
        self.extended_leases.append({"lease_id": lease_id, "end_date": end_date})
        return {"lease_id": lease_id, "end_date": end_date}

    def create_task(
        self,
        *,
        category_id: Optional[str],
        name: str,
        description: str,
    ) -> Mapping[str, Any]:
        task_id = f"task-{self._next_task_id}"
        self._next_task_id += 1
        payload = {
            "category_id": category_id,
            "name": name,
            "description": description,
            "id": task_id,
        }
        self.created_tasks.append(payload)
        return payload

    def create_task_history_comment(
        self, *, task_id: str, body: str
    ) -> Mapping[str, Any]:
        payload = {"task_id": task_id, "body": body}
        self.task_comments.append(payload)
        return payload

    def list_task_categories(self) -> Sequence[Mapping[str, Any]]:
        return [dict(item) for item in self.task_categories]

    def create_task_category(self, *, name: str) -> Mapping[str, Any]:
        identifier = f"cat-{len(self.task_categories) + 1}"
        payload = {"id": identifier, "name": name}
        self.task_categories.append(payload)
        return payload

    def create_lease_renewal(
        self, *, lease_id: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        record = {"lease_id": lease_id, "payload": dict(payload)}
        self.lease_renewals.append(record)
        return record

    def request_presigned_upload(
        self,
        *,
        filename: str,
        content_type: str,
        metadata: Optional[Mapping[str, Any]] = None,
    ) -> Mapping[str, Any]:
        response = {
            "url": f"https://uploads.example/{filename}",
            "fields": {"key": filename},
        }
        self.presign_requests.append(
            {
                "filename": filename,
                "content_type": content_type,
                "metadata": dict(metadata or {}),
                "response": response,
            }
        )
        return response

    def upload_to_presigned_url(
        self,
        *,
        url: str,
        fields: Mapping[str, Any],
        content: bytes,
        content_type: str,
    ) -> Mapping[str, Any]:
        record = {
            "url": url,
            "fields": dict(fields),
            "content": content,
            "content_type": content_type,
        }
        self.presigned_uploads.append(record)
        return {"status": "ok"}


def _decode_excel(excel_b64: str) -> str:
    binary = base64.b64decode(excel_b64)
    with ZipFile(BytesIO(binary)) as zf:
        data = zf.read("xl/worksheets/sheet1.xml")
    return data.decode("utf-8")


def _decode_pdf(pdf_b64: str) -> bytes:
    return base64.b64decode(pdf_b64)


def _load_pdf_reader(pdf_bytes: bytes) -> PdfReader:
    reader = PdfReader(BytesIO(pdf_bytes))
    if reader.is_encrypted:
        reader.decrypt("")
    return reader


def _collect_pdf_stream_text(reader: PdfReader) -> str:
    segments: List[str] = []
    for page in reader.pages:
        contents = page.get_contents()
        if contents is None:
            continue
        items = contents if isinstance(contents, list) else [contents]
        for item in items:
            try:
                segments.append(item.get_data().decode("latin1"))
            except Exception:  # pragma: no cover - defensive
                continue
    return "\n".join(segments)


def _pdf_stream_pattern(value: str) -> str:
    replacements = {
        " ": "\\040",
        "-": "\\055",
        "$": "\\044",
        ".": "\\056",
        "%": "\\045",
    }
    return "".join(replacements.get(ch, ch) for ch in value)


def test_handle_n1_creation_persists_schedules(monkeypatch) -> None:
    api = FakeBuildiumAPI()
    firestore = FakeFirestore(initial_docs={"acct-1": {"automated_tasks_category_id": "cat-1"}})

    monkeypatch.setattr(n1_increase, "MAX_PAYLOAD_BYTES", 200)

    n1_increase.handle_n1_increase_automation(
        account_id="acct-1",
        api_headers={"Authorization": "Bearer token"},
        gl_mapping={"4000": "Income"},
        webhook={"eventType": "TaskCreated"},
        firestore_client=firestore,
        buildium_api=api,
    )

    document = firestore.collection_instance.document("acct-1")
    data = document.data
    assert "n1_increase" in data
    n1_data = data["n1_increase"]

    assert n1_data["lease_count"] == len(api.leases)
    assert len(n1_data["payload_chunks"]) >= 1
    assert n1_data["schedules"][0]["property_name"] == "Property One"
    assert n1_data["schedules"][1]["is_extended"] is True
    assert n1_data["schedules"][0]["agi_amount"] == "0.00"

    excel_xml = _decode_excel(n1_data["summary_files"]["excel"])
    assert "Property One" in excel_xml
    assert "Property Two" in excel_xml

    pdf_bytes = _decode_pdf(n1_data["summary_files"]["pdf"])
    assert pdf_bytes.startswith(b"%PDF")

    schedule_map = {item["lease_id"]: item for item in n1_data["schedules"]}
    assert schedule_map["lease-1"]["new_rent"] == "1236.00"
    assert schedule_map["lease-2"]["new_rent"] == "1537.50"
    assert schedule_map["lease-2"]["agi_amount"] == "0.00"

    first_chunk = n1_data["payload_chunks"][0]
    assert "encryption" in first_chunk
    assert first_chunk["encryption"]["algorithm"] == "xor+zlib"

    decoded_entries = n1_data_module.decode_payload_chunk(first_chunk)
    assert decoded_entries
    assert decoded_entries[0]["schedule"]["lease_id"] == "lease-1"
    assert decoded_entries[0]["recurring_transactions"][0]["amount"] == "1200.00"


def test_handle_n1_completion_generates_documents(monkeypatch) -> None:
    api = FakeBuildiumAPI()
    schedules = [
        {
            "lease_id": "lease-1",
            "property_id": "prop-1",
            "unit_id": "unit-1",
            "property_name": "Property One",
            "unit_name": "101",
            "current_rent": "1200.00",
            "new_rent": "1236.00",
            "increase_rate": "0.03",
            "increase_rate_percent": "3.00%",
            "increase_amount": "36.00",
            "effective_date": "2024-09-01",
            "is_extended": False,
            "extension_end_date": None,
        },
        {
            "lease_id": "lease-2",
            "property_id": "prop-2",
            "unit_id": "unit-2",
            "property_name": "Property Two",
            "unit_name": "201",
            "current_rent": "1500.00",
            "new_rent": "1537.50",
            "increase_rate": "0.025",
            "increase_rate_percent": "2.50%",
            "increase_amount": "37.50",
            "effective_date": "2024-09-01",
            "is_extended": True,
            "extension_end_date": "2025-08-31",
        },
    ]
    firestore = FakeFirestore(
        initial_docs={
            "acct-1": {
                "automated_tasks_category_id": "cat-1",
                "n1_increase": {
                    "schedules": schedules,
                    "payload_chunks": [],
                    "summary_files": {
                        "excel": base64.b64encode(b"excel").decode("ascii"),
                        "pdf": base64.b64encode(b"pdf").decode("ascii"),
                    },
                },
            }
        }
    )

    webhook = {
        "eventType": "TaskStatusChanged",
        "task": {"status": "Completed"},
    }

    n1_increase.handle_n1_increase_automation(
        account_id="acct-1",
        api_headers={"Authorization": "Bearer token"},
        gl_mapping={},
        webhook=webhook,
        firestore_client=firestore,
        buildium_api=api,
    )

    assert len(api.updated_leases) == 2
    assert any(call["lease_id"] == "lease-1" for call in api.updated_leases)
    assert len(api.extended_leases) == 1
    assert api.extended_leases[0]["lease_id"] == "lease-2"

    assert len(api.uploaded_documents) == 2

    expected_strings = {
        "lease-1": [
            "Residents of Unit 101",
            "Property One",
            "101 - Property One",
            "$1236.00",
            "$36.00",
            "3.00%",
            "2024-09-01",
        ],
        "lease-2": [
            "Residents of Unit 201",
            "Property Two",
            "201 - Property Two",
            "$1537.50",
            "$37.50",
            "2.50%",
            "2024-09-01",
        ],
    }

    for upload in api.uploaded_documents:
        lease_id = upload["lease_id"]
        reader = _load_pdf_reader(upload["content"])
        assert len(reader.pages) == 2
        stream_text = _collect_pdf_stream_text(reader)
        for expected_value in expected_strings[lease_id]:
            assert _pdf_stream_pattern(expected_value) in stream_text

    tasks_by_property = defaultdict(list)
    for task in api.created_tasks:
        tasks_by_property[task["name"]].append(task)
    assert any("Property One" in name for name in tasks_by_property)
    assert any("Property Two" in name for name in tasks_by_property)

    assert len(api.presign_requests) == 2
    assert {entry["filename"] for entry in api.presign_requests} == {
        "N1 Summary.xlsx",
        "N1 Summary.pdf",
    }
    assert {upload["content"] for upload in api.presigned_uploads} == {b"excel", b"pdf"}

    document = firestore.collection_instance.document("acct-1")
    n1_block = document.data["n1_increase"]
    assert n1_block["forms_uploaded"] == 2
    assert "summary_uploads" in n1_block
    assert {
        entry["filename"] for entry in n1_block["summary_uploads"]
    } == {"N1 Summary.xlsx", "N1 Summary.pdf"}

    property_tasks = n1_block.get("property_tasks") or {}
    assert property_tasks["prop-1"]["status"] == "created"
    assert property_tasks["prop-2"]["status"] == "created"


def test_handle_n1_completion_creates_lease_renewals() -> None:
    api = FakeBuildiumAPI()
    schedule = {
        "lease_id": "lease-1",
        "property_id": "prop-1",
        "unit_id": "unit-1",
        "property_name": "Property One",
        "unit_name": "101",
        "current_rent": "1200.00",
        "new_rent": "1236.00",
        "increase_rate": "0.03",
        "increase_rate_percent": "3.00%",
        "increase_amount": "36.00",
        "effective_date": "2024-09-01",
        "is_extended": False,
        "extension_end_date": None,
    }

    payload_entries = [
        {
            "schedule": schedule,
            "lease": {"id": "lease-1", "effective_date": "2024-09-01"},
        }
    ]
    chunks = n1_data_module.build_encrypted_chunks(
        payload_entries, max_bytes=1024, encryption_secret=n1_data_module.ENCRYPTION_SECRET
    )

    firestore = FakeFirestore(
        initial_docs={
            "acct-1": {
                "n1_increase": {
                    "schedules": [schedule],
                    "payload_chunks": chunks,
                    "lease_renewals": {
                        "lease-1": {
                            "startDate": "2024-09-01",
                            "endDate": "2025-08-31",
                        }
                    },
                }
            }
        }
    )

    webhook = {"eventType": "TaskStatusChanged", "task": {"status": "Completed"}}

    n1_increase.handle_n1_increase_automation(
        account_id="acct-1",
        api_headers={"Authorization": "Bearer token"},
        gl_mapping={},
        webhook=webhook,
        firestore_client=firestore,
        buildium_api=api,
    )

    assert len(api.lease_renewals) == 1
    renewal = api.lease_renewals[0]
    assert renewal["lease_id"] == "lease-1"
    payload = renewal["payload"]
    assert payload["leaseId"] == "lease-1"
    assert payload["startDate"] == "2024-09-01"
    assert payload["endDate"] == "2025-08-31"
    assert float(payload["rentAmount"]) == 1236.0


def test_handle_n1_completion_skips_ignored_leases() -> None:
    api = FakeBuildiumAPI()
    schedules = [
        {
            "lease_id": "lease-1",
            "property_id": "prop-1",
            "unit_id": "unit-1",
            "property_name": "Property One",
            "unit_name": "101",
            "current_rent": "1200.00",
            "new_rent": "1236.00",
            "increase_rate": "0.03",
            "increase_rate_percent": "3.00%",
            "increase_amount": "36.00",
            "effective_date": "2024-09-01",
            "is_extended": False,
            "extension_end_date": None,
        },
        {
            "lease_id": "lease-2",
            "property_id": "prop-2",
            "unit_id": "unit-2",
            "property_name": "Property Two",
            "unit_name": "201",
            "current_rent": "1500.00",
            "new_rent": "1537.50",
            "increase_rate": "0.025",
            "increase_rate_percent": "2.50%",
            "increase_amount": "37.50",
            "effective_date": "2024-09-01",
            "is_extended": False,
            "extension_end_date": None,
        },
    ]

    firestore = FakeFirestore(
        initial_docs={
            "acct-1": {
                "n1_increase": {
                    "schedules": schedules,
                    "payload_chunks": [],
                    "ignored_leases": ["lease-2"],
                }
            }
        }
    )

    webhook = {"eventType": "TaskStatusChanged", "task": {"status": "Completed"}}

    n1_increase.handle_n1_increase_automation(
        account_id="acct-1",
        api_headers={"Authorization": "Bearer token"},
        gl_mapping={},
        webhook=webhook,
        firestore_client=firestore,
        buildium_api=api,
    )

    assert len(api.updated_leases) == 1
    assert api.updated_leases[0]["lease_id"] == "lease-1"
    assert all(call["lease_id"] != "lease-2" for call in api.updated_leases)
    assert len(api.uploaded_documents) == 1
    assert api.uploaded_documents[0]["lease_id"] == "lease-1"

    document = firestore.collection_instance.document("acct-1")
    n1_block = document.data["n1_increase"]
    assert n1_block["forms_uploaded"] == 1
    assert "lease-2" in n1_block["ignored_leases"]


def test_handle_n1_completion_uploads_summary_documents() -> None:
    api = FakeBuildiumAPI()
    schedule = {
        "lease_id": "lease-1",
        "property_id": "prop-1",
        "unit_id": "unit-1",
        "property_name": "Property One",
        "unit_name": "101",
        "current_rent": "1200.00",
        "new_rent": "1236.00",
        "increase_rate": "0.03",
        "increase_rate_percent": "3.00%",
        "increase_amount": "36.00",
        "effective_date": "2024-09-01",
        "is_extended": False,
        "extension_end_date": None,
    }

    firestore = FakeFirestore(
        initial_docs={
            "acct-1": {
                "n1_increase": {
                    "schedules": [schedule],
                    "payload_chunks": [],
                    "summary_files": {
                        "custom": base64.b64encode(b"binary").decode("ascii"),
                    },
                    "property_tasks": {"prop-1": {"task_id": "task-5"}},
                }
            }
        }
    )

    webhook = {"eventType": "TaskStatusChanged", "task": {"status": "Completed"}}

    n1_increase.handle_n1_increase_automation(
        account_id="acct-1",
        api_headers={"Authorization": "Bearer token"},
        gl_mapping={},
        webhook=webhook,
        firestore_client=firestore,
        buildium_api=api,
    )

    assert api.presign_requests[0]["filename"] == "N1 Summary - custom.bin"
    assert api.presign_requests[0]["metadata"]["label"] == "custom"
    assert api.presigned_uploads[0]["content"] == b"binary"
    assert len(api.task_comments) == 1
    assert api.task_comments[0]["task_id"] == "task-5"
