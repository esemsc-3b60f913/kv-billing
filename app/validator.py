from typing import List
from .models import ExtractionResult, ValidationResult, EBMCode
from .reference import EBM_CODES, ICD10_CODES

def validate_icd_codes(er: ExtractionResult, errors: List[str], warnings: List[str]) -> None:
    if not er.diagnoses:
        warnings.append("No diagnoses provided")
        return
    seen_primary = False
    for d in er.diagnoses[:3]:
        if d.icd10_code not in ICD10_CODES:
            errors.append(f"Unknown ICD code: {d.icd10_code}")
        if d.is_primary:
            seen_primary = True
    if not seen_primary:
        errors.append("No primary diagnosis marked")

def validate_ebm_codes(er: ExtractionResult, errors: List[str], warnings: List[str]) -> None:
    if not er.ebm_codes:
        warnings.append("No EBM codes provided")
        return
    for e in er.ebm_codes[:5]:
        if e.code not in EBM_CODES:
            errors.append(f"Unknown EBM code: {e.code}")
            continue
        spec = EBM_CODES[e.code]
        if spec.get("requires_additional_data"):
            needed = set(spec.get("additional_data_spec", []))
            got = set()
            if e.zusatzangaben:
                if e.zusatzangaben.dauer_minuten is not None:
                    got.add("dauer_minuten")
            missing = needed - got
            if missing:
                errors.append(f"Missing Zusatzangaben for {e.code}: {', '.join(sorted(missing))}")

def validate_encounter(er: ExtractionResult) -> ValidationResult:
    errors: List[str] = []
    warnings: List[str] = []
    validate_icd_codes(er, errors, warnings)
    validate_ebm_codes(er, errors, warnings)
    # Minimal metadata checks
    if not er.encounter_metadata.kv_region:
        errors.append("kv_region missing")
    if not er.encounter_metadata.quarter:
        errors.append("quarter missing")
    ok = len(errors) == 0
    return ValidationResult(ok=ok, errors=errors, warnings=warnings)
