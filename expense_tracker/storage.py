import json
import os

from .models import Expense

DATA_FILE = "expenses.json"


def load_expenses(path=DATA_FILE):
    if not os.path.exists(path):
        return []
    try:
        with open(path) as f:
            data = json.load(f)
        return [Expense.from_dict(item) for item in data]
    except:
        return []


def save_expenses(expenses, path=DATA_FILE):
    with open(path, "w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=2)
