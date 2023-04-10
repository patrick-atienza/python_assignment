import trio

from peewee import SqliteDatabase

db = SqliteDatabase('financial_data.sqlite3')


# Adjust event loop
async def task():
    await trio.sleep(5)


trio.run(task)
