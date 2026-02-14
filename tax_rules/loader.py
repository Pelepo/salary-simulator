import importlib


def get_tax_rules(year: int):
    try:
        module = importlib.import_module(f"tax_rules._{year}")
        return module.TAX_RULES
    except ModuleNotFoundError:
        raise ValueError(f"Nessuna configurazione fiscale trovata per l'anno {year}")