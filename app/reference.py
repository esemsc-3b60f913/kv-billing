# Tiny placeholder reference tables.
# Replace with real EBM and ICD loaders pinned by quarter.

EBM_CODES = {
    "03220": {"short_text": "Hausärztliche Beratung bis 10 Min", "requires_additional_data": False, "additional_data_spec": []},
    "03230": {"short_text": "Hausärztliche Beratung ab 10 Min", "requires_additional_data": True, "additional_data_spec": ["dauer_minuten"]},
    "03360": {"short_text": "Blutentnahme", "requires_additional_data": False, "additional_data_spec": []},
    "03362": {"short_text": "Urin-/Schnelltests", "requires_additional_data": False, "additional_data_spec": []},
    "01435": {"short_text": "Problemorientiertes ärztliches Gespräch", "requires_additional_data": True, "additional_data_spec": ["dauer_minuten"]},
    "01732": {"short_text": "Krebsfrüherkennung Männer", "requires_additional_data": False, "additional_data_spec": []},
    "01745": {"short_text": "Impfleistung", "requires_additional_data": False, "additional_data_spec": []},
    "35100": {"short_text": "Kleiner chirurgischer Eingriff", "requires_additional_data": False, "additional_data_spec": []},
}

# Very small ICD list for demo
ICD10_CODES = {
    "J02.9": "Akute Pharyngitis, nicht näher bezeichnet",
    "J06.9": "Akute Infektion der oberen Atemwege, nicht näher bezeichnet",
    "M54.5": "Kreuzschmerz",
    "R50.9": "Fieber, nicht näher bezeichnet",
    "R51": "Kopfschmerz",
}

# Minimal KVDT field definitions for a toy export
# Each tuple: (field_name, length, pad_char, align)
KVDT_DEFS = {
    "6000": [
        ("record_type", 4, " ", "right"),
        ("version", 5, " ", "right"),
        ("practice_id", 10, " ", "right"),
        ("quarter", 6, " ", "right"),
    ],
    "6100": [
        ("record_type", 4, " ", "right"),
        ("iknr", 9, " ", "right"),
        ("lanr", 9, " ", "right"),
        ("name", 30, " ", "right"),
    ],
    "6200": [
        ("record_type", 4, " ", "right"),
        ("patient_id", 12, " ", "right"),
        ("kv_region", 10, " ", "right"),
        ("primary_icd", 7, " ", "right"),
    ],
    "6300": [
        ("record_type", 4, " ", "right"),
        ("ebm_code", 5, " ", "right"),
        ("anzahl", 2, "0", "left"),
        ("dauer_minuten", 3, "0", "left"),
    ],
    "9999": [
        ("record_type", 4, " ", "right"),
        ("record_count", 6, "0", "left"),
    ],
}
