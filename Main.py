from aiogram import executor
from config import dp
from handlers import (
    start,
)

from DB import bot_DB


async def on_startup(_):
    db = bot_DB.Database()
    db.sql_create_tables()


start.register_start_handler(dp=dp)

if __name__ == '__main__':
    executor.start_polling(
        dp,
        on_startup=on_startup
    )
