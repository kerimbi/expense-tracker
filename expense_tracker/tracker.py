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
        if fmt == "text":
            lines = []
            for i, e in enumerate(self.expenses):
                lines.append(f"{i}. {e.date} | {e.category} | {e.description} | {e.amount}")
            lines.append(f"TOTAL: {self.total()}")
            return "\n".join(lines)
        elif fmt == "csv":
            lines = ["date,category,description,amount"]
            for e in self.expenses:
                lines.append(f"{e.date},{e.category},{e.description},{e.amount}")
            return "\n".join(lines)
        elif fmt == "markdown":
            lines = ["| Date | Category | Description | Amount |", "|---|---|---|---|"]
            for e in self.expenses:
                lines.append(f"| {e.date} | {e.category} | {e.description} | {e.amount} |")
            lines.append(f"| | | **TOTAL** | {self.total()} |")
            return "\n".join(lines)
        else:
            return ""
