from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from budgetkit import (
    total,
    average,
    highest,
    category_totals,
    percentage_breakdown,
    budget_status,
    format_money,
)

from .forms import ExpenseForm
from .models import Expense


def expense_list(request):
    """Show all expenses and a form to add a new one."""
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expense_list")
    else:
        form = ExpenseForm()

    expenses = Expense.objects.all()
    for expense in expenses:
        expense.display_amount = format_money(expense.amount)

    return render(request, "tracker/expense_list.html", {
        "expenses": expenses,
        "form": form,
    })


@require_POST
def expense_delete(request, pk):
    """Delete one expense, then go back to the list."""
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect("expense_list")

def expense_edit(request, pk):
    """Edit an existing expense."""
    expense = get_object_or_404(Expense, pk=pk)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("expense_list")
    else:
        form = ExpenseForm(instance=expense)

    return render(request, "tracker/expense_edit.html", {
        "form": form,
        "expense": expense,
    })


def summary(request):
    """Show statistics, calculated by our own budgetkit package."""
    expenses = Expense.objects.all()

    amounts = [e.amount for e in expenses]
    pairs = [(e.category, e.amount) for e in expenses]

    spent = total(amounts)
    budget = settings.MONTHLY_BUDGET
    totals = category_totals(pairs)
    percents = percentage_breakdown(totals)

    rows = [
        {
            "category": category,
            "total": format_money(amount),
            "percent": percents[category],
        }
        for category, amount in totals.items()
    ]

    return render(request, "tracker/summary.html", {
        "count": len(amounts),
        "spent": format_money(spent),
        "average": format_money(average(amounts)),
        "highest": format_money(highest(amounts)),
        "budget": format_money(budget),
        "remaining": format_money(budget - spent),
        "status": budget_status(spent, budget),
        "rows": rows,
    })