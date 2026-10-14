# budgetkit

Small helpers for expense totals, category breakdowns and money formatting.

## Install

    pip install budgetkit-michele

## Usage

    from budgetkit import total, format_money

    print(format_money(total([10, 20, 30])))   # $60.00

## Used in

This package is used by the Expense Tracker Django project in this repository.