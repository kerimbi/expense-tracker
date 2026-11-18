# Expense Tracker

A small command-line tool for tracking personal expenses. Data is stored in a local `expenses.json` file.

## Install

```
pip install -r requirements.txt
```

## Usage

```
python main.py add 1500 food "lunch" 2026-11-01
python main.py list
python main.py summary
python main.py delete 0
python main.py export csv
```

## Tests

```
pytest
```
