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
- Duration keywords like **"15 minutes"** or **"12 minutes"** should trigger **EBM 03230** with `duration_minutes`  
- Duration under 10 minutes should trigger **EBM 03220**  
- Multiple symptoms may yield multiple ICD codes

---

## Note 4: Complex Orthopedic Case - Rotator Cuff Injury with Injection

**Patient:** Dr. Michael Bauer, 58 years old  
**Date:** 2025-11-15  
**KV Region:** Hamburg  
**Specialty:** Orthopedics

```
The patient presents with persistent right shoulder pain for the past 6 weeks following a fall. 
Pain is localized to the anterior and lateral aspect of the shoulder, worse with overhead activities 
and at night. Clinical examination reveals positive Neer and Hawkins impingement signs, weakness 
in external rotation, and crepitus on active range of motion.

Findings:
- Limited active abduction to 90 degrees, passive abduction to 150 degrees
- Painful arc between 60-120 degrees
- Positive Jobe test for supraspinatus involvement
- Slight atrophy of the infraspinatus muscle

Diagnostic imaging: X-ray of the right shoulder performed showing signs of subacromial impingement 
and calcific deposits in the supraspinatus tendon. No evidence of fracture or dislocation.

Diagnosis: Rotator cuff lesion (M75.1) with subacromial impingement syndrome and calcific tendinitis.

Performed procedures:
1. Orthopedic examination with detailed assessment and documentation (03246)
2. X-ray examination of the right shoulder/upper extremity (01760)
3. Therapeutic injection of corticosteroid and local anesthetic into the subacromial space (35200)

Treatment plan: Continue with NSAIDs, physical therapy focusing on rotator cuff strengthening, 
and follow-up in 4 weeks. If symptoms persist, consider MRI for further evaluation.

Total consultation time: 25 minutes including examination, imaging review, and injection procedure.
```

**Expected Codes:**
- ICD-10: M75.1 (Lesions of rotator cuff), M75.3 (Calcific tendinitis of shoulder)
- EBM: 03246 (Orthopedic examination with documentation)
- EBM: 01760 (X-ray examination of extremities)
- EBM: 35200 (Injection at joints or tendons)

---

## Note 5: Complex Orthopedic Case - Meniscal Tear with Knee Pain

**Patient:** Sarah Müller, 34 years old  
**Date:** 2025-11-18  
**KV Region:** North Rhine-Westphalia  
**Specialty:** Orthopedics

```
The patient reports a twisting injury to her left knee while playing soccer 3 weeks ago. 
Since then, she experiences intermittent locking and catching sensations, especially when 
flexing and extending the knee. Pain is localized to the medial joint line, worse with 
squatting and climbing stairs.

Clinical examination:
- Positive McMurray test medially with palpable click
- Apley compression test positive
- Joint effusion present, moderate swelling
- Range of motion: 0-130° flexion, extension limited by pain
- No instability on Lachman or anterior drawer test
- Normal neurovascular examination

X-ray examination of the left knee performed in AP and lateral views, showing no bony 
pathology or signs of osteoarthritis. Small joint effusion visible.

Clinical diagnosis: Meniscal lesion of the left knee (M23.2), likely medial meniscus tear 
based on mechanism of injury and clinical findings.

Performed services:
1. Comprehensive orthopedic examination with detailed documentation (03246)
2. X-ray examination of the left knee (01760)
3. Diagnostic knee joint aspiration performed under sterile conditions - clear synovial fluid 
   obtained, sent for analysis (35900)

Recommendations: Rest, ice, compression, elevation. Referral for MRI to confirm meniscal 
pathology. Consider arthroscopic evaluation if symptoms persist or worsen. Physical therapy 
to maintain quadriceps strength.

Consultation duration: 20 minutes including examination, imaging review, and joint aspiration.
```

**Expected Codes:**
- ICD-10: M23.2 (Meniscal lesion), S83.5 (Sprain and strain of knee joint)
- EBM: 03246 (Orthopedic examination with documentation)
- EBM: 01760 (X-ray examination of extremities)
- EBM: 35900 (Diagnostic joint puncture)

---

## Note 6: Complex Surgical Case - Infected Wound with Removal of Foreign Body

