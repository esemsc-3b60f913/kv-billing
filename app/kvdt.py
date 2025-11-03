from typing import List
from .models import ExtractionResult, KvdtExportRequest, KvdtExportResponse
from .reference import KVDT_DEFS
from .validator import validate_encounter

def _fmt(field_name: str, value, length: int, pad_char: str, align: str) -> str:
    s = "" if value is None else str(value)
    if align == "right":
        return s.ljust(length)[:length]
    else:
        return s.rjust(length, pad_char)[-length:]

def _write_record(record_type: str, data: dict) -> str:
    parts = []
    for field_name, length, pad_char, align in KVDT_DEFS[record_type]:
        val = data.get(field_name, "")
        parts.append(_fmt(field_name, val, length, pad_char, align))
    return "".join(parts)

def export_kvdt(req: KvdtExportRequest) -> KvdtExportResponse:
    lines: List[str] = []
    errors: List[str] = []

    quarter = ""
    if req.encounters:
        quarter = req.encounters[0].encounter_metadata.quarter

    # 6000 header
    lines.append(_write_record("6000", {
        "record_type": "6000",
        "version": "MVP01",
        "practice_id": str(req.practice.get("id","")),
        "quarter": quarter,
    }))

    # 6100 practice
    lines.append(_write_record("6100", {
        "record_type": "6100",
        "iknr": req.practice.get("iknr",""),
        "lanr": req.practice.get("lanr",""),
        "name": req.practice.get("name",""),
    }))

    # 6200 + 6300 per encounter
    for er in req.encounters:
        vr = validate_encounter(er)
        if not vr.ok:
            errors.extend(vr.errors)
            continue
        primary_icd = ""
        for d in er.diagnoses:
            if d.is_primary:
                primary_icd = d.icd10_code
                break

        lines.append(_write_record("6200", {
            "record_type": "6200",
            "patient_id": str(req.patient.get("id","")),
            "kv_region": er.encounter_metadata.kv_region,
            "primary_icd": primary_icd,
        }))

        for e in er.ebm_codes:
            dauer = 0
            if e.zusatzangaben and e.zusatzangaben.dauer_minuten is not None:
                dauer = int(e.zusatzangaben.dauer_minuten)
            lines.append(_write_record("6300", {
                "record_type": "6300",
                "ebm_code": e.code,
                "anzahl": 1,
                "dauer_minuten": dauer,
            }))

    # 9999 trailer
    lines.append(_write_record("9999", {
        "record_type": "9999",
        "record_count": len(lines) + 1,  # include trailer itself
    }))

    return KvdtExportResponse(ok=(len(errors)==0), errors=errors, content="\n".join(lines) + "\n")
