from .formatters import FORMATTERS
from .models import Expense
from .storage import load_expenses, save_expenses


class ExpenseTracker:
    def __init__(self, path="expenses.json"):
        self.path = path
        self.expenses = load_expenses(path)

    def add_expense(self, amount, category, description, date):
        expense = Expense(float(amount), category, description, date)
        self.expenses.append(expense)
        save_expenses(self.expenses, self.path)
        return expense

    def list_expenses(self):
        return list(self.expenses)

    def delete_expense(self, index):
        removed = self.expenses.pop(index)
        save_expenses(self.expenses, self.path)
        return removed

    def total(self):
        return sum(e.amount for e in self.expenses)

    def total_by_category(self):
        totals = {}
        for e in self.expenses:
            totals[e.category] = totals.get(e.category, 0) + e.amount
        return totals

    def export_report(self, fmt):
        formatter = FORMATTERS.get(fmt)
        if formatter is None:
            return ""
        return formatter(self.expenses, self.total())
