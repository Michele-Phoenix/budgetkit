"""Helpers for displaying money."""


def format_money(amount, symbol="$"):
    """Format a number as money, e.g. 1234.5 becomes $1,234.50."""
    return f"{symbol}{amount:,.2f}"
