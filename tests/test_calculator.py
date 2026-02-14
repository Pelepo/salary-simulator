import pytest

from salary.models import SalaryInput, TaxYear
from salary.calculator import calculate_salary
from salary.contributions import calculate_contributions
from salary.irpef import calculate_irpef
from salary.detrazioni import (
    calculate_employee_deduction,
    calculate_cuneo_fiscale_bonus
)
from salary.addizionali import (
    calculate_regional_additional,
    calculate_municipal_additional,
)
from tax_rules.loader import get_tax_rules

#Testing contributi previdenziali INPS
def test_contributions():
    ral = 30000
    rate = 0.0949

    expected= ral * rate

    result = calculate_contributions(ral, rate)

    assert result == pytest.approx(expected)

#Testing bracket IRPEF
#1
def test_irpef_first_bracket():
    imponibile = 20000
    brackets = [
        {"limit": 28000, "rate": 0.23},
        {"limit": 50000, "rate": 0.33},
        {"limit": None, "rate": 0.43},
    ]

    expected= imponibile * 0.23

    result = calculate_irpef(imponibile, brackets)

    assert result == pytest.approx(expected)

#2
def test_irpef_second_bracket():
    imponibile = 35000
    brackets = [
        {"limit": 28000, "rate": 0.23},
        {"limit": 50000, "rate": 0.33},
        {"limit": None, "rate": 0.43},
    ]

    expected= 28000 * 0.23 + 7000 * 0.33

    result = calculate_irpef(imponibile, brackets)

    assert result == pytest.approx(expected)
#3
def test_irpef_third_bracket():
    imponibile = 60000
    brackets = [
        {"limit": 28000, "rate": 0.23},
        {"limit": 50000, "rate": 0.33},
        {"limit": None, "rate": 0.43},
    ]

    expected= 28000 * 0.23 + 22000 * 0.33 + 10000 * 0.43

    result = calculate_irpef(imponibile, brackets)

    assert result == pytest.approx(expected)

#Testing taglio cuneo fiscale
#1
def test_employee_cuneo_fiscale_1():
    imponibile = 10000

    result = calculate_cuneo_fiscale_bonus(imponibile)

    expected = 0

    assert result == pytest.approx(expected)
#2
def test_employee_cuneo_fiscale_2():
    imponibile = 36000

    result = calculate_cuneo_fiscale_bonus(imponibile)

    expected = 1000 * (40000 - imponibile) / 8000

    assert result == pytest.approx(expected)

#Testing addizionali regionali
#1
def test_regional_additional_first_bracket():
    imponibile = 12000

    config = [
        {"limit": 15000, "rate": 0.0123},
        {"limit": 28000, "rate": 0.0158},
        {"limit": 50000, "rate": 0.0172},
        {"limit": None, "rate": 0.0173}
    ]

    result = calculate_regional_additional(imponibile, config)

    expected = 12000 * 0.0123

    assert result == pytest.approx(expected)

#2
def test_regional_additional_second_bracket():
    imponibile = 20000

    config = [
        {"limit": 15000, "rate": 0.0123},
        {"limit": 28000, "rate": 0.0158},
        {"limit": 50000, "rate": 0.0172},
        {"limit": None, "rate": 0.0173}
    ]

    result = calculate_regional_additional(imponibile, config)

    expected = 15000 * 0.0123 + 5000 * 0.0158

    assert result == pytest.approx(expected)

#3
def test_regional_additional_third_bracket():
    imponibile = 30000

    config = [
        {"limit": 15000, "rate": 0.0123},
        {"limit": 28000, "rate": 0.0158},
        {"limit": 50000, "rate": 0.0172},
        {"limit": None, "rate": 0.0173}
    ]

    result = calculate_regional_additional(imponibile, config)

    expected = 15000 * 0.0123 + 13000 * 0.0158 + 2000 * 0.0172

    assert result == pytest.approx(expected)

#4
def test_regional_additional_fourth_bracket():
    imponibile = 60000

    config = [
        {"limit": 15000, "rate": 0.0123},
        {"limit": 28000, "rate": 0.0158},
        {"limit": 50000, "rate": 0.0172},
        {"limit": None, "rate": 0.0173}
    ]

    result = calculate_regional_additional(imponibile, config)

    expected = 15000 * 0.0123 + 13000 * 0.0158 + 22000 * 0.0172 + 10000 * 0.0173

    assert result == pytest.approx(expected)


#Testing addizionali comunali
#1
def test_municipal_additional_first_bracket():
    imponibile = 20000

    config = {"lowerLimit": 23000, "rate": 0.008}

    result = calculate_municipal_additional(imponibile, config)

    expected = 0

    assert result == pytest.approx(expected)

#2
def test_municipal_additional_second_bracket():
    imponibile = 30000

    config = {"lowerLimit": 23000, "rate": 0.008}

    result = calculate_municipal_additional(imponibile, config)

    expected = 30000 * 0.008

    assert result == pytest.approx(expected)


#General Test sulla calculation
def test_full_salary_calculation():
    input_data = SalaryInput(
        ral=35000,
        mensilita=13,
        tax_year=TaxYear(year=2026),
    )

    result = calculate_salary(input_data)

    assert result.netto_annuo > 0
    assert result.netto_annuo < input_data.ral
    assert result.netto_mensile == pytest.approx(
        result.netto_annuo / input_data.mensilita
    )