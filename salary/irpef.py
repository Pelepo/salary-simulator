# Funzione per il calcolo dell'IRPEF nazionale

def calculate_irpef(imponibile: float, brackets: list) -> float:
    tax = 0
    previous_limit = 0

    for bracket in brackets:
        limit = bracket["limit"]
        rate = bracket["rate"]

        if limit is None:
            tax += (imponibile - previous_limit) * rate
            break

        if imponibile > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (imponibile - previous_limit) * rate
            break

    return tax

