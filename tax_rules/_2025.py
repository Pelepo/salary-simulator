TAX_RULES = {
    "year": 2025,

    "contributions": {
        "employee_rate": 0.0919
    },

    "irpef": {
        "brackets": [
            {"limit": 28000, "rate": 0.23},
            {"limit": 50000, "rate": 0.35},
            {"limit": None, "rate": 0.43}
        ]
    },

    "addizionali": {
        "regionale": 0.0123,
        "comunale": 0.008
    },

    "detrazioni": {
        "lavoro_dipendente": {
            "soglia_bassa": 15000,
            "soglia_alta": 50000,
            "importo_base": 1910
        }
    }
}
