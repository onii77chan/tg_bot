import webbrowser

from aiogram import types, Dispatcher

from config import bot
from keyboards.questionnaire import (
    questionnaire_keyboard,
    python_is_keyboard,
    bird_is_keyboard,
    geeks_is_keyboard,

)


async def questinaire_start_quiz(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Выберите один из вопросов',
        reply_markup=await questionnaire_keyboard()
    )


async def button_python_is(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Что такое пайтон',
        reply_markup=await python_is_keyboard(),
    )


async def python_is_html(call: types.CallbackQuery):
    await call.message.answer("Гений (Близко но не то попробуй еще раз)")


async def python_is_NOsql(call: types.CallbackQuery):
    await call.message.answer("Неправильно попробуй еще раз")


async def true_option_python(call: types.CallbackQuery):
    video_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(video_link)


async def button_bird_is(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Что такое птица',
        reply_markup=await bird_is_keyboard()
    )


async def option_one_bird(call: types.CallbackQuery):
    await call.message.answer("Правильно")


async def option_two_bird(call: types.CallbackQuery):
    await call.message.answer("Я то согласен\n"
                              "а вот моя биологичка так не думает")


async def option_three_bird(call: types.CallbackQuery):
    await call.message.answer("Ну почти")


async def button_geeks_is(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Что такое geeks',
        reply_markup=await geeks_is_keyboard()
    )


async def option_one_geeks(call: types.CallbackQuery):
    await call.message.answer("Правильно")


async def option_two_geeks(call: types.CallbackQuery):
    await call.message.answer("Неправильно")


async def option_three_geeks(call: types.CallbackQuery):
    await call.message.answer("Неправильно")


def register_questionaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questinaire_start_quiz,
        lambda call: call.data == "quiz_start",
    )
    #
    #
    dp.register_callback_query_handler(
        button_python_is,
        lambda call: call.data == "button_python_is",
    )
    dp.register_callback_query_handler(
        button_bird_is,
        lambda call: call.data == "button_bird_is",
    )
    dp.register_callback_query_handler(
        button_geeks_is,
        lambda call: call.data == "button_geeks_is",
    )
    #
    #
    dp.register_callback_query_handler(
        python_is_html,
        lambda call: call.data == "python_is_html",
    )
    dp.register_callback_query_handler(
        python_is_NOsql,
        lambda call: call.data == "python_is_NOsql"
    )
    dp.register_callback_query_handler(
        true_option_python,
        lambda call: call.data == "True_option_python"
    )
    #
    #
    dp.register_callback_query_handler(
        option_one_bird,
        lambda call: call.data == "true_option_bird"
    )
    dp.register_callback_query_handler(
        option_two_bird,
        lambda call: call.data == "bird_is_kiborg"
    )
    dp.register_callback_query_handler(
        option_three_bird,
        lambda call: call.data == "bird_is_cat"
    )
    #
    #
    dp.register_callback_query_handler(
        option_one_geeks,
        lambda call: call.data == "true_option_geeks"
    )
    dp.register_callback_query_handler(
        option_two_geeks,
        lambda call: call.data == "geeks_is_factory"
    )
    dp.register_callback_query_handler(
        option_three_geeks,
        lambda call: call.data == "geeks_is_GeekBrains"
    )
