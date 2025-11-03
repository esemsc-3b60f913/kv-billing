import json
import re
from fastapi import FastAPI, HTTPException
from datetime import datetime
from typing import Any, Dict
from fastapi.middleware.cors import CORSMiddleware

from .models import ExtractionPayload, ExtractionResult, ValidationResult, KvdtExportRequest, KvdtExportResponse
from .prompts import make_prompt, call_llm
from .validator import validate_encounter
from .kvdt import export_kvdt

app = FastAPI(title="KV Billing MVP", version="0.1.0")

# --- Enable CORS for ALL ORIGINS for debugging ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins temporarily for debug
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz")
def healthz() -> Dict[str, Any]:
    return {"ok": True, "ts": datetime.utcnow().isoformat()}

@app.post("/extract", response_model=ExtractionResult)
def extract_codes(payload: ExtractionPayload):
    prompt = make_prompt(payload)
    raw = call_llm(prompt)
    data = json.loads(raw)

    # --- Normalize diagnoses ---
    normalized_diagnoses = []
    for diag in data.get("diagnoses", []):
        if isinstance(diag, str):
            # Convert string diagnosis to dictionary format
            normalized_diag = {
                "icd10_code": diag,
                "is_primary": True
            }
        else:
            # Handle dictionary format
            normalized_diag = diag.copy()
            if "icd10_code" not in normalized_diag and "code" in normalized_diag:
                normalized_diag["icd10_code"] = normalized_diag.pop("code")
            if "is_primary" not in normalized_diag:
                normalized_diag["is_primary"] = True
        
        normalized_diagnoses.append(normalized_diag)
    
    data["diagnoses"] = normalized_diagnoses

    # --- Detect minutes from note ---
    detected_minutes = None
    match = re.search(r"(\d+)\s*(min|minute|minuten)", payload.doctor_note_text.lower())
    if match:
        detected_minutes = int(match.group(1))

    # --- Normalize EBM codes ---
    ebm_fixed = []
    for ebm in data.get("ebm_codes", []):
        if isinstance(ebm, str):
            ebm = {"code": ebm, "reasoning": "", "zusatzangaben": {}}

        ebm.setdefault("zusatzangaben", {})

        # Auto-fill dauer_minuten for 03230 if missing
        if ebm["code"] == "03230" and not ebm["zusatzangaben"].get("dauer_minuten"):
            if detected_minutes:
                ebm["zusatzangaben"]["dauer_minuten"] = detected_minutes
            else:
                ebm["zusatzangaben"]["dauer_minuten"] = 15  # default fallback

        ebm_fixed.append(ebm)

    data["ebm_codes"] = ebm_fixed

    # --- Validate against schema ---
    try:
        return ExtractionResult(**data)
    except Exception as e:
        print("❌ Validation failed:", e)
        raise HTTPException(status_code=400, detail=f"Schema error: {e}")

@app.post("/validate", response_model=ValidationResult)
def validate(er: ExtractionResult) -> ValidationResult:
    return validate_encounter(er)

@app.post("/kvdt/export", response_model=KvdtExportResponse)
def kvdt_export(req: KvdtExportRequest) -> KvdtExportResponse:
    return export_kvdt(req)