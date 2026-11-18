from dataclasses import dataclass, asdict


@dataclass
class Expense:
    amount: float
    category: str
    description: str
    date: str  # expected format: YYYY-MM-DD

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data):
        return Expense(
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            date=data["date"],
        )
