from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,

)


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()

    frog_button = InlineKeyboardButton(
        "Вопрос1",
        callback_data="start_frog_question"
    )
    markup.add(frog_button)

    birds_button = InlineKeyboardButton(
        text='вопрос2',
        callback_data="start_bird_question"
    )
    markup.add(birds_button)

    python_button = InlineKeyboardButton(
        text='вопрос3',
        callback_data='start_python_question'
    )

    markup.add(python_button)
    return markup