**Patient:** Klaus Hoffmann, 42 years old  
**Date:** 2025-11-20  
**KV Region:** Bavaria  
**Specialty:** Surgery

```
The patient presents to the emergency department with a wound on the palmar surface of his 
right hand, sustained 5 days ago when he stepped on a piece of glass. The wound site shows 
signs of local infection with surrounding erythema, swelling, and purulent discharge. 
Patient reports increasing pain and warmth at the site.

Examination findings:
- Wound located on the thenar eminence, approximately 2cm in length
- Edges erythematous and swollen
- Purulent discharge present
- Palpable foreign body detected deep in the wound
- No signs of flexor tendon involvement on examination
- Range of motion intact, no neurovascular deficits

Procedure performed:
1. Surgical consultation and wound assessment (03440)
2. Local anesthesia administered
3. Careful exploration and removal of glass fragment (foreign body removal) (35700)
4. Wound debridement and irrigation with saline solution
5. Complex wound care with drainage placement (35102)
6. Dressing applied

Intraoperative findings: Glass fragment approximately 8mm x 5mm removed from deep tissue.

Diagnosis: Infected wound of the hand (S61.9) with retained foreign body.

Post-procedure care: Prescribed oral antibiotics (amoxicillin-clavulanate), wound care 
instructions provided, follow-up in 48 hours for dressing change and reassessment.

Total procedure time: 18 minutes including consultation, procedure, and documentation.
```

**Expected Codes:**
- ICD-10: S61.9 (Open wound of wrist and hand), T14.0 (Superficial injury)
- EBM: 03440 (Surgical consultation with documentation)
- EBM: 35700 (Removal of superficial foreign bodies)
- EBM: 35102 (Complex wound care)

---

## Note 7: Complex Orthopedic Case - Cervical Radiculopathy with Multiple Procedures

**Patient:** Prof. Dr. Christine Wagner, 61 years old  
**Date:** 2025-11-22  
**KV Region:** Berlin  
**Specialty:** Orthopedics

```
The patient presents with a 3-month history of progressive neck pain radiating into the 
right arm, associated with numbness and tingling in the thumb and index finger. Symptoms 
worsened after a motor vehicle accident 4 months ago. Pain is worse with neck extension 
and turning the head to the right.

Clinical examination:
- Limited cervical range of motion: flexion 30°, extension 15°, rotation right 20°, left 45°
- Positive Spurling's test on the right reproducing radicular symptoms
- Sensory deficit in C6 dermatome (thumb and index finger)
- Weakness in right wrist extension (4/5 strength)
- Diminished biceps reflex on the right
- Normal Hoffman's sign

Diagnostic imaging: X-ray of the cervical spine in AP, lateral, and oblique views performed. 
Findings show degenerative changes at C5-C6 and C6-C7 levels with foraminal narrowing on the 
right side at C5-C6, consistent with discogenic radiculopathy.

Clinical diagnosis: Cervical radiculopathy (M54.1) secondary to degenerative disc disease 
at C5-C6 level, likely C6 nerve root involvement.

Services rendered:
1. Comprehensive orthopedic examination with detailed neurological assessment (03246)
2. X-ray examination of the cervical spine (01762)
3. Therapeutic injection: Cervical epidural steroid injection at C5-C6 level (35910)

Post-procedure: Patient tolerated the procedure well. Instructions provided for activity 
modification, continuation of NSAIDs, and referral to physical therapy for cervical 
traction and strengthening exercises.

Follow-up scheduled in 6 weeks to assess response to treatment. If symptoms persist, 
consider MRI evaluation and surgical consultation.

Total consultation and procedure time: 28 minutes.
```

**Expected Codes:**
- ICD-10: M54.1 (Radiculopathy), M54.2 (Cervicalgia), M51.2 (Other intervertebral disc displacement)
- EBM: 03246 (Orthopedic examination with documentation)
- EBM: 01762 (X-ray examination of spine)
- EBM: 35910 (Therapeutic joint puncture)

---

## Note 8: Complex Surgical Case - Excision of Skin Lesion

**Patient:** Martin Schneider, 55 years old  
**Date:** 2025-11-25  
**KV Region:** Baden-Württemberg  
**Specialty:** Surgery

