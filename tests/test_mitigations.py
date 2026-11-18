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


# --- R2: corrupted data file silently discarded and then overwritten ----------

CORRUPTED = '[{"amount": 100, "category": "food", "description": "a", "date": "2026-11-01"}, {"amount": 5}]'


def test_corrupted_file_raises_storage_error(tmp_path):
    from expense_tracker.storage import StorageError

    path = tmp_path / "expenses.json"
    path.write_text(CORRUPTED)
    with pytest.raises(StorageError):
        ExpenseTracker(path=str(path))


def test_invalid_json_raises_storage_error(tmp_path):
    from expense_tracker.storage import StorageError

    path = tmp_path / "expenses.json"
    path.write_text("{broken")
    with pytest.raises(StorageError):
        ExpenseTracker(path=str(path))


def test_cli_does_not_overwrite_corrupted_file(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "expenses.json").write_text(CORRUPTED)
    exit_code = main(["add", "200", "food", "b", "2026-11-02"])
    assert exit_code == 1
    assert "Error" in capsys.readouterr().err
    assert (tmp_path / "expenses.json").read_text() == CORRUPTED  # original data kept
