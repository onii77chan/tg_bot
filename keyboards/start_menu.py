from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    button_quiz = InlineKeyboardButton(
        "Начать викторину",
        callback_data="quiz_start"
    )

    markup.add(button_quiz)
    return markup
