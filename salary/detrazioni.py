# Funzione per il calcolo di eventuali detrazioni per il lavoratore

def calculate_employee_deduction(imponibile: float, ral: float) -> float:

    if imponibile <= 15000:
        detrazione = 1955

    elif imponibile <= 28000:
        detrazione = 1910 + 1190 * (28000 - imponibile) / 13000

    elif imponibile <= 50000:
        detrazione = 1910 * (50000 - imponibile) / 22000

    else:
        detrazione = 0

    # Maggiorazione 65€ tra 25k e 35k
    if 25000 <= ral <= 35000:
        detrazione += 65

    return detrazione


def calculate_cuneo_fiscale_bonus(ral: float) -> float:

    if ral <= 20000:
        return 0

    if ral <= 32000:
        return 1000

    if ral <= 40000:
        return 1000 * (40000 - ral) / 8000

    return 0

