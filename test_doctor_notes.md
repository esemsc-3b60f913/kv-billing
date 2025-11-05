# Test Doctor Notes

These three doctor notes are designed to work with your current ICD-10 and EBM code reference setup.

---

## Note 1: Acute Pharyngitis

**Patient:** Max Mustermann, 45 years old  
**Date:** 2025-10-28  
**KV Region:** Berlin  
**Specialty:** General Medicine

```
The patient presents with a sore throat and difficulty swallowing for two days. 
No fever, general condition slightly reduced. 
Throat reddened, tonsils moderately swollen, no coatings.
Clinical diagnosis: Acute pharyngitis.

Services performed:
- Medical history and physical examination
- Counseling for symptomatic treatment
- Consultation duration: 15 minutes

Recommendation: Symptomatic therapy with gargling solutions, paracetamol if needed. 
Return if symptoms persist or worsen.
```

**Expected Codes:**
- ICD-10: J02.9 (Acute pharyngitis, unspecified)
- EBM: 03230 (General practitioner consultation ≥10 min)  
  `duration_minutes: 15`

---

## Note 2: Lower Back Pain

**Patient:** Anna Schmidt, 52 years old  
**Date:** 2025-11-05  
**KV Region:** Bavaria  
**Specialty:** General Medicine

```
The patient complains of acute lower back pain in the lumbar region for three days. 
Pain worsens with movement, improves at rest. No radiation into the legs, 
no neurological deficits.

History revealed: lifting a heavy box three days ago, followed by sudden onset of pain.

Examination performed: inspection, palpation, range of motion testing. 
Advised on back-friendly behavior, recommended physical therapy.

Consultation lasted 12 minutes.
```

**Expected Codes:**
- ICD-10: M54.5 (Low back pain)
- EBM: 03230 (General practitioner consultation ≥10 min)  
  `duration_minutes: 12`

---

## Note 3: Fever and Headache

**Patient:** Thomas Weber, 38 years old  
**Date:** 2025-11-10  
**KV Region:** Berlin  
**Specialty:** General Medicine

```
The patient reports fever up to 38.5°C and severe headache since this morning. 
General condition reduced, no cough, no sore throat. 
Physical exam: tympanic temperature 38.2°C, otherwise normal findings.

Suspected diagnosis: Viral upper respiratory tract infection.

Treatment: Symptomatic therapy with paracetamol, bed rest, sufficient fluid intake.
Short consultation of 8 minutes.
```

**Expected Codes:**
- ICD-10: R50.9 (Fever, unspecified), R51 (Headache), or J06.9 (Acute upper respiratory infection)
- EBM: 03220 (General practitioner consultation ≤10 min)  
  `duration_minutes: 8`

---

## Testing Instructions

1. Copy each note into the **Treatment Documentation** field  
2. Fill in the corresponding patient name, date, and other form fields  
3. Submit and verify that:
   - ICD codes are correctly extracted  
   - EBM codes match the consultation duration  
   - Patient is saved in the stored patient list  
4. Test the quarterly export by processing multiple notes within the same quarter

---

## Tips for Best Results

- The LLM should extract codes based on mentioned symptoms/conditions  
- Duration keywords like **“15 minutes”** or **“12 minutes”** should trigger **EBM 03230** with `duration_minutes`  
- Duration under 10 minutes should trigger **EBM 03220**  
- Multiple symptoms may yield multiple ICD codes