```
The patient presents for evaluation of a pigmented lesion on his back that has been slowly 
growing over the past 2 years. The lesion is located on the left scapular region, measures 
approximately 1.5cm in diameter, and has irregular borders with varying pigmentation. 
Patient reports occasional itching and slight elevation of the lesion.

Clinical examination:
- Lesion: Irregularly pigmented nevus, elevated, diameter 1.5cm
- Borders: Slightly irregular
- Color: Varying shades of brown
- Surface: Slightly raised, some areas appear scaly
- No satellite lesions or lymphadenopathy

Patient concerned about potential malignancy. After discussion of risks and benefits, decision 
made for excisional biopsy.

Procedure performed:
1. Surgical consultation and lesion assessment (03440)
2. Local anesthesia administered (lidocaine 1%)
3. Elliptical excision of the lesion with 2mm margins (35300)
4. Hemostasis achieved with electrocautery
5. Wound closure with interrupted sutures (35100)
6. Dressing applied

Specimen sent for histopathological examination.

Post-procedure: Wound care instructions provided. Sutures to be removed in 10-14 days. 
Patient advised to return for follow-up to review pathology results.

Diagnosis: Melanocytic nevus (D22.9), excised for diagnostic purposes.

Procedure duration: 22 minutes including consultation, procedure, and documentation.
```

**Expected Codes:**
- ICD-10: D22.9 (Melanocytic nevus)
- EBM: 03440 (Surgical consultation with documentation)
- EBM: 35300 (Excision of skin lesions)
- EBM: 35100 (Minor surgical procedure)

---

## Note 9: Intelligent Code Selection - Orthopedic Consultation with Multiple Services

**Patient:** Dr. Andreas Fischer, 49 years old  
**Date:** 2025-11-28  
**KV Region:** Hessen  
**Specialty:** Orthopedics

```
The patient presents with chronic right elbow pain for the past 4 months, gradually worsening. 
Pain is localized to the lateral epicondyle, worse with gripping and lifting activities. Patient 
is a dentist and reports the pain affects his work performance.

Clinical examination performed:
- Detailed orthopedic history and physical examination
- Inspection: slight swelling over lateral epicondyle
- Palpation: point tenderness over lateral epicondyle
- Positive Cozen's test for lateral epicondylitis
- Active range of motion testing: pain with resisted wrist extension
- Neurological examination: normal

Diagnostic imaging: X-ray of the right elbow performed in AP and lateral views to rule out 
bony pathology or calcifications. Findings show no abnormalities.

Clinical diagnosis: Lateral epicondylitis (tennis elbow), right elbow (M77.1).

Treatment provided:
1. Comprehensive orthopedic examination with detailed documentation of findings
2. X-ray examination of the right elbow (extremity imaging)
3. Therapeutic injection: corticosteroid injection into the lateral epicondyle region (35200)

Post-procedure: Patient instructed on activity modification, ergonomic recommendations, and 
prescribed NSAIDs. Follow-up scheduled in 3 weeks.

Total consultation and procedure time: 22 minutes including examination, imaging review, 
and injection.

**Billing Note:** This visit could technically be billed as:
- Option A: 03230 (General consultation ≥10 min) + 01760 (X-ray) + 35200 (Injection)
- Option B: 03246 (Orthopedic examination with documentation) + 01760 (X-ray) + 35200 (Injection)

**Expected Optimal Selection:** Option B - The specialized orthopedic examination code (03246) 
is more lucrative than a general consultation and includes the consultation component, so 
billing both would be redundant. The AI should automatically select the most lucrative 
combination: 03246 + 01760 + 35200.
```

**Expected Codes (Optimal Selection):**
- ICD-10: M77.1 (Lateral epicondylitis)
- EBM: 03246 (Orthopedic examination with documentation) ⭐ **More lucrative than 03230**
- EBM: 01760 (X-ray examination of extremities)
- EBM: 35200 (Injection at joints or tendons)

**Why this demonstrates intelligence:**
- The model should recognize that 03246 (specialized orthopedic exam) includes the consultation
- It should NOT bill both 03230 AND 03246 (redundant)
- It should choose 03246 over 03230 because it's more lucrative for the same work
- Additional procedures (X-ray, injection) can still be billed separately

---

## Note 10: Intelligent Code Selection - Surgical Procedure with Consultation

