# Funzioni per il calcolo dell'addizionale regionale e comunale

def calculate_regional_additional(imponibile: float, brackets: list) -> float:
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



def calculate_municipal_additional(imponibile: float, rules: dict) -> float:

    if imponibile > rules["lowerLimit"]:
        return imponibile * rules["rate"]
    else:
        return 0