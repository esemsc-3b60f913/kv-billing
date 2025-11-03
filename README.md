# KV Billing MVP

Minimal FastAPI MVP that:
- accepts doctor notes and visit metadata
- extracts suggested ICD and EBM codes via LLM or stub
- validates deterministically against reference tables
- emits a toy KVDT text file with fixed width records

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Endpoints
- POST /extract — run LLM or stub to produce structured codes
- POST /validate — deterministic checks on JSON payload
- POST /kvdt/export — generate fixed width KVDT text file
- GET /healthz — liveness

## Notes
- Reference tables are tiny placeholders in app/reference.py
- KVDT writer is table driven in app/kvdt.py with a minimal subset of records 6000 6100 6200 6300 9999
- Replace the stub LLM with a real provider in app/prompts.py -> call_llm()
