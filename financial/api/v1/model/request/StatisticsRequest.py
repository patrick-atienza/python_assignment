import datetime

from pydantic import BaseModel


class StatisticsRequest(BaseModel):
    start_date: datetime.date
    end_date: datetime.date
    symbol: str
