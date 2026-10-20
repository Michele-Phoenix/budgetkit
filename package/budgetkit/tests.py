import unittest

from budgetkit import (
    total,
    average,
    highest,
    category_totals,
    percentage_breakdown,
    budget_status,
    format_money,
)


class CalculationTests(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total([10, 20, 30]), 60)

    def test_average(self):
        self.assertEqual(average([10, 20, 30]), 20)

    def test_average_of_empty_list(self):
        self.assertEqual(average([]), 0)

    def test_highest(self):
        self.assertEqual(highest([5, 50, 20]), 50)

    def test_category_totals(self):
        data = [("Food", 10), ("Bills", 50), ("Food", 5)]
        self.assertEqual(category_totals(data), {"Bills": 50, "Food": 15})

    def test_percentage_breakdown(self):
        result = percentage_breakdown({"Bills": 75, "Food": 25})
        self.assertEqual(result, {"Bills": 75.0, "Food": 25.0})

    def test_budget_status(self):
        self.assertEqual(budget_status(500, 1000), "Within budget")
        self.assertEqual(budget_status(1500, 1000), "Over budget")


class FormattingTests(unittest.TestCase):
    def test_format_money(self):
        self.assertEqual(format_money(1234.5), "$1,234.50")


if __name__ == "__main__":
    unittest.main()