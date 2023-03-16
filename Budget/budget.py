import calendar
from datetime import datetime


class Budget:
    def __init__(self, yearMonth: str, amount: int):
        self.yearMonth = yearMonth
        self.amount = amount

    def get_db_budget_datetime(self) -> datetime:
        return datetime.strptime(self.yearMonth, '%Y%m')

    def is_between(self, query_start_time: datetime, query_end_time: datetime) -> bool:
        return ~((self.get_db_budget_datetime() < query_start_time) or (self.get_db_budget_datetime() > query_end_time))

    def get_days_in_month(self) -> int:
        # 取得該月份的天數
        print(f"get_db_budget_datetime : {self.get_db_budget_datetime()}")
        print(f"last day : {calendar.monthrange(self.get_db_budget_datetime().year, self.get_db_budget_datetime().month)[1]}")
        return calendar.monthrange(self.get_db_budget_datetime().year, self.get_db_budget_datetime().month)[1]

    def calculate_budget_days_between(self, query_start_time:datetime, query_end_time: datetime):
        budget_datetime = self.get_db_budget_datetime()
        # print(f"budget_datetime: {budget_datetime}")
        # print(f"query_start_time: {query_start_time}")
        start_date = query_start_time if (budget_datetime.year == query_start_time.year and budget_datetime.month == query_start_time.month) else datetime(budget_datetime.year, budget_datetime.month, 1)
        # print(f"start_date: {start_date}")
        # print(f"query_end_time: {query_end_time}")
        end_date = query_end_time if (budget_datetime.year == query_end_time.year and budget_datetime.month == query_end_time.month) else datetime(budget_datetime.year, budget_datetime.month, self.get_days_in_month())
        # print(f"end_date: {end_date}")
        # if start_date == end_date:
        #     return 1
        return (end_date - start_date).days + 1

    def calculate_amount_between(self, query_start_time:datetime, query_end_time: datetime):
        if not self.is_between(query_start_time, query_end_time):
           return 0.0
        print(f'amount:{self.amount} , days: {self.calculate_budget_days_between(query_start_time, query_end_time)} , last day:{self.get_days_in_month()}')
        return float(self.amount) * self.calculate_budget_days_between(query_start_time, query_end_time) / self.get_days_in_month()

    def get_amount(self):
        return self.amount
