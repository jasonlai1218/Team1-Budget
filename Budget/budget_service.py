from datetime import datetime
from typing import List

from Budget.budget import Budget


# Budget DB類別
class BudgetRepository:
    def get_all(self) -> List[Budget]:
        pass


# Budget查詢機制
class BudgetService:

    def __init__(self, budget_repository: BudgetRepository):
        self.budget_repository = budget_repository

    def query(self, start: datetime, end: datetime) -> float:
        if end < start:
            return 0
        return sum([budget.calculate_amount_between(start, end) for budget in self.budget_repository.get_all()])
