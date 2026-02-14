def calculate_somma_integrativa(ral: float) -> float:

    if ral <= 8500:
        return ral * 0.071

    elif ral <= 15000:
        return ral * 0.053

    elif ral <= 20000:
        return ral * 0.048

    return 0.0
