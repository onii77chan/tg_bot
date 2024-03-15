from sqlite3 import IntegrityError
from aiogram import types, Dispatcher
from DB import bot_DB
from config import bot, MEDIA_DESTINATION
from keyboards.start_menu import start_menu_keyboard


async def start_menu(message: types.Message):
    print(message)
    db = bot_DB.Database()
    try:
        db.sql_insert_user(
            tg_id=message.from_user.id,
            user_name=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
    except IntegrityError:
        pass
    # await bot.send_message(
    #     chat_id=message.from_user.id,
    #     text=f'hello {message.from_user.first_name}',
    #     reply_markup=await start_menu_keyboard()
    # )

    with open(MEDIA_DESTINATION + "bot_icon.gif", 'rb') as animation:
        await bot.send_animation(
            chat_id=message.from_user.id,
            animation=animation,
            reply_markup=await start_menu_keyboard()
        )

def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(
        start_menu,
        commands=['start']
    )
