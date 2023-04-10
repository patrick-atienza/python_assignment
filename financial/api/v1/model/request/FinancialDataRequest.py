import datetime
from typing import Annotated, Union

from fastapi import Query
from pydantic import BaseModel

DEFAULT_LIMIT = 5
DEFAULT_PAGE = 1


class FinancialDataRequest(BaseModel):
    start_date: Union[datetime.date, None] = None
    end_date: Union[datetime.date, None] = None
    symbol: str
    limit: Annotated[int, Query(ge=1)] = DEFAULT_LIMIT
    page: Annotated[int, Query(ge=1)] = DEFAULT_PAGE
