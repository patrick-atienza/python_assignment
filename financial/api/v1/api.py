import math
import statistics
import uvicorn

from fastapi import Depends
from financial.entity.StatisticsModel import StatisticsModel
from financial.api.v1.model.request.FinancialDataRequest import FinancialDataRequest
from financial.api.v1.model.request.StatisticsRequest import StatisticsRequest
from financial.api.v1.model.response.FinancialDataResponse import FinancialDataResponse, FinancialDataPagination
from financial.api.v1.model.response.StatisticsResponse import StatisticsResponse
from financial.entity.FinancialDataEntity import FinancialDataEntity, FinancialData
from financial.main import app


@app.get("/api/financial_data")
async def get_financial_data(req: FinancialDataRequest = Depends()) -> FinancialDataResponse:
    """
        Get the financial data by symbol (AAPL or IBM) within a certain start date and end date
    """
    conditions = [FinancialDataEntity.symbol == req.symbol]

    if req.start_date:
        conditions.append(FinancialDataEntity.date >= req.start_date)

    if req.end_date:
        conditions.append(FinancialDataEntity.date <= req.end_date)

    query = FinancialDataEntity.select()

    if conditions:
        query = query.where(*conditions)

    data_page = query.paginate(req.page, req.limit).execute()

    count = query.count()
    pages = math.ceil(count / req.limit) or 1
    pagination = FinancialDataPagination(
        count=count,
        page=req.page,
        limit=req.limit,
        pages=pages
    )

    return FinancialDataResponse(
        data=[FinancialData.from_orm(fd) for fd in data_page],
        pagination=pagination
    )


@app.get("/api/statistics")
async def get_statistics(req: StatisticsRequest = Depends()) -> StatisticsResponse:
    """
        Get the average of financial data by symbol (AAPL or IBM) within a certain start date and end date
    """
    query = FinancialDataEntity.select().where(
        FinancialDataEntity.date >= req.start_date,
        FinancialDataEntity.date <= req.end_date,
        FinancialDataEntity.symbol == req.symbol
    )

    data: list[FinancialData] = query.execute()

    if not data:
        return StatisticsResponse(
            info="No data found"
        )

    return StatisticsResponse(
        data=StatisticsModel(
            start_date=req.start_date,
            end_date=req.end_date,
            symbol=req.symbol,
            average_daily_open_price=float(format(statistics.mean((d.open_price for d in data)), ".2f")),
            average_daily_close_price=float(format(statistics.mean((d.close_price for d in data)), ".2f")),
            average_daily_volume=float(format(statistics.mean((d.volume for d in data)), ".2f"))
        )
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
