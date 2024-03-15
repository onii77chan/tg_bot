from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)



async def python_is_keyboard():
    markup = InlineKeyboardMarkup()

    option_one_python = InlineKeyboardButton(
        text="язык гипертекстовой разметки",
        callback_data="python_is_html",
    )

    option_two_python = InlineKeyboardButton(
        text='язык управления нереляционными базами данных',
        callback_data="python_is_NOsql"
    )
    option_three_python = InlineKeyboardButton(
        text='интерпретируемый язык с динамической типизацией',
        callback_data="True_option_python",
    )
    markup.add(option_one_python)
    markup.add(option_two_python)
    markup.add(option_three_python)
    return markup


async def bird_is_keyboard():
    markup = InlineKeyboardMarkup()
    option_one_bird = InlineKeyboardButton(
        text='С перьями и пухом позвоночное животное с крыльями',
        callback_data='true_option_bird'
    )
    option_two_bird = InlineKeyboardButton(
        text='Киборг убийца',
        callback_data="bird_is_kiborg"
    )
    option_three_bird = InlineKeyboardButton(
        text='животное из семейства кошек',
        callback_data="bird_is_cat"
    )
    markup.add(option_one_bird)
    markup.add(option_two_bird)
    markup.add(option_three_bird)
    return markup


async def geeks_is_keyboard():
    markup = InlineKeyboardMarkup()

    option_one_geeks = InlineKeyboardButton(
        text='Компания обучающая программированию из кр',
        callback_data='true_option_geeks'
    )
    option_two_geeks = InlineKeyboardButton(
        text='Завод по производству и обработке лития',
        callback_data="geeks_is_factory"
    )
    option_three_geeks = InlineKeyboardButton(
        text='Компания GeekBrains из россии',
        callback_data="geeks_is_GeekBrains"
    )
    markup.add(option_one_geeks)
    markup.add(option_two_geeks)
    markup.add(option_three_geeks)
    return markup


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()

    button_python_is = InlineKeyboardButton(
        "пайтон это",
        callback_data="button_python_is"
    )
    button_bird_is = InlineKeyboardButton(
        'птица это',
        callback_data="button_bird_is"

    )
    button_geeks_is = InlineKeyboardButton(
        'гикс это',
        callback_data="button_geeks_is"
    )

    markup.add(button_python_is)
    markup.add(button_bird_is)
    markup.add(button_geeks_is)
    return markup