**Patient:** Petra Koch, 48 years old  
**Date:** 2025-12-01  
**KV Region:** Saxony  
**Specialty:** Surgery

```
The patient presents with a painful, infected ingrown toenail on the right great toe. Symptoms 
have been present for 2 weeks, with increasing pain, redness, and purulent discharge. Patient 
has tried conservative management with soaking and topical antibiotics without improvement.

Clinical examination:
- Right great toe: significant paronychia with erythema and swelling
- Nail plate embedded in lateral nail fold
- Purulent discharge present
- Range of motion: limited due to pain
- No signs of deeper infection or osteomyelitis

After surgical consultation and discussion of treatment options, decision made for partial 
nail avulsion with nail bed ablation.

Procedure performed:
1. Surgical consultation and assessment of the condition
2. Local anesthesia administered (digital block)
3. Partial nail avulsion (removal of the lateral portion of the nail plate) (35110)
4. Chemical ablation of the nail matrix using phenol
5. Complex wound care with antimicrobial dressing (35102)
6. Post-procedure instructions provided

Post-procedure: Patient advised to keep foot elevated, change dressing daily, and prescribed 
oral antibiotics. Follow-up in 1 week.

Total procedure time: 18 minutes including consultation, procedure, and documentation.

**Billing Note:** This visit could technically be billed as:
- Option A: 03230 (General consultation) + 35110 (Nail removal) + 35102 (Complex wound care)
- Option B: 03440 (Surgical consultation with documentation) + 35110 (Nail removal) + 35102 (Complex wound care)

**Expected Optimal Selection:** Option B - The surgical consultation code (03440) is more 
lucrative than a general consultation and includes the consultation component. The AI should 
recognize this and select the optimal combination: 03440 + 35110 + 35102, avoiding redundant 
billing of both consultation codes.
```

**Expected Codes (Optimal Selection):**
- ICD-10: L60.0 (Ingrown nail), T14.0 (Superficial injury)
- EBM: 03440 (Surgical consultation with documentation) ⭐ **More lucrative than 03230**
- EBM: 35110 (Removal of nails)
- EBM: 35102 (Complex wound care)

**Why this demonstrates intelligence:**
- The model should recognize that 03440 (surgical consultation) includes the basic consultation
- It should NOT bill both 03230 AND 03440 (redundant and incorrect)
- It should choose 03440 over 03230 because surgical consultations are more lucrative
- Additional procedures (nail removal, wound care) can still be billed separately

---

These complex cases demonstrate the tool's ability to:

1. **Extract multiple ICD-10 codes** from complex medical documentation
2. **Identify multiple EBM codes** for different procedures performed
3. **Handle specialized terminology** from orthopedics and surgery
4. **Process detailed clinical findings** and translate them into billing codes
5. **Recognize procedures** that require specific EBM codes (injections, imaging, surgical procedures)
6. **Intelligently select optimal billing combinations** - choosing more lucrative specialized codes over basic consultation codes when applicable

### Expected Capabilities Demonstrated:

- **Note 4**: Multiple EBM codes (examination, imaging, injection) + multiple ICD codes
- **Note 5**: Diagnostic procedures (joint aspiration) + imaging
- **Note 6**: Multiple surgical procedures (foreign body removal, complex wound care)
- **Note 7**: Complex radiculopathy case with multiple procedures and diagnoses
- **Note 8**: Surgical excision with proper coding
- **Note 9**: ⭐ **Intelligent code selection** - Choosing specialized orthopedic exam (03246) over general consultation (03230) for maximum billing
- **Note 10**: ⭐ **Intelligent code selection** - Choosing surgical consultation (03440) over general consultation (03230) for maximum billing

### Tips for Best Results

- The LLM should extract codes based on mentioned symptoms/conditions  
- Duration keywords like **"15 minutes"** or **"25 minutes"** should trigger appropriate consultation codes  
- Multiple procedures should yield multiple EBM codes
- Multiple diagnoses should yield multiple ICD codes
- The tool should recognize specialized procedures (injections, imaging, surgical procedures) and assign appropriate EBM codes
- **Most importantly**: The AI should intelligently select the most lucrative billing combination, avoiding redundant codes (e.g., don't bill both general consultation AND specialized consultation when the specialized code includes the consultation)
