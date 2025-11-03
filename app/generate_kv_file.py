import requests

export_payload = {
    "practice": {
        "id": "1234567890",
        "iknr": "123456789",
        "lanr": "123456789",
        "name": "Hausarztpraxis Müller"
    },
    "patient": {
        "id": "P001",
        "name": "Erika Mustermann",
        "birthdate": "1980-01-01"
    },
    "encounters": [
        {
            "diagnoses": [
                {
                    "icd10_code": "M54.5",
                    "description": "",
                    "is_primary": True
                }
            ],
            "ebm_codes": [
                {
                    "code": "03220",
                    "reasoning": "",
                    "zusatzangaben": {}
                }
            ],
            "encounter_metadata": {
                "quarter": "2025Q4",
                "kv_region": "Berlin",
                "is_valid_for_kv": True,
                "validation_notes": ""
            }
        }
    ]
}

# Call your local FastAPI backend
response = requests.post("http://127.0.0.1:8000/kvdt/export", json=export_payload)
response.raise_for_status()

data = response.json()

if data["ok"]:
    with open("abrechnung_2025Q4.dat", "w", encoding="utf-8") as f:
        f.write(data["content"])
    print("✅ KVDT file successfully saved as abrechnung_2025Q4.dat")
else:
    print("❌ Validation errors:", data["errors"])