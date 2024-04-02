from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def profile_keyboard(tg_id):
    markup = InlineKeyboardMarkup()

    like_button = InlineKeyboardButton(
        "Like 👍🏻",
        callback_data=f"like_{tg_id}"
    )
    dislike_button = InlineKeyboardButton(
        "Dislike 👎🏻",
        callback_data=f"dis_{tg_id}"
    )

    markup.add(like_button)
    markup.add(dislike_button)
    return markup


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()

    update_profile_button = InlineKeyboardButton(
        "Update 🟡",
        callback_data="registration"
    )
    delete_profile_button = InlineKeyboardButton(
        "Delete ❌",
        callback_data="delete_profile"
    )

    markup.add(update_profile_button)
    markup.add(delete_profile_button)
    return markup
