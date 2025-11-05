import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from .models import ExtractionPayload

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def make_prompt(p: ExtractionPayload) -> str:
    return f"""You are a medical billing assistant for outpatient doctors in Germany.
Your task is to read the doctor's encounter note and return ONLY structured data 
needed for KV billing (EBM + ICD-10-GM + Zusatzangaben if required).
Be precise and conservative: if uncertain, leave fields empty instead of guessing.
For EBM codes that require Zusatzangaben such as duration (e.g., 03230), always 
include "dauer_minuten" with the number of minutes documented in the note if available.

INPUT:
<<DOCTOR_NOTE>>
{p.doctor_note_text}

<<VISIT_METADATA>>
- Date: {p.date}
- KV Region: {p.kv_region}
- Specialty: {p.specialty}
- Patient age: {p.patient_age}
- Versicherungsart: {p.insurance_type}

REQUIRED OUTPUT FORMAT (JSON ONLY):

{{
  "diagnoses": [],
  "ebm_codes": [],
  "encounter_metadata": {{
    "quarter": "YYYYQn",
    "kv_region": "{p.kv_region}",
    "is_valid_for_kv": true,
    "validation_notes": ""
  }}
}}

Rules:
- Use only valid ICD-10-GM and EBM codes.
- Return valid JSON only.

EBM Code Selection Priority:
- For specialized consultations (orthopedics, surgery), prefer specialized consultation codes over general consultation codes:
  * Orthopedics: Use 03246 (Orthopedic examination with documentation) instead of 03230 (General consultation) when a comprehensive orthopedic examination was performed
  * Surgery: Use 03440 (Surgical consultation with documentation) instead of 03230 (General consultation) when a surgical consultation was performed
- Do NOT bill both a general consultation (03230) AND a specialized consultation (03246, 03440) - the specialized code includes the consultation component
- When multiple valid codes apply, select the most appropriate and lucrative combination that accurately reflects the services provided
- Additional procedures (injections, imaging, surgical procedures) can be billed separately alongside consultation codes
"""

def call_llm(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=600
        )
        text = response.choices[0].message.content.strip()
        print("🧠 Raw LLM output:", repr(text))  # 👈 log the exact raw output

        if not text:
            raise ValueError("LLM returned an empty response. Check API key or prompt.")

        json.loads(text)  # validate JSON
        return text

    except Exception as e:
        print("❌ OpenAI API call failed:", e)
        raise

    