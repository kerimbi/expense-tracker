"""Characterization tests: lock in the baseline export output before refactoring (AC4)."""
import json

from expense_tracker.tracker import ExpenseTracker


def make_tracker(tmp_path):
    t = ExpenseTracker(path=str(tmp_path / "expenses.json"))
    t.add_expense(1000, "food", "lunch", "2026-11-01")
    t.add_expense(500, "transport", "bus", "2026-11-02")
    return t


def test_export_text_exact(tmp_path):
    t = make_tracker(tmp_path)
    assert t.export_report("text") == (
        "0. 2026-11-01 | food | lunch | 1000.0\n"
        "1. 2026-11-02 | transport | bus | 500.0\n"
        "TOTAL: 1500.0"
    )


def test_export_csv_exact(tmp_path):
    t = make_tracker(tmp_path)
    assert t.export_report("csv") == (
        "date,category,description,amount\n"
        "2026-11-01,food,lunch,1000.0\n"
        "2026-11-02,transport,bus,500.0"
    )


def test_export_markdown_exact(tmp_path):
    t = make_tracker(tmp_path)
    assert t.export_report("markdown") == (
        "| Date | Category | Description | Amount |\n"
        "|---|---|---|---|\n"
        "| 2026-11-01 | food | lunch | 1000.0 |\n"
        "| 2026-11-02 | transport | bus | 500.0 |\n"
        "| | | **TOTAL** | 1500.0 |"
    )


def test_export_unknown_format_returns_empty(tmp_path):
    t = make_tracker(tmp_path)
    assert t.export_report("pdf") == ""


def test_baseline_file_format_loads(tmp_path):
    """AC5: a data file written in the baseline format still loads."""
    path = tmp_path / "expenses.json"
    path.write_text(json.dumps([
        {"amount": 250.0, "category": "food", "description": "tea", "date": "2026-11-05"}
    ]))
    t = ExpenseTracker(path=str(path))
    assert t.total() == 250.0
