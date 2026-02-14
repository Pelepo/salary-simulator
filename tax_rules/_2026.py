TAX_RULES = {
    "year": 2026,

    "contributions": {
        "employee_rate": 0.0949
    },

    "irpef": {
        "brackets": [
            {"limit": 28000, "rate": 0.23},
            {"limit": 50000, "rate": 0.33},
            {"limit": None, "rate": 0.43}
        ]
    },

    "addizionali": {
        "regionale": {
            "brackets": [
                {"limit": 15000, "rate": 0.0123},
                {"limit": 28000, "rate": 0.0158},
                {"limit": 50000, "rate": 0.0172},
                {"limit": None, "rate": 0.0173}
            ]
        },
        "comunale": 
            {"lowerLimit": 23000, "rate": 0.008},
    },

    "detrazioni": {
        "lavoro_dipendente": {
            "soglia_bassa": 15000,
            "soglia_alta": 50000,
            "importo_base": 1910
        }
    }
}
