import datetime
from decimal import Decimal
from typing import Any

import peewee
from peewee import TextField, DateField, DecimalField, IntegerField, CompositeKey, Model
from pydantic import BaseModel
from pydantic.utils import GetterDict

from financial.database import db


class FinancialDataEntity(Model):
    symbol = TextField()
    date = DateField()
    open_price = DecimalField()
    close_price = DecimalField()
    volume = IntegerField()

    class Meta:
        database = db
        table_name = 'financial_data'
        primary_key = CompositeKey('symbol', 'date')


def create_financial_data_table() -> None:
    db.create_tables([FinancialDataEntity])


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class FinancialData(BaseModel):
    symbol: str
    date: datetime.date
    open_price: Decimal
    close_price: Decimal
    volume: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
