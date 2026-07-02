"""Currency formatting for CLI output."""


def format_currency(amount: float) -> str:
    return f"${amount:.2f}"
