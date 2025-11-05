# Demo Video Script: KV Billing Tool

## Introduction (0:00 - 0:30)

**[Screen: Frontend application loaded]**

"Welcome! Today I'm demonstrating our Medical Billing tool that automatically extracts ICD-10 and EBM codes from German medical documentation. This tool streamlines the billing process for outpatient practices in Germany by using AI to extract the required billing codes."

**[Navigate to the main page]**

"This is our clean, English interface. Let me walk you through how it works with three real patient cases."

---

## Part 1: Processing Patient 1 - Acute Pharyngitis (0:30 - 2:00)

### Setup

**[Click on Treatment Documentation form]**

"First, I'll process a patient with acute pharyngitis. I'll enter the patient details..."

**[Fill in form]**
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


**[Click "Process" button]**

### What Happens in the Backend

"Now, let me explain what's happening behind the scenes when I click Process."

**[Show backend terminal/logs or switch to code view]**

**Backend Flow Explanation:**

1. **API Request to `/extract` endpoint**
   - "The frontend sends a POST request to our FastAPI backend at `/extract`"
   - "The request includes the doctor's note text, patient metadata, date, region, specialty, and age"

2. **GPT-4 API Call**
   - "Our backend uses GPT-4o-mini to analyze the medical documentation"
   - "The prompt instructs the AI to extract only valid ICD-10-GM and EBM codes"
   - "It's instructed to be conservative - if uncertain, it leaves fields empty"
   - "The AI returns structured JSON with diagnoses and EBM codes"

3. **Smart Duration Detection**
   - "Our backend automatically detects consultation duration from the text"
   - "It searches for patterns like '15 Minuten' or '15 minutes'"
   - "For EBM code 03230, which requires duration, it automatically fills in `dauer_minuten` if detected"

4. **Data Normalization**
   - "The backend normalizes the response structure"
   - "ICD codes are standardized to uppercase"
   - "EBM codes are structured with required fields and Zusatzangaben (additional data)"

5. **Validation**
   - "The data is validated against our reference databases"
   - "ICD codes are checked against ICD-10-GM reference"
   - "EBM codes are validated against EBM code specifications"
   - "Required fields like primary diagnosis and duration (for certain codes) are verified"

**[Switch back to frontend]**

### Results Display

**[Results appear on screen]**

"Perfect! The system extracted:
- **ICD Code: J02.9** - Acute Pharyngitis
- **EBM Code: 03230** - with 15 minutes duration (for consultations over 10 minutes)

The badge shows 'Validated' - meaning all codes passed validation checks. The patient has been automatically saved to our local storage."

---

## Part 2: Processing Patient 2 - Lower Back Pain (2:00 - 3:00)

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

**[Click "Process"]**

**[Wait for results]**

"Excellent! The system extracted:
- **ICD Code: M54.5** - Kreuzschmerz (Lower back pain)
- **EBM Code: 03230** - with 12 minutes duration

Notice how it automatically detected the 12 minutes from the text and added it to the EBM code. This patient is also saved."

---

## Part 3: Processing Patient 3 - Fever and Headache (3:00 - 4:00)

**[Fill in third patient]**

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

**[Click "Process"]**

**[Wait for results]**

"Great! This case is interesting because:
- **Multiple ICD Codes** were extracted: Fever (R50.9), Headache (R51), or possibly Upper Respiratory Infection (J06.9)
- **EBM Code: 03220** - Notice this is different! Since the consultation was only 8 minutes (under 10 minutes), it correctly used code 03220 instead of 03230"

**[Scroll down to show stored patients list]**

"You can see all three patients are now stored in the system, organized by date, with their ICD and EBM codes visible."

---

## Part 4: Single Patient Export (4:00 - 5:00)

