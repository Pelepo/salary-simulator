from pydantic import BaseModel, Field
from typing import Optional


class TaxYear(BaseModel):
    year: int = Field(2026, ge=2025, description="Anno fiscale di riferimento")


class SalaryInput(BaseModel):
    ral: float = Field(..., gt=0, description="Retribuzione Annua Lorda")
    mensilita: int = Field(13, ge=12, le=14, description="Numero mensilità")
    tax_year: TaxYear


class SalaryBreakdown(BaseModel):
    ral: float
    contributi: float
    imponibile_irpef: float
    irpef_lorda: float
    detrazioni_lavoro: float
    detrazione_cuneo_fiscale: float
    somma_integrativa: float
    trattamento_integrativo: float
    irpef_netta: float
    addizionale_regionale: float
    addizionale_comunale: float
    netto_annuo: float
    netto_mensile: float