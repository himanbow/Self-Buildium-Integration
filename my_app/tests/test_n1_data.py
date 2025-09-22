
from __future__ import annotations

import base64
from typing import Any, Dict, List, Mapping, Optional, Sequence

import importlib

n1_data = importlib.import_module("my_app.tasks.n1_data")


class DataFakeAPI:
    def __init__(self) -> None:
        self.leases: List[Mapping[str, Any]] = []
        self.market_rent: Dict[tuple[str, str], Mapping[str, Any]] = {}
        self.lease_notes: Dict[str, List[Mapping[str, Any]]] = {}
        self.building_notes: Dict[str, List[Mapping[str, Any]]] = {}
        self.recurring_transactions: Dict[str, List[Mapping[str, Any]]] = {}
        self.agi_summaries: Dict[str, Mapping[str, Any]] = {}
        self.presigned_urls: Dict[str, Mapping[str, Any]] = {}
        self.downloaded_files: Dict[str, bytes] = {}

    def list_eligible_leases(self) -> Sequence[Mapping[str, Any]]:
        return list(self.leases)

    def get_market_rent(self, *, property_id: str, unit_id: str) -> Optional[Mapping[str, Any]]:
        return self.market_rent.get((property_id, unit_id))

    def get_ontario_increase_rates(self) -> Mapping[str, Any]:
        return {"default": "0.03"}

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


def _base_lease(lease_id: str, property_id: str, unit_id: str, *, name: str = "") -> Mapping[str, Any]:
    return {
        "leaseId": lease_id,
        "property": {"id": property_id, "name": name or property_id.title()},
        "unit": {"id": unit_id, "name": unit_id.upper()},
        "rent": {"amount": "1000"},
        "increaseEffectiveDate": "2024-09-01",
        "residents": [{"fullName": "Resident One"}],
    }


def test_prepare_data_filters_blocked_leases() -> None:
    api = DataFakeAPI()
    api.leases = [
        _base_lease("lease-1", "prop-1", "unit-1", name="Eligible"),
        _base_lease("lease-2", "prop-2", "unit-2", name="Blocked"),
    ]
    api.recurring_transactions = {
        "lease-1": [{"amount": "1000", "glAccountNumber": "4000"}],
        "lease-2": [{"amount": "1000", "glAccountNumber": "4000"}],
    }
    api.lease_notes["lease-2"] = [{"body": "Do not increase"}]

    prepared = n1_data.prepare_n1_data(
        api,
        rates={"default": "0.01"},
        gl_mapping={"4000": "Rent"},
        max_payload_bytes=4096,
    )

    assert len(prepared.schedules) == 1
    assert prepared.schedules[0]["lease_id"] == "lease-1"
    assert prepared.excluded == [{"lease_id": "lease-2", "reason": "blocked:lease_note"}]


def test_prepare_data_applies_agi_adjustment() -> None:
    api = DataFakeAPI()
    api.leases = [_base_lease("lease-1", "prop-1", "unit-1", name="AGI")]
    api.recurring_transactions["lease-1"] = [{"amount": "1000", "glAccountNumber": "4000"}]
    api.agi_summaries["lease-1"] = {
        "monthlyAmount": "25",
        "percent": "0.01",
        "documentId": "doc-1",
    }
    api.presigned_urls["doc-1"] = {"url": "https://example.com/doc-1"}
    api.downloaded_files["https://example.com/doc-1"] = b"attachment"

    prepared = n1_data.prepare_n1_data(
        api,
        rates={"default": "0.02"},
        gl_mapping={"4000": "Rent"},
        max_payload_bytes=4096,
    )

    schedule = prepared.schedules[0]
    assert schedule["current_rent"] == "1000.00"
    assert schedule["new_rent"] == "1055.00"
    assert schedule["agi_amount"] == "25.00"
    assert schedule["agi_percent"] == "3.50%"

    entry = prepared.payload_entries[0]
    assert entry["agi"]["document"]["content"] == base64.b64encode(b"attachment").decode("ascii")


def test_prepare_data_generates_encrypted_payload() -> None:
    api = DataFakeAPI()
    api.leases = [_base_lease("lease-1", "prop-1", "unit-1")]
    api.recurring_transactions["lease-1"] = [{"amount": "950", "glAccountNumber": "4000"}]

    prepared = n1_data.prepare_n1_data(
        api,
        rates={"default": "0.02"},
        gl_mapping={"4000": "Rent"},
        max_payload_bytes=256,
    )

    assert prepared.payload_chunks
    chunk = prepared.payload_chunks[0]
    assert chunk["encryption"]["algorithm"] == "xor+zlib"

    decoded = n1_data.decode_payload_chunk(chunk)
    assert decoded[0]["schedule"]["lease_id"] == "lease-1"
    assert decoded[0]["schedule"]["new_rent"] != ""
    assert decoded[0]["recurring_transactions"][0]["is_rent"] is True
