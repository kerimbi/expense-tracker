from expense_tracker.tracker import ExpenseTracker


def make_tracker(tmp_path):
    return ExpenseTracker(path=str(tmp_path / "expenses.json"))


def test_add_expense(tmp_path):
    t = make_tracker(tmp_path)
    t.add_expense(1500, "food", "lunch", "2026-11-01")
    assert len(t.list_expenses()) == 1


def test_total(tmp_path):
    t = make_tracker(tmp_path)
    t.add_expense(1000, "food", "lunch", "2026-11-01")
    t.add_expense(500, "transport", "bus", "2026-11-02")
    assert t.total() == 1500


def test_total_by_category(tmp_path):
    t = make_tracker(tmp_path)
    t.add_expense(1000, "food", "lunch", "2026-11-01")
    t.add_expense(2000, "food", "dinner", "2026-11-01")
    t.add_expense(500, "transport", "bus", "2026-11-02")
    assert t.total_by_category() == {"food": 3000, "transport": 500}


def test_delete_expense(tmp_path):
    t = make_tracker(tmp_path)
    t.add_expense(1000, "food", "lunch", "2026-11-01")
    t.delete_expense(0)
    assert t.list_expenses() == []


def test_data_persists(tmp_path):
    t = make_tracker(tmp_path)
    t.add_expense(1000, "food", "lunch", "2026-11-01")
    t2 = make_tracker(tmp_path)
    assert len(t2.list_expenses()) == 1


def test_export_text(tmp_path):
    t = make_tracker(tmp_path)
    t.add_expense(1000, "food", "lunch", "2026-11-01")
    report = t.export_report("text")
    assert "TOTAL: 1000" in report
