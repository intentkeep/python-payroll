"""Calculate payroll for a single employee (CLI command surface)."""

import sys

from payroll_cli.lib.validation import validate_hours, validate_employee_id
from payroll_cli.lib.calculation import compute_gross, compute_net, TAX_RATE
from payroll_cli.lib.formatting import format_currency


def run(employee_id: str, hours: float) -> int:
    """
    CLI response boundary: prints gross and net on success (exit 0) or the error
    code PAYROLL_UNKNOWN_EMPLOYEE / PAYROLL_INVALID_HOURS on stderr (exit 1).
    """
    try:
        validate_employee_id(employee_id)
        gross = compute_gross(hours)
        net = compute_net(gross, TAX_RATE)
        print(f"gross={format_currency(gross)} net={format_currency(net)} employee={employee_id}")
        return 0
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 1
