from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,

)


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()

    questiare_button_frog = InlineKeyboardButton(
        "Лягушка это",
        callback_data="start_frog_question_1"
    )

    questiare_button_bird = InlineKeyboardButton(
        text='Птица это',
        callback_data="start_bird_question_1"
    )
    questiare_button_python = InlineKeyboardButton(
        text='python это',
        callback_data="start_python_question_1"
    )

    markup.add(questiare_button_frog, questiare_button_bird, questiare_button_python)
    return markup
