# Test Doctor Notes

These three doctor notes are designed to work with your current ICD-10 and EBM code reference setup.

## Note 1: Acute Pharyngitis (Pharyngitis)

**Patient:** Max Mustermann, 45 Jahre alt  
**Date:** 2025-10-28  
**KV Region:** Berlin  
**Specialty:** Allgemeinmedizin

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

**Expected Codes:**
- ICD-10: J02.9 (Akute Pharyngitis, nicht näher bezeichnet)
- EBM: 03230 (Hausärztliche Beratung ab 10 Min) with dauer_minuten: 15

---

## Note 2: Lower Back Pain (Kreuzschmerz)

**Patient:** Anna Schmidt, 52 Jahre alt  
**Date:** 2025-11-05  
**KV Region:** Bayern  
**Specialty:** Allgemeinmedizin

```
Patientin klagt über seit 3 Tagen bestehende akute Kreuzschmerzen im Bereich der LWS. 
Schmerzen verstärken sich bei Bewegung, Besserung in Ruhe. Keine Ausstrahlung in die Beine, 
keine neurologischen Ausfälle. 

Anamnese ergab: Heben einer schweren Kiste vor 3 Tagen, danach akuter Schmerzbeginn.

Durchgeführte Untersuchung: Inspektion, Palpation, Beweglichkeitstest. 
Beratung zu rückenschonendem Verhalten, Krankengymnastik empfohlen.

Beratungsgespräch dauerte 12 Minuten.
```

**Expected Codes:**
- ICD-10: M54.5 (Kreuzschmerz)
- EBM: 03230 (Hausärztliche Beratung ab 10 Min) with dauer_minuten: 12

---

## Note 3: Fever and Headache (Fieber und Kopfschmerz)

**Patient:** Thomas Weber, 38 Jahre alt  
**Date:** 2025-11-10  
**KV Region:** Berlin  
**Specialty:** Allgemeinmedizin

```
Patient meldet sich mit Fieber bis 38,5°C und ausgeprägten Kopfschmerzen seit heute Morgen. 
Allgemeinzustand reduziert, kein Husten, keine Halsschmerzen. 
Körperliche Untersuchung: Tympanische Temperatur 38,2°C, sonst unauffälliger Befund.

Verdacht auf viralen Infekt der oberen Atemwege.

Behandlung: Symptomatische Therapie mit Paracetamol, Bettruhe, ausreichende Flüssigkeitszufuhr.
Kurze Beratung von 8 Minuten.
```

**Expected Codes:**
- ICD-10: R50.9 (Fieber, nicht näher bezeichnet), R51 (Kopfschmerz), or J06.9 (Akute Infektion der oberen Atemwege)
- EBM: 03220 (Hausärztliche Beratung bis 10 Min) - since 8 minutes is under 10

---

## Testing Instructions

1. Copy each note into the "Behandlungsdokumentation" field
2. Fill in the corresponding patient name, date, and other form fields
3. Submit and verify that:
   - ICD codes are correctly extracted
   - EBM codes match the consultation duration
   - Patient is saved in the stored patients list
4. Test the Quartal Export by processing multiple notes with dates in the same quarter

---

## Tips for Best Results

- The LLM should extract codes based on the symptoms/conditions mentioned
- Duration keywords like "15 Minuten" or "12 Minuten" should trigger EBM 03230 with dauer_minuten
- Duration under 10 minutes should trigger EBM 03220
- Multiple symptoms may result in multiple ICD codes being extracted

