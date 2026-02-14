# Funzione per il calcolo di eventuali detrazioni per il lavoratore

def calculate_employee_deduction(imponibile: float) -> float:
    
    if imponibile <= 15000:
        return 1955

    if imponibile <= 28000:
        return 1910 + 1190 * (28000 - imponibile) / 13000

    if imponibile <= 50000:
        return 1910 * (50000 - imponibile) / 22000

    return 0
