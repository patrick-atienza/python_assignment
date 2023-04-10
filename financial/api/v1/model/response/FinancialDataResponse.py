from pydantic import BaseModel, PositiveInt

from financial.entity.FinancialDataEntity import FinancialData


class FinancialDataPagination(BaseModel):
    count: PositiveInt
    page: PositiveInt
    limit: PositiveInt
    pages: PositiveInt


class FinancialDataResponse(BaseModel):
    data: list[FinancialData]
    pagination: FinancialDataPagination
