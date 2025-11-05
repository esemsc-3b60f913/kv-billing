import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Download, CheckCircle2, AlertCircle } from "lucide-react";

interface ResultsDisplayProps {
  icdCodes: string[];
  ebmCodes: string[];
  isValid: boolean;
  onExport: () => void;
  isExporting: boolean;
}

const ResultsDisplay = ({ icdCodes, ebmCodes, isValid, onExport, isExporting }: ResultsDisplayProps) => {
  return (
    <Card className="border-result-border bg-result-bg">
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardTitle className="flex items-center gap-2">
            Extracted Codes
            {isValid ? (
              <CheckCircle2 className="h-5 w-5 text-success" />
            ) : (
              <AlertCircle className="h-5 w-5 text-destructive" />
            )}
          </CardTitle>
          <Badge variant={isValid ? "default" : "destructive"}>
            {isValid ? "Validated" : "Invalid"}
          </Badge>
        </div>
        <CardDescription>
          {isValid
            ? "The codes were successfully extracted and validated."
            : "The extracted codes could not be validated."}
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-4">
        <div>
          <h4 className="font-semibold text-sm mb-2">ICD Codes</h4>
          <div className="flex flex-wrap gap-2">
            {icdCodes.length > 0 ? (
              icdCodes.map((code, index) => (
                <Badge key={index} variant="secondary" className="font-mono">
                  {code}
                </Badge>
              ))
            ) : (
              <span className="text-sm text-muted-foreground">No ICD codes found</span>
            )}
          </div>
        </div>

        <div>
          <h4 className="font-semibold text-sm mb-2">EBM Codes</h4>
          <div className="flex flex-wrap gap-2">
            {ebmCodes.length > 0 ? (
              ebmCodes.map((code, index) => (
                <Badge key={index} variant="secondary" className="font-mono">
                  {code}
                </Badge>
              ))
            ) : (
              <span className="text-sm text-muted-foreground">No EBM codes found</span>
            )}
          </div>
        </div>

        {isValid && (
          <Button onClick={onExport} disabled={isExporting} className="w-full mt-4">
            {isExporting ? (
              <>
                <Download className="mr-2 h-4 w-4 animate-pulse" />
                Exporting...
              </>
            ) : (
              <>
                <Download className="mr-2 h-4 w-4" />
                KVDT Export
              </>
            )}
          </Button>
        )}
      </CardContent>
    </Card>
  );
};

export default ResultsDisplay;
