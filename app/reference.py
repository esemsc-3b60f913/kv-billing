# Tiny placeholder reference tables.
# Replace with real EBM and ICD loaders pinned by quarter.

EBM_CODES = {
    # General Practice
    "03220": {"short_text": "Hausärztliche Beratung bis 10 Min", "requires_additional_data": False, "additional_data_spec": []},
    "03230": {"short_text": "Hausärztliche Beratung ab 10 Min", "requires_additional_data": True, "additional_data_spec": ["dauer_minuten"]},
    "03360": {"short_text": "Blutentnahme", "requires_additional_data": False, "additional_data_spec": []},
    "03362": {"short_text": "Urin-/Schnelltests", "requires_additional_data": False, "additional_data_spec": []},
    "01435": {"short_text": "Problemorientiertes ärztliches Gespräch", "requires_additional_data": True, "additional_data_spec": ["dauer_minuten"]},
    "01732": {"short_text": "Krebsfrüherkennung Männer", "requires_additional_data": False, "additional_data_spec": []},
    "01745": {"short_text": "Impfleistung", "requires_additional_data": False, "additional_data_spec": []},
    
    # Orthopedics
    "03245": {"short_text": "Orthopädische Untersuchung", "requires_additional_data": False, "additional_data_spec": []},
    "03246": {"short_text": "Orthopädische Untersuchung mit Befundung", "requires_additional_data": False, "additional_data_spec": []},
    "35200": {"short_text": "Injektion an Gelenken oder Sehnen", "requires_additional_data": False, "additional_data_spec": []},
    "35700": {"short_text": "Entfernung von oberflächlichen Fremdkörpern", "requires_additional_data": False, "additional_data_spec": []},
    "35900": {"short_text": "Gelenkpunktion diagnostisch", "requires_additional_data": False, "additional_data_spec": []},
    "35910": {"short_text": "Gelenkpunktion therapeutisch", "requires_additional_data": False, "additional_data_spec": []},
    "01760": {"short_text": "Röntgenuntersuchung Extremitäten", "requires_additional_data": False, "additional_data_spec": []},
    "01762": {"short_text": "Röntgenuntersuchung Wirbelsäule", "requires_additional_data": False, "additional_data_spec": []},
    
    # Surgery
    "35100": {"short_text": "Kleiner chirurgischer Eingriff", "requires_additional_data": False, "additional_data_spec": []},
    "35101": {"short_text": "Wundversorgung", "requires_additional_data": False, "additional_data_spec": []},
    "35102": {"short_text": "Wundversorgung kompliziert", "requires_additional_data": False, "additional_data_spec": []},
    "35110": {"short_text": "Entfernung von Nägeln", "requires_additional_data": False, "additional_data_spec": []},
    "35300": {"short_text": "Exzision von Hautläsionen", "requires_additional_data": False, "additional_data_spec": []},
    "35310": {"short_text": "Exzision von Hautläsionen größer 2cm", "requires_additional_data": False, "additional_data_spec": []},
    "03430": {"short_text": "Chirurgische Konsultation", "requires_additional_data": False, "additional_data_spec": []},
    "03440": {"short_text": "Chirurgische Konsultation mit Befundung", "requires_additional_data": False, "additional_data_spec": []},
}

# ICD-10-GM codes for demo (General Medicine, Orthopedics, Surgery)
ICD10_CODES = {
    # General Medicine / Respiratory
    "J02.9": "Akute Pharyngitis, nicht näher bezeichnet",
    "J06.9": "Akute Infektion der oberen Atemwege, nicht näher bezeichnet",
    "R50.9": "Fieber, nicht näher bezeichnet",
    "R51": "Kopfschmerz",
    
    # Orthopedics - Spine
    "M54.5": "Kreuzschmerz",
    "M54.4": "Lumbago mit Ischias",
    "M54.3": "Ischialgie",
    "M54.2": "Zervikalgie",
    "M54.1": "Radikulopathie",
    "M51.2": "Sonstige Bandscheibenverschiebung",
    
    # Orthopedics - Shoulder
    "M75.0": "Adhäsive Entzündung der Schultergelenkkapsel",
    "M75.1": "Läsionen der Rotatorenmanschette",
    "M75.2": "Bizepssehnenentzündung",
    "M75.3": "Kalzifizierende Tendinitis der Schulter",
    "M25.5": "Gelenkschmerz",
    
    # Orthopedics - Knee
    "M23.2": "Meniskusschädigung durch alten Riss oder Alteration",
    "M17.1": "Sonstige primäre Gonarthrose",
    "M17.2": "Posttraumatische Gonarthrose",
    "M25.5": "Gelenkschmerz",
    "S83.5": "Zerrung und Verstauchung des Kniegelenks",
    
    # Orthopedics - Hand/Wrist
    "M79.3": "Pannikulitis",
    "M25.6": "Steifigkeit des Gelenkes",
    "S52.5": "Distale Fraktur des Radius",
    "M77.1": "Epicondylitis radialis humeri",
    
    # Orthopedics - Foot/Ankle
    "M79.3": "Pannikulitis",
    "M25.5": "Gelenkschmerz",
    "M77.9": "Enthesopathie, nicht näher bezeichnet",
    "M20.1": "Hallux valgus",
    
    # Orthopedics - General
    "M79.3": "Sonstige Krankheiten des Weichteilgewebes",
    "M79.4": "Hypertrophie der Fettgewebes",
    "M25.5": "Sonstige Gelenkkrankheiten",
    
    # Surgery - Hernias
    "K40.9": "Leistenhernie ohne Einklemmung",
    "K41.9": "Femoralhernie ohne Einklemmung",
    "K42.9": "Nabelhernie",
    
    # Surgery - Appendicitis
    "K35.9": "Akute Appendizitis",
    "K37": "Appendizitis, nicht näher bezeichnet",
    
    # Surgery - Wounds
    "T14.0": "Oberflächliche Verletzung an einer nicht näher bezeichneten Körperregion",
    "T14.8": "Sonstige Verletzungen an einer nicht näher bezeichneten Körperregion",
    "S01.9": "Offene Wunde des Kopfes",
    "S61.9": "Offene Wunde des Handgelenkes und der Hand",
    
    # Surgery - Skin lesions
    "D22.9": "Melanozytärer Nävus",
    "D23.9": "Sonstige gutartige Neubildungen der Haut",
    "L72.9": "Follikuläre Zyste der Haut",
    "L91.0": "Hypertrophe Narbe",
    "L60.0": "Eingewachsener Nagel",
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
