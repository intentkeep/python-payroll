"""Summarise payroll totals for all known employees (CLI command surface)."""

import sys

from payroll_cli.lib.validation import KNOWN_EMPLOYEES
from payroll_cli.lib.calculation import compute_gross, compute_net, TAX_RATE
from payroll_cli.lib.formatting import format_currency


DEFAULT_HOURS = 40.0


def run() -> int:
    """
    CLI response boundary: prints a summary line with employee count and total
    net pay for the default 40-hour week (exit 0).
    """
    total_net = 0.0
    for employee_id in sorted(KNOWN_EMPLOYEES):
        gross = compute_gross(DEFAULT_HOURS)
        total_net += compute_net(gross, TAX_RATE)

    print(
        f"employees={len(KNOWN_EMPLOYEES)} "
        f"total_net={format_currency(total_net)} "
        f"hours={DEFAULT_HOURS}"
    )
    return 0
