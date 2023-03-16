from typing import List
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Budget:
    year_month: str
    amount: int


class BudgetRepo:

    def get_all(self) -> List[Budget]:
        return NotImplementedError


class BudgetService:

    def __init__(self):
        self.budgetRepo = BudgetRepo()
        self.budgets = self.budgetRepo.get_all()

    def has_data(self):
        if self.budgets:
            return True
        return False

    def is_valid(self, start_dt, end_dt):
        return end_dt > start_dt

    def query(self, start_dt, end_dt) -> float:
        if self.is_valid(start_dt, end_dt):
            return 0.0