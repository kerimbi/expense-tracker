# Expense Tracker

A small command-line tool for tracking personal expenses. Data is stored in a local `expenses.json` file.

## Install

```
python -m venv venv
venv\Scripts\activate          # Windows (cmd)
source venv/bin/activate       # macOS / Linux
pip install -r requirements.txt
```

## Usage

```
python -m expense_tracker.cli add 1500 food "lunch" 2026-11-01
python -m expense_tracker.cli list
python -m expense_tracker.cli summary
python -m expense_tracker.cli delete 0
python -m expense_tracker.cli export csv      # text, csv or markdown
```

## Checks

```
python -m pytest -v
ruff check .
```

See `AGENTS.md` for AI-agent rules and `ACCEPTANCE_CRITERIA.md` for the acceptance criteria.