**[Click on one patient's results card]**

"Now let's export a single patient's billing data. I'll click the 'KVDT Export' button on Anna Schmidt's results."

**[Click "KVDT Export" button]**

### Export Process Explanation

"Behind the scenes, here's what happens:"

1. **Export Request**
   - "The frontend sends a POST request to `/kvdt/export`"
   - "It packages the patient data with practice information and encounter metadata"

2. **KVDT Format Generation**
   - "The backend generates a KVDT (KV Data Transfer) file - the standard format for German health insurance billing"
   - "It creates fixed-width records following the KVDT specification:
     - **6000**: Header record with version and quarter
     - **6100**: Practice information (IKNR, LANR, name)
     - **6200**: Patient encounter record with primary ICD code
     - **6300**: EBM code records with duration in minutes
     - **9999**: Trailer record with total record count"

3. **Validation Before Export**
   - "Each encounter is validated again before export"
   - "Any errors would prevent export and show validation messages"

4. **File Download**
   - "The generated `.txt` file is downloaded to your computer"
   - "This file can be directly submitted to the KV (Kassenärztliche Vereinigung)"

**[Show downloaded file or file preview]**

"The file follows the exact KVDT specification required for billing submission."

---

## Part 5: Quarterly Export (5:00 - 6:30)

**[Scroll to Stored Patients section]**

"Now, for the powerful feature - quarterly export. This allows you to export all patients from a specific quarter in one batch."

**[Point to Quarter Export section]**

"I can see we have patients from Q4 2025. Let me select that quarter and export all patients."

**[Select "2025Q4" from dropdown]**

**[Click "Quarter Export" button]**

### Quarterly Export Process

**Backend Explanation:**

1. **Patient Filtering**
   - "The frontend filters all stored patients by the selected quarter"
   - "Dates are parsed to determine which quarter each patient belongs to"

2. **Batch Processing**
   - "All encounters for the quarter are collected"
   - "The system ensures each encounter has required metadata (KV region, quarter)"

3. **KVDT File Generation**
   - "A single KVDT file is generated with all encounters"
   - "Each patient encounter becomes a 6200 record with its 6300 EBM records"
   - "The file maintains proper record ordering and counts"

4. **Validation**
   - "All encounters are validated before inclusion"
   - "Any invalid encounters would generate errors but valid ones still export"

**[File downloads]**

"Perfect! The quarterly export file contains all three patients from Q4 2025. This single file can be submitted for the entire quarter's billing."

---

## Part 6: Backend Architecture Overview (6:30 - 7:30)

**[Show code/files or architecture diagram]**

"Let me quickly explain the backend architecture:"

### Key Components:

1. **FastAPI Backend (`main.py`)**
   - RESTful API with three main endpoints:
     - `/extract` - Processes doctor notes
     - `/validate` - Validates extracted codes
     - `/kvdt/export` - Generates billing files

2. **AI Integration (`prompts.py`)**
   - Uses OpenAI GPT-4o-mini for code extraction
   - Carefully crafted prompts for accuracy
   - Temperature set to 0 for consistent results

3. **Validation Engine (`validator.py`)**
   - Validates ICD codes against ICD-10-GM reference
   - Validates EBM codes against EBM specifications
   - Checks required Zusatzangaben (additional data)

4. **Reference Data (`reference.py`)**
   - Contains lookup tables for valid ICD-10 codes
   - Contains EBM code specifications and requirements

5. **KVDT Formatter (`kvdt.py`)**
   - Generates fixed-width formatted files
   - Follows official KVDT specification
   - Handles all required record types

### Data Flow:

```
Doctor Note → Frontend → POST /extract
                        ↓
                  GPT-4 API Call
                        ↓
                  Response Normalization
                        ↓
                  Validation Checks
                        ↓
                  Return to Frontend
                        ↓
                  Store in LocalStorage
                        ↓
                  Export → POST /kvdt/export
                                ↓
                          Generate KVDT File
                                ↓
                          Download .txt file
```

---

## Conclusion (7:30 - 8:00)

**[Show full interface with all three patients]**

"This tool dramatically simplifies medical billing:

✅ **Automatic Code Extraction** - AI extracts ICD and EBM codes from free-form text  
✅ **Smart Validation** - Ensures all codes are valid before export  
✅ **Duration Detection** - Automatically extracts consultation duration  
✅ **Batch Processing** - Export single patients or entire quarters  
✅ **Standard Format** - Generates KVDT files ready for submission  

The system handles the complexity of German medical billing codes, so doctors can focus on patient care rather than administrative work."

**[End screen with contact info or next steps]**

---

## Tips for Recording:

1. **Screen Recording**: Use screen recording software (OBS, QuickTime, etc.)
2. **Pacing**: Speak clearly and pause at key moments
3. **Highlights**: Use cursor highlighting or zoom-in for important UI elements
4. **Backend View**: Have a terminal window open showing API logs if possible
5. **Error Handling**: Consider showing what happens with invalid input (optional)
6. **Cut Scenes**: You can edit out waiting times for API responses
7. **Zoom**: Zoom in on code extraction results and validation badges
8. **File Preview**: Show a quick preview of the exported KVDT file contents

---

## Quick Reference: Patient Data for Copy-Paste

### Patient 1: Max Mustermann

**Form Fields:**
- Patient Name: `Max Mustermann`
- Treatment Date: `2025-10-28`
- Patient Age: `45`
- KV Region: `Berlin`
- Insurance Type: `GKV (Public)`
- Specialty: `General Medicine`

**Documentation Text:**
```
Patient stellt sich vor mit seit 2 Tagen bestehenden Halsschmerzen und Schluckbeschwerden. 
Kein Fieber, Allgemeinzustand leicht reduziert. 
Rachen gerötet, Tonsillen mäßig geschwollen, keine Beläge.
Klinische Diagnose: Akute Pharyngitis.

Durchgeführte Leistungen:
- Anamnese und körperliche Untersuchung
- Beratung zur symptomatischen Behandlung
- Gesprächsdauer: 15 Minuten

Empfehlung: Symptomatische Therapie mit Gurgellösungen, Paracetamol bei Bedarf. 
Bei Persistenz oder Verschlechterung Wiedervorstellung.
```

**Expected Results:**
- ICD: J02.9 (Acute Pharyngitis)
- EBM: 03230 (with dauer_minuten: 15)

---

### Patient 2: Anna Schmidt

**Form Fields:**
- Patient Name: `Anna Schmidt`
- Treatment Date: `2025-11-05`
- Patient Age: `52`
- KV Region: `Bayern`
- Insurance Type: `GKV (Public)`
- Specialty: `General Medicine`

**Documentation Text:**
```
Patientin klagt über seit 3 Tagen bestehende akute Kreuzschmerzen im Bereich der LWS. 
Schmerzen verstärken sich bei Bewegung, Besserung in Ruhe. Keine Ausstrahlung in die Beine, 
keine neurologischen Ausfälle. 

Anamnese ergab: Heben einer schweren Kiste vor 3 Tagen, danach akuter Schmerzbeginn.

Durchgeführte Untersuchung: Inspektion, Palpation, Beweglichkeitstest. 
Beratung zu rückenschonendem Verhalten, Krankengymnastik empfohlen.

Beratungsgespräch dauerte 12 Minuten.
```

**Expected Results:**
- ICD: M54.5 (Lower back pain / Kreuzschmerz)
- EBM: 03230 (with dauer_minuten: 12)

---

### Patient 3: Thomas Weber

**Form Fields:**
- Patient Name: `Thomas Weber`
- Treatment Date: `2025-11-10`
- Patient Age: `38`
- KV Region: `Berlin`
- Insurance Type: `GKV (Public)`
- Specialty: `General Medicine`

**Documentation Text:**
```
Patient meldet sich mit Fieber bis 38,5°C und ausgeprägten Kopfschmerzen seit heute Morgen. 
Allgemeinzustand reduziert, kein Husten, keine Halsschmerzen. 
Körperliche Untersuchung: Tympanische Temperatur 38,2°C, sonst unauffälliger Befund.

Verdacht auf viralen Infekt der oberen Atemwege.

Behandlung: Symptomatische Therapie mit Paracetamol, Bettruhe, ausreichende Flüssigkeitszufuhr.
Kurze Beratung von 8 Minuten.
```

**Expected Results:**
- ICD: R50.9 (Fever) and/or R51 (Headache) and/or J06.9 (Upper respiratory infection)
- EBM: 03220 (since 8 minutes < 10 minutes)

---

## Backend API Endpoints Reference

**Base URL:** `http://localhost:8000` (or your deployed URL)

1. **POST `/extract`**
   - Request body: `ExtractionPayload` (doctor_note_text, date, kv_region, specialty, patient_age, insurance_type)
   - Response: `ExtractionResult` (diagnoses, ebm_codes, encounter_metadata)

2. **POST `/validate`**
   - Request body: `ExtractionResult`
   - Response: `ValidationResult` (ok, errors, warnings)

3. **POST `/kvdt/export`**
   - Request body: `KvdtExportRequest` (practice, patient, encounters)
   - Response: `KvdtExportResponse` (ok, errors, content)
