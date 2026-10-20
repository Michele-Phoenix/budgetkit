"""Money calculations used by the expense tracker."""


def total(amounts):
    """Add up a list of amounts."""
    return sum(amounts)


def average(amounts):
    """Return the average amount, or 0 if the list is empty."""
    if not amounts:
        return 0
    return sum(amounts) / len(amounts)


def highest(amounts):
    """Return the largest amount, or 0 if the list is empty."""
    if not amounts:
        return 0
    return max(amounts)


def category_totals(expenses):
    """
    Take a list of (category, amount) pairs and return a dictionary
    of total per category, biggest first.

    Example: [("Food", 10), ("Bills", 50), ("Food", 5)]
    gives    {"Bills": 50, "Food": 15}
    """
    totals = {}
    for category, amount in expenses:
        totals[category] = totals.get(category, 0) + amount
    return dict(sorted(totals.items(), key=lambda item: item[1], reverse=True))


def percentage_breakdown(totals):
    """Turn category totals into percentages of the grand total."""
    grand_total = sum(totals.values())
    if grand_total == 0:
        return {name: 0 for name in totals}
    return {
        name: round(amount / grand_total * 100, 1)
        for name, amount in totals.items()
    }


def budget_status(spent, budget):
    """Say whether spending is within the budget."""
    if spent > budget:
        return "Over budget"
    return "Within budget"