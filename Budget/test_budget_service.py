import unittest
from datetime import datetime
from typing import List
from unittest.mock import patch

from Budget.budget import Budget
from Budget.budget_service import BudgetService, BudgetRepository
from unittest.mock import MagicMock


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.mock_budget_repo = MagicMock(spec=BudgetRepository)
        self.budgetService = BudgetService(self.mock_budget_repo)
        # get_all_patcher = patch('Budget.budget_service.BudgetRepository.getAll')
        # self.fake_get_all = get_all_patcher.start()

    def given_budget(self, budgets: List[Budget]):
        # self.fake_get_all.return_value = budgets
        self.mock_budget_repo.get_all.return_value = budgets

    def budget_between_should_be(self, start: datetime, end: datetime, expected_amount: float):
        actual = self.budgetService.query(start, end)
        print(f'actual:{actual}')
        assert actual == expected_amount

    def test_full_month(self):
        self.given_budget([Budget("202301", 310)])
        self.budget_between_should_be(datetime(2023, 1, 1), datetime(2023, 1, 31), 310.0)

    def test_part_month(self):
        self.given_budget([Budget("202301", 310)])
        self.budget_between_should_be(datetime(2023, 1, 1), datetime(2023, 1, 10), 100.0)

    def test_one_day(self):
        self.given_budget([Budget("202303", 31)])
        self.budget_between_should_be(datetime(2023, 3, 1), datetime(2023, 3, 1), 1.0)

    def test_cross_month(self):
        self.given_budget([Budget("202303", 31), Budget("202304", 300)])
        self.budget_between_should_be(datetime(2023, 3, 31), datetime(2023, 4, 3), 31.0)

    def test_cross_three_months(self):
        self.given_budget([Budget("202303", 31), Budget("202304", 300), Budget("202305", 3100)])
        self.budget_between_should_be(datetime(2023, 3, 28), datetime(2023, 5, 30), 3304.0)


if __name__ == '__main__':
    unittest.main()
