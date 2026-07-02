"""Payroll arithmetic."""

HOURLY_RATE = 25.0
TAX_RATE = 0.2


def compute_gross(hours: float) -> float:
    return round(hours * HOURLY_RATE, 2)


def compute_net(gross: float, tax_rate: float) -> float:
    return round(gross * (1.0 - tax_rate), 2)
