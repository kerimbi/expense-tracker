"""Report formatters (Strategy pattern).

Each formatter takes the list of expenses and the total, and returns the report as a string.
To add a new format, write one function and register it in FORMATTERS — no other code changes.
"""


def format_text(expenses, total):
    lines = [
        f"{i}. {e.date} | {e.category} | {e.description} | {e.amount}"
        for i, e in enumerate(expenses)
    ]
    lines.append(f"TOTAL: {total}")
    return "\n".join(lines)


def format_csv(expenses, total):
    lines = ["date,category,description,amount"]
    lines += [f"{e.date},{e.category},{e.description},{e.amount}" for e in expenses]
    return "\n".join(lines)


def format_markdown(expenses, total):
    lines = ["| Date | Category | Description | Amount |", "|---|---|---|---|"]
    lines += [f"| {e.date} | {e.category} | {e.description} | {e.amount} |" for e in expenses]
    lines.append(f"| | | **TOTAL** | {total} |")
    return "\n".join(lines)


FORMATTERS = {
    "text": format_text,
    "csv": format_csv,
    "markdown": format_markdown,
}
