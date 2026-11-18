import json
import os

from .models import Expense

DATA_FILE = "expenses.json"


class StorageError(Exception):
    """The data file exists but cannot be read safely."""


def load_expenses(path=DATA_FILE):
    if not os.path.exists(path):
        return []
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return [Expense.from_dict(item) for item in data]
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        raise StorageError(
            f"Data file '{path}' is corrupted and was not changed ({exc!r}). "
            "Fix or move the file, then try again."
        ) from exc


def save_expenses(expenses, path=DATA_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=2)
