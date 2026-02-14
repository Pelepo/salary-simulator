# Motore di aggregazione di tutte le funzioni per il calcolo da RAL a NETTO

from salary.models import SalaryInput, SalaryBreakdown
from salary.contributions import calculate_contributions
from salary.irpef import calculate_irpef
from salary.addizionali import (
    calculate_regional_additional,
    calculate_municipal_additional,
)
from salary.detrazioni import (
    calculate_employee_deduction,
    calculate_cuneo_fiscale_bonus
)
from salary.somma_integrativa import calculate_somma_integrativa
from tax_rules.loader import get_tax_rules


def calculate_salary(input_data: SalaryInput) -> SalaryBreakdown:

    rules = get_tax_rules(input_data.tax_year.year)

    ral = input_data.ral

    # 1 Contributi Previdenziali Lavoratore
    contrib_rate = rules["contributions"]["employee_rate"]
    contributi = calculate_contributions(ral, contrib_rate)

    # 2 Reddito Imponibile Fiscale
    imponibile = ral - contributi

    # 3 IRPEF
    brackets = rules["irpef"]["brackets"]
    irpef_lorda = calculate_irpef(imponibile, brackets)

    # 4 Detrazioni Lavoro Dipendente
    detrazioni_lavoro = calculate_employee_deduction(imponibile, ral)
    detrazione_cuneo_fiscale= calculate_cuneo_fiscale_bonus(ral)
    detrazioni = detrazioni_lavoro + detrazione_cuneo_fiscale

    irpef_netta = max(irpef_lorda - detrazioni, 0)

    # 5 Addizionale Regionale e Comunale
    add_regionale = calculate_regional_additional(
        imponibile, rules["addizionali"]["regionale"]["brackets"]
    )

    add_comunale = calculate_municipal_additional(
        imponibile, rules["addizionali"]["comunale"]
    )

    #6 Somma Integrativa
    somma_integrativa = calculate_somma_integrativa(ral)

    # 6 Sipendio Mensile Netto
    netto_annuo = ral - contributi - irpef_netta - add_regionale - add_comunale + somma_integrativa
    netto_mensile = netto_annuo / input_data.mensilita

    return SalaryBreakdown(
        ral=ral,
        contributi=contributi,
        imponibile_irpef=imponibile,
        irpef_lorda=irpef_lorda,
        detrazioni_lavoro=detrazioni_lavoro,
        detrazione_cuneo_fiscale=detrazione_cuneo_fiscale,
        somma_integrativa=somma_integrativa,
        irpef_netta=irpef_netta,
        addizionale_regionale=add_regionale,
        addizionale_comunale=add_comunale,
        netto_annuo=netto_annuo,
        netto_mensile=netto_mensile,
    )
