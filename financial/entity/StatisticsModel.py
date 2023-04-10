import datetime
from decimal import Decimal

from pydantic import BaseModel


class StatisticsModel(BaseModel):
    start_date: datetime.date
    end_date: datetime.date
    symbol: str
    average_daily_open_price: Decimal
    average_daily_close_price: Decimal
    average_daily_volume: Decimal
