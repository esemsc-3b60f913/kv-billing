import { useState, useEffect } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { useToast } from "@/hooks/use-toast";
import TreatmentForm, { FormData } from "@/components/TreatmentForm";
import ResultsDisplay from "@/components/ResultsDisplay";
import { FileText, Users, Download, Trash2 } from "lucide-react";

interface StoredPatient {
  id: string;
  patientName: string;
  date: string;
  icdCodes: string[];
  ebmCodes: string[];
  fullExtractionData: any;
  formData: FormData; // This is the FormData type from TreatmentForm component
}

const Index = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [isExporting, setIsExporting] = useState(false);
  const [isQuartalExporting, setIsQuartalExporting] = useState(false);
  const [selectedQuarter, setSelectedQuarter] = useState<string>("");
  // Set ExtractionResult to backend's shape
  const [results, setResults] = useState<{
    icdCodes: string[];
    ebmCodes: string[];
    isValid: boolean;
  } | null>(null);
  // Store the full extraction response for export
  const [fullExtractionData, setFullExtractionData] = useState<any>(null);
  const [storedPatients, setStoredPatients] = useState<StoredPatient[]>([]);
  const { toast } = useToast();

  // Load stored patients from localStorage on mount
  useEffect(() => {
    const stored = localStorage.getItem("kv_billing_patients");
    if (stored) {
      try {
        setStoredPatients(JSON.parse(stored));
      } catch (e) {
        console.error("Error loading stored patients:", e);
      }
    }
  }, []);

  // Save patients to localStorage whenever it changes
  useEffect(() => {
    if (storedPatients.length > 0) {
      localStorage.setItem("kv_billing_patients", JSON.stringify(storedPatients));
    } else {
      // Clear localStorage if no patients
      localStorage.removeItem("kv_billing_patients");
    }
  }, [storedPatients]);

  // Replace with your actual FastAPI backend URL
  const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

  const handleFormSubmit = async (formData: FormData) => {
    setIsLoading(true);
    setResults(null);
    setFullExtractionData(null);

    try {
      const response = await fetch(`${API_BASE_URL}/extract`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          doctor_note_text: formData.documentation,
          date: formData.date || new Date().toISOString().split("T")[0],
          kv_region: formData.kvRegion || "",
          specialty: formData.specialty || "",
          patient_age: formData.patientAge ? parseInt(formData.patientAge) : 0,
          insurance_type: formData.insuranceType || "GKV",
        }),
      });

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || "Fehler bei der Verarbeitung");
      }

      // Adapt to backend's actual output fields (diagnoses, ebm_codes, encounter_metadata)
      const data = await response.json();
      // Store the full extraction data for export
      setFullExtractionData(data);
      // diagnoses is an array of { icd10_code: string ... }. Map to string[]
      const icdCodes = Array.isArray(data.diagnoses)
        ? data.diagnoses.map((diag: any) => diag.icd10_code || diag.code).filter(Boolean)
        : [];
      // ebm_codes will rarely be just strings, but extract 'code'
      const ebmCodes = Array.isArray(data.ebm_codes)
        ? data.ebm_codes.map((ebm: any) => ebm.code || "").filter(Boolean)
        : [];
      // isValid: you might want smarter logic, here we validate they are not empty
      const isValid = icdCodes.length > 0 && ebmCodes !== undefined;
      setResults({ icdCodes, ebmCodes, isValid });

      // Store patient data for quartal export
      // Ensure kv_region is set in the extraction data if missing
      const extractionDataWithRegion = { ...data };
      if (!extractionDataWithRegion.encounter_metadata) {
        extractionDataWithRegion.encounter_metadata = {};
      }
      if (!extractionDataWithRegion.encounter_metadata.kv_region || extractionDataWithRegion.encounter_metadata.kv_region === "") {
        extractionDataWithRegion.encounter_metadata.kv_region = formData.kvRegion || "Berlin";
      }

      const patientData: StoredPatient = {
        id: `P${Date.now()}`,
        patientName: formData.patientName,
        date: formData.date || new Date().toISOString().split("T")[0],
        icdCodes,
        ebmCodes,
        fullExtractionData: extractionDataWithRegion,
        formData,
      };
      setStoredPatients((prev) => [...prev, patientData]);

      toast({
        title: "Erfolgreich verarbeitet",
        description: `${icdCodes.length} ICD-Codes und ${ebmCodes.length} EBM-Codes extrahiert. Patient gespeichert.`,
      });
    } catch (error) {
      console.error("Error:", error);
      toast({
        title: "Fehler",
        description: error instanceof Error ? error.message : "Ein unerwarteter Fehler ist aufgetreten.",
        variant: "destructive",
      });
    } finally {
      setIsLoading(false);
    }
  };

  const handleExport = async () => {
    if (!results || !fullExtractionData) return;
    setIsExporting(true);
    try {
      // package backend export request to match KvdtExportRequest; use full extraction data
      const exportPayload = {
        practice: {
          id: "1234567890",
          iknr: "123456789",
          lanr: "123456789",
          name: "Hausarztpraxis Müller"
        },
        patient: {
          id: "P001",
          name: "Erika Mustermann",
          birthdate: "1980-01-01"
        },
        encounters: [
          // Use the full extraction data directly to preserve all metadata
          fullExtractionData
        ]
      };
      const response = await fetch(`${API_BASE_URL}/kvdt/export`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(exportPayload),
      });
      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || "Fehler beim Export");
      }
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `kvdt-export-${new Date().toISOString().split("T")[0]}.txt`;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
      toast({
        title: "Export erfolgreich",
        description: "Die KVDT-Datei wurde heruntergeladen.",
      });
    } catch (error) {
      console.error("Error:", error);
      toast({
        title: "Export fehlgeschlagen",
        description: error instanceof Error ? error.message : "Ein unerwarteter Fehler ist aufgetreten.",
        variant: "destructive",
      });
    } finally {
      setIsExporting(false);
    }
  };

  const handleQuartalExport = async () => {
    if (!selectedQuarter) {
      toast({
        title: "Fehler",
        description: "Bitte wählen Sie ein Quartal aus.",
        variant: "destructive",
      });
      return;
    }

    const patientsForQuarter = storedPatients.filter((patient) => {
      const year = patient.date.substring(0, 4);
      const month = parseInt(patient.date.substring(5, 7));
      let quarter = "";
      if (month >= 1 && month <= 3) quarter = `${year}Q1`;
      else if (month >= 4 && month <= 6) quarter = `${year}Q2`;
      else if (month >= 7 && month <= 9) quarter = `${year}Q3`;
      else quarter = `${year}Q4`;
      return quarter === selectedQuarter;
    });

    if (patientsForQuarter.length === 0) {
      toast({
        title: "Keine Patienten",
        description: `Keine Patienten für ${selectedQuarter} gefunden.`,
        variant: "destructive",
      });
      return;
    }

    setIsQuartalExporting(true);
    try {
      // Group encounters by patient
      const encountersByPatient = new Map<string, any[]>();
      patientsForQuarter.forEach((patient) => {
        const patientId = patient.id;
        if (!encountersByPatient.has(patientId)) {
          encountersByPatient.set(patientId, []);
        }
        encountersByPatient.get(patientId)!.push(patient.fullExtractionData);
      });

      // Export all patients and encounters for the quarter
      // Ensure kv_region is set for each encounter (use formData as fallback)
      const allEncounters: any[] = [];
      patientsForQuarter.forEach((patient) => {
        const encounter = { ...patient.fullExtractionData };
        // Ensure kv_region is set in encounter_metadata
        if (!encounter.encounter_metadata || !encounter.encounter_metadata.kv_region || encounter.encounter_metadata.kv_region === "") {
          if (!encounter.encounter_metadata) {
            encounter.encounter_metadata = {};
          }
          // Use kv_region from formData, or default to "Berlin" if still missing
          encounter.encounter_metadata.kv_region = patient.formData.kvRegion || "Berlin";
        }
        allEncounters.push(encounter);
      });

      const exportPayload = {
        practice: {
          id: "1234567890",
          iknr: "123456789",
          lanr: "123456789",
          name: "Hausarztpraxis Müller",
        },
        patient: {
          id: "QUARTAL_EXPORT",
          name: "Quartal Export",
          birthdate: "1900-01-01",
        },
        encounters: allEncounters,
      };

      const response = await fetch(`${API_BASE_URL}/kvdt/export`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(exportPayload),
      });

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || "Fehler beim Quartal Export");
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `kvdt-quartal-export-${selectedQuarter}.txt`;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);

      toast({
        title: "Quartal Export erfolgreich",
        description: `${patientsForQuarter.length} Patienten für ${selectedQuarter} exportiert.`,
      });
    } catch (error) {
      console.error("Error:", error);
      toast({
        title: "Export fehlgeschlagen",
        description: error instanceof Error ? error.message : "Ein unerwarteter Fehler ist aufgetreten.",
        variant: "destructive",
      });
    } finally {
      setIsQuartalExporting(false);
    }
  };

  const handleDeletePatient = (patientId: string) => {
    setStoredPatients((prev) => prev.filter((p) => p.id !== patientId));
    toast({
      title: "Patient gelöscht",
      description: "Patient wurde aus der Liste entfernt.",
    });
  };

  // Get unique quarters from stored patients
  const getAvailableQuarters = (): string[] => {
    const quarters = new Set<string>();
    storedPatients.forEach((patient) => {
      const year = patient.date.substring(0, 4);
      const month = parseInt(patient.date.substring(5, 7));
      let quarter = "";
      if (month >= 1 && month <= 3) quarter = `${year}Q1`;
      else if (month >= 4 && month <= 6) quarter = `${year}Q2`;
      else if (month >= 7 && month <= 9) quarter = `${year}Q3`;
      else quarter = `${year}Q4`;
      quarters.add(quarter);
    });
    return Array.from(quarters).sort().reverse();
  };

  return (
    <div className="min-h-screen bg-background py-8 px-4">
      <div className="max-w-4xl mx-auto space-y-8">
        <header className="text-center space-y-2">
          <div className="flex items-center justify-center gap-2 text-primary">
            <FileText className="h-8 w-8" />
            <h1 className="text-3xl font-bold">Medizinische Abrechnung</h1>
          </div>
          <p className="text-muted-foreground">
            Automatische Extraktion von ICD- und EBM-Codes aus Behandlungsdokumentationen
          </p>
        </header>

        <Card>
          <CardHeader>
            <CardTitle>Behandlungsdokumentation</CardTitle>
            <CardDescription>
              Geben Sie die Behandlungsdokumentation ein und ergänzen Sie optional weitere Angaben.
            </CardDescription>
          </CardHeader>
          <CardContent>
            <TreatmentForm onSubmit={handleFormSubmit} isLoading={isLoading} />
          </CardContent>
        </Card>

        {results && (
          <ResultsDisplay
            icdCodes={results.icdCodes}
            ebmCodes={results.ebmCodes}
            isValid={results.isValid}
            onExport={handleExport}
            isExporting={isExporting}
          />
        )}

        {/* Stored Patients and Quartal Export */}
        <Card>
          <CardHeader>
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <Users className="h-5 w-5" />
                <CardTitle>Gespeicherte Patienten</CardTitle>
              </div>
              <Badge variant="secondary">{storedPatients.length} Patienten</Badge>
            </div>
            <CardDescription>
              Alle behandelten Patienten mit ihren ICD- und EBM-Codes
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            {/* Quartal Export Section */}
            <div className="flex items-end gap-2 p-4 bg-muted rounded-lg">
              <div className="flex-1 space-y-2">
                <label className="text-sm font-medium">Quartal Export</label>
                <Select value={selectedQuarter} onValueChange={setSelectedQuarter}>
                  <SelectTrigger>
                    <SelectValue placeholder="Quartal auswählen" />
                  </SelectTrigger>
                  <SelectContent>
                    {getAvailableQuarters().map((quarter) => (
                      <SelectItem key={quarter} value={quarter}>
                        {quarter}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>
              <Button
                onClick={handleQuartalExport}
                disabled={!selectedQuarter || isQuartalExporting || storedPatients.length === 0}
              >
                {isQuartalExporting ? (
                  <>
                    <Download className="mr-2 h-4 w-4 animate-pulse" />
                    Exportiere...
                  </>
                ) : (
                  <>
                    <Download className="mr-2 h-4 w-4" />
                    Quartal Export
                  </>
                )}
              </Button>
            </div>

            {/* Patient List */}
            {storedPatients.length > 0 ? (
              <div className="space-y-2">
                {storedPatients.map((patient) => (
                  <div
                    key={patient.id}
                    className="flex items-start justify-between p-4 border rounded-lg hover:bg-muted/50"
                  >
                    <div className="flex-1 space-y-2">
                      <div className="flex items-center gap-2">
                        <h4 className="font-semibold">{patient.patientName}</h4>
                        <Badge variant="outline">{patient.date}</Badge>
                      </div>
                      <div className="space-y-1">
                        <div className="text-sm">
                          <span className="font-medium">ICD-Codes: </span>
                          {patient.icdCodes.length > 0 ? (
                            <div className="inline-flex flex-wrap gap-1 mt-1">
                              {patient.icdCodes.map((code, idx) => (
                                <Badge key={idx} variant="secondary" className="font-mono text-xs">
                                  {code}
                                </Badge>
                              ))}
                            </div>
                          ) : (
                            <span className="text-muted-foreground">Keine</span>
                          )}
                        </div>
                        <div className="text-sm">
                          <span className="font-medium">EBM-Codes: </span>
                          {patient.ebmCodes.length > 0 ? (
                            <div className="inline-flex flex-wrap gap-1 mt-1">
                              {patient.ebmCodes.map((code, idx) => (
                                <Badge key={idx} variant="secondary" className="font-mono text-xs">
                                  {code}
                                </Badge>
                              ))}
                            </div>
                          ) : (
                            <span className="text-muted-foreground">Keine</span>
                          )}
                        </div>
                      </div>
                    </div>
                    <Button
                      variant="ghost"
                      size="icon"
                      onClick={() => handleDeletePatient(patient.id)}
                      className="ml-2"
                    >
                      <Trash2 className="h-4 w-4 text-destructive" />
                    </Button>
                  </div>
                ))}
              </div>
            ) : (
              <div className="text-center py-8 text-muted-foreground">
                <Users className="h-12 w-12 mx-auto mb-2 opacity-50" />
                <p>Noch keine Patienten gespeichert</p>
                <p className="text-sm">Patienten werden automatisch beim Verarbeiten gespeichert</p>
              </div>
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default Index;
