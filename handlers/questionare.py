from aiogram import types, Dispatcher
from config import bot


async def questinaire_start_frog(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='started'
    )


async def questinaire_start_bird(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='started'
    )


async def questinaire_start_python(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='started'
    )


def register_questionaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questinaire_start_frog,
        lambda call: call.data == "start_frog_question_1",
        questinaire_start_bird,
        lambda call: call.data == "start_bird_question_1",
        questinaire_start_python,
        lambda call: call.data == "start_python_question_1"
    )
