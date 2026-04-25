"""Smoke tests for macroeconomics calculators."""

from gdp_calculator import calculate_gdp
from inflation_rate_calculator import calculate_inflation_rate
from unemployment_rate_calculator import calculate_unemployment_rate


def test_gdp_expenditure() -> None:
    result = calculate_gdp(consumption=1000, investment=500, government=300, net_exports=50)
    assert result == 1850.0


def test_inflation_rate() -> None:
    rate = calculate_inflation_rate(index_current=105, index_previous=100)
    assert abs(rate - 5.0) < 1e-9


def test_unemployment_rate() -> None:
    rate = calculate_unemployment_rate(unemployed=500, labor_force=10000)
    assert abs(rate - 5.0) < 1e-9
