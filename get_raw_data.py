import os
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

from financial import entity
from financial.entity import FinancialDataEntity
from financial.entity.FinancialDataEntity import FinancialData, FinancialDataEntity

# Load .env file
load_dotenv()

STOCK_DAYS: int = os.getenv('STOCK_DAYS')
STOCK_SYMBOLS: list[str] = os.getenv('STOCK_SYMBOLS').split(",")
ALPHA_VANTAGE_API_KEY: str = os.getenv('ALPHA_VANTAGE_API_KEY')
ALPHA_VANTAGE_URL_DAILY: str = os.getenv('ALPHA_VANTAGE_URL_DAILY')


def get_stocks() -> None:
    for symbol in STOCK_SYMBOLS:
        get_stock(symbol)


def get_stock(symbol: str) -> None:
    """
        Get financial data from Alpha Vantage
    """
    url = ALPHA_VANTAGE_URL_DAILY.format(
        symbol, ALPHA_VANTAGE_API_KEY
    )

    # Fetch data from Alpha Vantage
    response = requests.get(url).json()

    to_insert = []
    data_result = response['Time Series (Daily)']

    # Date today
    curr_date = datetime.today()
    # 14 days before the date today
    from_date = datetime(curr_date.year, curr_date.month, curr_date.day) - timedelta(days=int(STOCK_DAYS))

    for date_str, data_day in data_result.items():
        to_insert.append(
            FinancialData(
                symbol=symbol,
                date=date_str,
                open_price=data_day['1. open'],
                close_price=data_day['4. close'],
                volume=data_day['6. volume']
            ).dict()
        )

        # If the data is less than 14 days before the current date, break the loop
        if datetime.strptime(date_str, '%Y-%m-%d') < from_date:
            break

    if to_insert:
        FinancialDataEntity.insert_many(to_insert).on_conflict_replace().execute()


if __name__ == "__main__":
    entity.FinancialDataEntity.create_financial_data_table()
    get_stocks()
    print("Success!")
