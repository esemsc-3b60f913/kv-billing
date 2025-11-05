import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Loader2 } from "lucide-react";

interface TreatmentFormProps {
  onSubmit: (data: FormData) => Promise<void>;
  isLoading: boolean;
}

export interface FormData {
  patientName: string;
  documentation: string;
  date: string;
  patientAge?: string;
  kvRegion?: string;
  insuranceType?: string;
  specialty: string;
}

const TreatmentForm = ({ onSubmit, isLoading }: TreatmentFormProps) => {
  const [formData, setFormData] = useState<FormData>({
    patientName: "",
    documentation: "",
    date: new Date().toISOString().split("T")[0],
    patientAge: "",
    kvRegion: "",
    insuranceType: "",
    specialty: "Allgemeinmedizin",
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="space-y-2">
          <Label htmlFor="patientName" className="text-base font-semibold">
            Patient Name *
          </Label>
          <Input
            id="patientName"
            placeholder="e.g. John Doe"
            value={formData.patientName}
            onChange={(e) => setFormData({ ...formData, patientName: e.target.value })}
            required
          />
        </div>

        <div className="space-y-2">
          <Label htmlFor="date" className="text-base font-semibold">
            Treatment Date *
          </Label>
          <Input
            id="date"
            type="date"
            value={formData.date}
            onChange={(e) => setFormData({ ...formData, date: e.target.value })}
            required
          />
        </div>
      </div>

      <div className="space-y-2">
        <Label htmlFor="documentation" className="text-base font-semibold">
          Treatment Documentation *
        </Label>
        <Textarea
          id="documentation"
          placeholder="Describe the treatment, diagnoses and services performed..."
          value={formData.documentation}
          onChange={(e) => setFormData({ ...formData, documentation: e.target.value })}
          className="min-h-[200px] resize-y"
          required
        />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="space-y-2">
          <Label htmlFor="patientAge">Patient Age (optional)</Label>
          <Input
            id="patientAge"
            type="number"
            min="0"
            max="150"
            placeholder="e.g. 45"
            value={formData.patientAge}
            onChange={(e) => setFormData({ ...formData, patientAge: e.target.value })}
          />
        </div>

        <div className="space-y-2">
          <Label htmlFor="kvRegion">KV Region (optional)</Label>
          <Select
            value={formData.kvRegion}
            onValueChange={(value) => setFormData({ ...formData, kvRegion: value })}
          >
            <SelectTrigger id="kvRegion">
              <SelectValue placeholder="Select Region" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="Berlin">Berlin</SelectItem>
              <SelectItem value="Bayern">Bayern</SelectItem>
              <SelectItem value="NRW">Nordrhein-Westfalen</SelectItem>
              <SelectItem value="Baden-Württemberg">Baden-Württemberg</SelectItem>
              <SelectItem value="Niedersachsen">Niedersachsen</SelectItem>
              <SelectItem value="Hessen">Hessen</SelectItem>
              <SelectItem value="Rheinland-Pfalz">Rheinland-Pfalz</SelectItem>
              <SelectItem value="Sachsen">Sachsen</SelectItem>
              <SelectItem value="Schleswig-Holstein">Schleswig-Holstein</SelectItem>
            </SelectContent>
          </Select>
        </div>

        <div className="space-y-2">
          <Label htmlFor="insuranceType">Insurance Type (optional)</Label>
          <Select
            value={formData.insuranceType}
            onValueChange={(value) => setFormData({ ...formData, insuranceType: value })}
          >
            <SelectTrigger id="insuranceType">
              <SelectValue placeholder="Select Type" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="GKV">GKV (Public)</SelectItem>
              <SelectItem value="PKV">PKV (Private)</SelectItem>
            </SelectContent>
          </Select>
        </div>

        <div className="space-y-2">
          <Label htmlFor="specialty">Specialty</Label>
          <Select
            value={formData.specialty}
            onValueChange={(value) => setFormData({ ...formData, specialty: value })}
          >
            <SelectTrigger id="specialty">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="Allgemeinmedizin">General Medicine</SelectItem>
              <SelectItem value="Innere Medizin">Internal Medicine</SelectItem>
              <SelectItem value="Chirurgie">Surgery</SelectItem>
              <SelectItem value="Pädiatrie">Pediatrics</SelectItem>
              <SelectItem value="Orthopädie">Orthopedics</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </div>

      <Button 
        type="submit" 
        className="w-full" 
        disabled={isLoading || !formData.documentation || !formData.patientName}
      >
        {isLoading ? (
          <>
            <Loader2 className="mr-2 h-4 w-4 animate-spin" />
            Processing...
          </>
        ) : (
          "Process"
        )}
      </Button>
    </form>
  );
};

export default TreatmentForm;
