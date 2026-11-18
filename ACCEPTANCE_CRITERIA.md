# Acceptance Criteria

These must remain true after every change. Verified by `python -m pytest -v` and the manual CLI checks below.

| ID | Criterion | How it is verified |
|---|---|---|
| AC1 | All existing tests pass. | `python -m pytest -v` |
| AC2 | A valid expense can be added, listed and deleted from the CLI, and data persists between runs. | `test_add_expense`, `test_delete_expense`, `test_data_persists`; manual `add` → `list` |
| AC3 | `total()` and `total_by_category()` return correct sums for valid data. | `test_total`, `test_total_by_category` |
| AC4 | `export text`, `export csv` and `export markdown` produce the same output as the baseline version for the same data. | `tests/test_export.py` (characterization tests written before refactoring) |
| AC5 | An `expenses.json` file created by the baseline version still loads without changes (data format unchanged). | `test_data_persists`; `test_baseline_file_format_loads` |
