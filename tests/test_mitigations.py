"""Regression tests for mitigated risks."""
import pytest

from expense_tracker.cli import main
from expense_tracker.tracker import ExpenseTracker


def make_tracker(tmp_path):
    return ExpenseTracker(path=str(tmp_path / "expenses.json"))


# --- R1: delete with negative / out-of-range index ---------------------------

def test_delete_negative_index_is_rejected(tmp_path):
    t = make_tracker(tmp_path)
    t.add_expense(1000, "food", "lunch", "2026-11-01")
    t.add_expense(500, "transport", "bus", "2026-11-02")
    with pytest.raises(IndexError):
        t.delete_expense(-1)
    assert len(t.list_expenses()) == 2  # nothing was deleted


def test_delete_out_of_range_index_is_rejected(tmp_path):
    t = make_tracker(tmp_path)
    t.add_expense(1000, "food", "lunch", "2026-11-01")
    with pytest.raises(IndexError):
        t.delete_expense(5)
    assert len(t.list_expenses()) == 1


def test_cli_delete_negative_index_prints_error(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    main(["add", "1000", "food", "lunch", "2026-11-01"])
    exit_code = main(["delete", "-1"])
    assert exit_code == 1
    assert "Error" in capsys.readouterr().err
    assert len(ExpenseTracker().list_expenses()) == 1
