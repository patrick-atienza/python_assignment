from typing import Any

from pydantic import BaseModel

from financial.entity.StatisticsModel import StatisticsModel


class StatisticsResponse(BaseModel):
    data: StatisticsModel
    info: Any = ''
