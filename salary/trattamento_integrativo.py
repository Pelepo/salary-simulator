def calculate_trattamento_integrativo(
    reddito_complessivo: float,
    irpef_lorda: float,
    detrazioni_totali: float
) -> float:

    BONUS_MAX = 1200.0

    if reddito_complessivo <= 15000:
        return BONUS_MAX

    elif reddito_complessivo <= 28000:
        capienza = detrazioni_totali - irpef_lorda
        
        if capienza > 0:
            return min(BONUS_MAX, capienza)
        
        return 0.0

    return 0.0
