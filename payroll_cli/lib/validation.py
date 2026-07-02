"""Employee and hours validation."""

KNOWN_EMPLOYEES = frozenset({"emp-001", "emp-002", "emp-003"})
MAX_BILLABLE_HOURS_PER_WEEK = 168


def validate_employee_id(employee_id: str) -> None:
    if employee_id not in KNOWN_EMPLOYEES:
        raise ValueError("PAYROLL_UNKNOWN_EMPLOYEE")


def validate_hours(hours: float) -> None:
    if hours <= 0 or hours > MAX_BILLABLE_HOURS_PER_WEEK:
        raise ValueError("PAYROLL_INVALID_HOURS")
