# AGENTS.md — Expense Tracker

Instructions for AI coding agents (Claude, Codex, Copilot, etc.) working in this repository.
If your tool does not load this file automatically, the human operator must paste it into the prompt.

## 1. Purpose

A small command-line tool for tracking personal expenses. Expenses are stored in a local
JSON file (`expenses.json`). It is a learning project: no server, no network, no real personal data.

## 2. Architecture

| Path | Responsibility |
|---|---|
| `expense_tracker/cli.py` | Entry point. Parses arguments (`argparse`) and prints results. No business logic here. |
| `expense_tracker/tracker.py` | `ExpenseTracker`: add, list, delete, totals, export. Business logic lives here. |
| `expense_tracker/models.py` | `Expense` dataclass and dict conversion. |
| `expense_tracker/storage.py` | Load/save the JSON data file. |
| `expense_tracker/formatters.py` | Report formatters (text / csv / markdown) — Strategy pattern. |
| `tests/` | `pytest` tests. Each test uses a temporary data file (`tmp_path`). |

Data flow: `cli.py` → `ExpenseTracker` → `storage.py` → `expenses.json`.

## 3. Setup (Windows `cmd`; use `source venv/bin/activate` on macOS/Linux)

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Always run Python **through the activated venv** using `python -m ...`. This machine also has
other interpreters (e.g. Anaconda); calling a bare script may silently use the wrong one.

## 4. Safe commands (allowed without asking)

```
python -m pytest -v                 # run all tests
ruff check .                        # lint
python -m expense_tracker.cli --help
python -m expense_tracker.cli list
git status / git diff / git log --oneline
```

Commands that write data (`add`, `delete`) may only be run in a temporary directory or
against a throwaway data file — never against a user's real `expenses.json`.

## 5. Coding conventions

- Python 3.12+, standard library only for application code.
- Keep business logic out of `cli.py`.
- Never use a bare `except:`; catch specific exceptions and do not silently discard data.
- Invalid input must raise a clear exception (e.g. `ValueError`, `IndexError` or a custom error class),
  and the CLI must print an error message and exit with a non-zero code.
- `ruff check .` must report no errors.

## 6. Test expectations

- Every behaviour change or bug fix comes with a test that fails before and passes after the fix.
- All tests must pass before a change is proposed: `python -m pytest -v`.
- Tests must not touch the real `expenses.json`; use `tmp_path`.
- Do not delete, skip or weaken existing tests to make a change pass.
- Acceptance criteria in `ACCEPTANCE_CRITERIA.md` must remain true.

## 7. Forbidden actions

- Do **not** add, read, print or commit secrets, tokens, passwords or real personal data.
- Do **not** deploy, publish or push to any remote (`git push`, `pip upload`, etc.).
- Do **not** run destructive commands: `rm -rf`, `del /s`, `git reset --hard`, `git push --force`,
  `git clean -fdx`, or deleting/overwriting `expenses.json`.
- Do **not** add, remove or upgrade dependencies (`pip install <pkg>`, editing `requirements.txt`)
  without explicit human approval.
- Do **not** change the JSON data format without a migration plan approved by a human.
- Do **not** modify files outside this repository.

## 8. Review gates

1. The agent proposes a change as a diff with a short summary and the test output.
2. A human reviews the diff, reruns `python -m pytest -v` and `ruff check .`.
3. Only the human commits, merges or pushes.
