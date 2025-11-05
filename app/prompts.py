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
  "diagnoses": [
    {{
      "icd10_code": "M54.5",
      "description": "Kreuzschmerz",
      "is_primary": true
    }}
  ],
  "ebm_codes": [
    {{
      "code": "03230",
      "reasoning": "Consultation duration 15 minutes",
      "zusatzangaben": {{
        "dauer_minuten": 15
      }}
    }},
    {{
      "code": "01760",
      "reasoning": "X-ray examination performed"
    }},
    {{
      "code": "35200",
      "reasoning": "Therapeutic injection performed"
    }}
  ],
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
- For diagnoses, use field name "icd10_code" (not "icd10" or "code").
- Include "description" field for diagnoses if available.
- Set "is_primary": true for the primary diagnosis.
- IMPORTANT: Extract ALL procedures performed - if multiple procedures are documented (consultation + examination + imaging + injection + surgical procedure + wound care), list ALL corresponding EBM codes.
- Do NOT only extract the consultation code - also extract codes for examinations, imaging, injections, surgical procedures, wound care, etc. that are explicitly mentioned in the note.

EBM Code Selection Priority:
- For specialized consultations (orthopedics, surgery), prefer specialized consultation codes over general consultation codes:
  * Orthopedics: Use 03246 (Orthopedic examination with documentation) instead of 03230 (General consultation) when a comprehensive orthopedic examination was performed
  * Surgery: Use 03440 (Surgical consultation with documentation) instead of 03230 (General consultation) when a surgical consultation was performed
- Do NOT bill both a general consultation (03230) AND a specialized consultation (03246, 03440) - the specialized code includes the consultation component
- When multiple valid codes apply, select the most appropriate and lucrative combination that accurately reflects the services provided
- Additional procedures (injections, imaging, surgical procedures, wound care, excisions) MUST be billed separately alongside consultation codes
- Examples of procedures that should be separately billed:
  * Excision of skin lesions → 35300
  * Minor surgical procedures (including wound closure with sutures, hemostasis) → 35100
  * Complex wound care → 35102
  * Removal of foreign bodies → 35700
  * Joint injections → 35200
  * X-ray examinations → 01760, 01762
  * Joint punctures → 35900, 35910
- IMPORTANT: When a surgical procedure involves both excision AND wound closure with sutures, bill BOTH:
  * Excision → 35300
  * Wound closure/suturing → 35100 (Minor surgical procedure)
- Similarly, if a procedure involves multiple distinct steps (e.g., removal + closure, excision + hemostasis + closure), each distinct procedural step should be billed separately
"""

def call_llm(prompt: str) -> str:
    models_to_try = ["gpt-4o", "gpt-4o-mini"]  # Try GPT-4o first, fallback to mini
    
    for model in models_to_try:
        try:
            print(f"🤖 Attempting API call with model: {model}")
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=1000
            )
            text = response.choices[0].message.content.strip()
            print("🧠 Raw LLM output:", repr(text))  # 👈 log the exact raw output

            if not text:
                raise ValueError("LLM returned an empty response. Check API key or prompt.")

            json.loads(text)  # validate JSON
            print(f"✅ Successfully used model: {model}")
            return text

        except Exception as e:
            print(f"❌ Model {model} failed: {e}")
            if model == models_to_try[-1]:  # If this was the last model, raise the error
                raise ValueError(f"All models failed. Last error: {e}")
            # Otherwise, continue to next model
            continue
    
    raise ValueError("Failed to get response from any model")

    