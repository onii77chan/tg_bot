from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    button_quiz = InlineKeyboardButton(
        "Начать викторину 🧐",
        callback_data="quiz_start"
    )
    button_manga_news = InlineKeyboardButton(
        "Сейчас читают 📖",
        callback_data="button_manga_news"
    )
    reputation_check_button = InlineKeyboardButton(
        "Проверить репутацию в группе ToT и Thunder 🤓",
        callback_data="reputation_check"
    )
    next_button = InlineKeyboardButton(
        "not ready yet 🛠️",
        callback_data="next_button"
    )
    registration_button = InlineKeyboardButton(
        "Registration 🔥",
        callback_data="registration"
    )
    random_profile_button = InlineKeyboardButton(
        "View Profiles 👍🏻👎🏻",
        callback_data="random_profile"
    )
    my_profile_button = InlineKeyboardButton(
        "Profile 🐲",
        callback_data="my_profile"
    )
    markup.add(random_profile_button)
    markup.add(my_profile_button)
    markup.add(registration_button)
    markup.add(next_button)
    markup.add(reputation_check_button)
    # markup.add(button_manga_news)
    markup.add(button_quiz)
    return markup
