"""Utilities for rendering N1 rent increase notices from templates."""

from __future__ import annotations

from decimal import Decimal, InvalidOperation
from io import BytesIO
from pathlib import Path
from typing import Any, Dict, Mapping, MutableMapping, Optional, Sequence, Tuple

from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import BooleanObject, IndirectObject, NameObject
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen import canvas

N1_TEMPLATE_PATH = (
    Path(__file__).resolve().parent.parent / "Notice_Templates" / "N1 Template.pdf"
)

_FieldRect = Tuple[float, float, float, float]
_FieldPosition = Tuple[int, _FieldRect]

_DRAWN_FIELDS: Sequence[str] = (
    "To_TenantName[0]",
    "From_LandlordName[0]",
    "RentUnitAddress[0]",
    "StartDate[0]",
    "RentIncAmount1[0]",
    "RentIncAmount2[0]",
    "RentIncPercent[0]",
)


def create_n1_notice_pdf(
    schedule: Mapping[str, Any],
    *,
    lease: Optional[Mapping[str, Any]] = None,
    template_path: Optional[Path] = None,
) -> bytes:
    """Render a completed N1 notice PDF for the supplied schedule."""

    path = template_path or N1_TEMPLATE_PATH
    reader = PdfReader(str(path))
    if reader.is_encrypted:
        reader.decrypt("")

    field_values = _build_field_values(schedule, lease)
    positions = _collect_field_positions(reader, _DRAWN_FIELDS)
    overlay_reader = _build_overlay(reader, positions, field_values)

    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    acro_form = reader.trailer["/Root"].get("/AcroForm")
    if acro_form is not None:
        if isinstance(acro_form, IndirectObject):
            acro_form_obj = acro_form.get_object()
        else:
            acro_form_obj = acro_form
        writer._root_object.update(  # type: ignore[attr-defined]
            {NameObject("/AcroForm"): writer._add_object(acro_form_obj)}
        )

    for page in writer.pages:
        writer.update_page_form_field_values(page, field_values)

    _ensure_need_appearances(writer)

    for index, page in enumerate(writer.pages):
        if index < len(overlay_reader.pages):
            overlay_page = overlay_reader.pages[index]
            page.merge_page(overlay_page)

    buffer = BytesIO()
    writer.write(buffer)
    return buffer.getvalue()


def _ensure_need_appearances(writer: PdfWriter) -> None:
    form = writer._root_object.get(NameObject("/AcroForm"))  # type: ignore[attr-defined]
    if form is None:
        return
    if isinstance(form, IndirectObject):
        form = form.get_object()
    if not isinstance(form, MutableMapping):
        return
    form[NameObject("/NeedAppearances")] = BooleanObject(True)


def _collect_field_positions(
    reader: PdfReader, field_names: Sequence[str]
) -> Dict[str, _FieldPosition]:
    positions: Dict[str, _FieldPosition] = {}
    targets = set(field_names)
    for page_index, page in enumerate(reader.pages):
        annots_ref = page.get("/Annots")
        if not annots_ref:
            continue
        annots = (
            annots_ref.get_object()
            if hasattr(annots_ref, "get_object")
            else annots_ref
        )
        for annot_ref in annots:
            annot = annot_ref.get_object()
            name = annot.get("/T")
            if name in targets:
                rect = annot.get("/Rect")
                if rect:
                    positions[name] = (
                        page_index,
                        tuple(float(value) for value in rect),
                    )
    return positions


def _build_overlay(
    reader: PdfReader,
    positions: Mapping[str, _FieldPosition],
    field_values: Mapping[str, str],
) -> PdfReader:
    width = float(reader.pages[0].mediabox.width)
    height = float(reader.pages[0].mediabox.height)

    buffer = BytesIO()
    pdf_canvas = canvas.Canvas(buffer, pagesize=(width, height))
    pdf_canvas.setFont("Helvetica", 10)

    page_count = len(reader.pages)
    for page_index in range(page_count):
        for name, (target_page, rect) in positions.items():
            if target_page != page_index:
                continue
            value = field_values.get(name)
            if not value:
                continue
            _draw_text(pdf_canvas, value, rect)
        if page_index != page_count - 1:
            pdf_canvas.showPage()
            pdf_canvas.setFont("Helvetica", 10)

    pdf_canvas.save()
    buffer.seek(0)
    return PdfReader(buffer)


def _draw_text(pdf_canvas: canvas.Canvas, value: str, rect: _FieldRect) -> None:
    x1, y1, x2, y2 = rect
    width = x2 - x1
    lines = simpleSplit(value, "Helvetica", 10, width)
    y = y2 - 10
    for line in lines:
        pdf_canvas.drawString(x1 + 2, y, line)
        y -= 12
        if y < y1:
            break


def _build_field_values(
    schedule: Mapping[str, Any],
    lease: Optional[Mapping[str, Any]],
) -> Dict[str, str]:
    property_name = _clean(schedule.get("property_name"))
    unit_name = _clean(schedule.get("unit_name"))
    tenant_names = _format_tenant_names(lease, unit_name)
    increase_amount = _format_currency(schedule.get("increase_amount"))
    new_rent = _format_currency(schedule.get("new_rent"))
    percent = _format_percent(schedule.get("increase_rate_percent"))
    start_date = _clean(schedule.get("effective_date"))

    values: Dict[str, str] = {
        "To_TenantName[0]": tenant_names,
        "From_LandlordName[0]": property_name or "Landlord",
        "RentUnitAddress[0]": _compose_unit_address(unit_name, property_name),
        "StartDate[0]": start_date,
        "RentIncAmount1[0]": new_rent,
        "RentIncAmount2[0]": increase_amount,
        "RentIncPercent[0]": percent,
    }
    notice_value = tenant_names or values["RentUnitAddress[0]"]
    values["Notice_Name_And_Address_1[0]"] = notice_value
    return values


def _format_tenant_names(
    lease: Optional[Mapping[str, Any]], unit_name: str
) -> str:
    if isinstance(lease, Mapping):
        residents = lease.get("residents")
        if isinstance(residents, Sequence) and not isinstance(residents, (str, bytes)):
            names = [
                _clean(resident)
                for resident in residents
                if _clean(resident)
            ]
            if names:
                return ", ".join(names)
    if unit_name:
        return f"Residents of Unit {unit_name}"
    return "Residents"


def _compose_unit_address(unit_name: str, property_name: str) -> str:
    parts = [part for part in (unit_name, property_name) if part]
    if parts:
        return " - ".join(parts)
    return property_name or unit_name or ""


def _format_percent(value: Any) -> str:
    text = _clean(value)
    if not text:
        return ""
    if "%" in text:
        return text
    try:
        decimal_value = Decimal(text)
    except (InvalidOperation, ValueError):
        return text
    percentage = decimal_value * Decimal("100")
    return f"{percentage.quantize(Decimal('0.01'))}%"


def _format_currency(value: Any) -> str:
    decimal_value = _to_decimal(value)
    return f"${decimal_value.quantize(Decimal('0.01'))}"


def _to_decimal(value: Any) -> Decimal:
    try:
        if isinstance(value, Decimal):
            return value
        if value is None:
            return Decimal("0")
        return Decimal(str(value))
    except (InvalidOperation, ValueError):
        return Decimal("0")


def _clean(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    return text


__all__ = [
    "N1_TEMPLATE_PATH",
    "create_n1_notice_pdf",
]
