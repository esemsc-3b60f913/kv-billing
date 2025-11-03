from pydantic import BaseModel, Field, field_validator, ValidationError
from typing import List, Optional, Literal
from datetime import date

class Diagnosis(BaseModel):
    icd10_code: str = Field(..., description="ICD-10-GM code")
    description: Optional[str] = ""
    is_primary: bool = True

    @field_validator("icd10_code")
    @classmethod
    def upper_strip(cls, v: str) -> str:
        return v.strip().upper()

class Zusatzangaben(BaseModel):
    arzt_zusatz: Optional[str] = None
    dauer_minuten: Optional[int] = None
    anzahl: Optional[int] = None
    sonstiges: Optional[str] = None

class EBMCode(BaseModel):
    code: str
    reasoning: Optional[str] = ""
    zusatzangaben: Optional[Zusatzangaben] = Zusatzangaben()

    @field_validator("code")
    @classmethod
    def code_strip(cls, v: str) -> str:
        return v.strip()

class EncounterMetadata(BaseModel):
    quarter: str
    kv_region: str
    is_valid_for_kv: bool = True
    validation_notes: Optional[str] = ""

class ExtractionPayload(BaseModel):
    doctor_note_text: str
    date: date
    kv_region: str
    specialty: str
    patient_age: int
    insurance_type: Literal["GKV","PKV","BG","OTHER"] = "GKV"

class ExtractionResult(BaseModel):
    diagnoses: List[Diagnosis] = Field(default_factory=list)
    ebm_codes: List[EBMCode] = Field(default_factory=list)
    encounter_metadata: EncounterMetadata

class ValidationResult(BaseModel):
    ok: bool
    errors: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)

class KvdtExportRequest(BaseModel):
    practice: dict  # id, name, iknr, lanr etc. kept loose for MVP
    patient: dict   # id, name, birthdate
    encounters: List[ExtractionResult]

class KvdtExportResponse(BaseModel):
    ok: bool
    errors: List[str] = Field(default_factory=list)
    content: str = Field(default="", description="Fixed width KVDT text content")
