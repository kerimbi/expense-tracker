import argparse

from .tracker import ExpenseTracker


def main(argv=None):
    parser = argparse.ArgumentParser(description="Simple expense tracker")
    sub = parser.add_subparsers(dest="command")

    add = sub.add_parser("add", help="Add an expense")
    add.add_argument("amount")
    add.add_argument("category")
    add.add_argument("description")
    add.add_argument("date")

    sub.add_parser("list", help="List expenses")

    delete = sub.add_parser("delete", help="Delete expense by index")
    delete.add_argument("index", type=int)

    sub.add_parser("summary", help="Totals by category")

    export = sub.add_parser("export", help="Export report")
    export.add_argument("format", help="text, csv or markdown")

    args = parser.parse_args(argv)
    tracker = ExpenseTracker()

    if args.command == "add":
        e = tracker.add_expense(args.amount, args.category, args.description, args.date)
        print(f"Added: {e}")
    elif args.command == "list":
        for i, e in enumerate(tracker.list_expenses()):
            print(f"{i}. {e.date} {e.category} {e.description} {e.amount}")
    elif args.command == "delete":
        e = tracker.delete_expense(args.index)
        print(f"Deleted: {e}")
    elif args.command == "summary":
        for cat, total in tracker.total_by_category().items():
            print(f"{cat}: {total}")
        print(f"TOTAL: {tracker.total()}")
    elif args.command == "export":
        print(tracker.export_report(args.format))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
