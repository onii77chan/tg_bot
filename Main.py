from aiogram import executor
from config import dp
from handlers import (
    start,
    questionare,
    group_actions,
    dot,
    registration,

)
from DB import bot_DB


async def on_startup(_):
    db = bot_DB.Database()
    db.sql_create_tables()


start.register_start_handler(dp=dp)
questionare.register_questionaire_handlers(dp=dp)
dot.register_manga_handler(dp=dp)
group_actions.register_group_actions_handlers(dp=dp)
registration.register_registration_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(
        dp,
        on_startup=on_startup
    )
