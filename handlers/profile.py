import re
from aiogram import types, Dispatcher
import const
from config import bot
from keyboards.profile import profile_keyboard, my_profile_keyboard
from DB.bot_DB import Database
import random


async def my_profile_call(call: types.CallbackQuery):
    db = Database()
    profile = db.select_profile(tg_id=call.from_user.id)

    if profile:
        with open(profile['photo'], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=profile['nickname'],
                    bio=profile['bio'],
                    age=profile['age'],
                    married=profile['married'],
                    gender=profile['gender'],
                    favorite_color=profile['favorite_color'],
                    nationality=profile['nationality'],
                ),
                reply_markup=await my_profile_keyboard()
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="U have not registered, please register to view ur profile"
        )


async def random_profile_call(call: types.CallbackQuery):
    db = Database()
    profiles = db.select_all_profiles(tg_id=call.from_user.id)
    if profiles:
        try:
            random_profile = random.choice(profiles)
            with open(random_profile['photo'], 'rb') as photo:
                await bot.send_photo(
                    chat_id=call.from_user.id,
                    photo=photo,
                    caption=const.PROFILE_TEXT.format(
                        nickname=random_profile['nickname'],
                        bio=random_profile['bio'],
                        age=random_profile['age'],
                        married=random_profile['married'],
                        gender=random_profile['gender'],
                        favorite_color=random_profile['favorite_color'],
                        nationality=random_profile['nationality'],

                    ),
                    reply_markup=await profile_keyboard(tg_id=random_profile['telegram_id'])
                )
        except Exception as e:
            print(f"Error sending profile photo: {e}")
            await bot.send_message(
                chat_id=call.from_user.id,
                text="Sorry, there was an error while processing your request. Please try again later."
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="There are no profiles available at the moment. Please try again later."
        )


async def delete_profile(call: types.CallbackQuery):
    db = Database()
    db.delete_profile(call.from_user.id)
    await bot.send_message(chat_id=call.from_user.id,
                           text="Profile deleted", )


async def detect_like_call(call: types.CallbackQuery):
    # print(call.data[5:])
    # print(call.data.replace("like_", ""))
    owner = re.sub("like_", "", call.data)
    db = Database()

    db.insert_like_profile(
        owner=owner,
        liker=call.from_user.id
    )
    await random_profile_call(call=call)


async def detect_dis_call(call: types.CallbackQuery):
    owner = re.sub("dis_", "", call.data)
    db = Database()

    db.insert_dis_profile(
        owner=owner,
        liker=call.from_user.id
    )
    await random_profile_call(call=call)


def register_profile_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        random_profile_call,
        lambda call: call.data == "random_profile"
    )
    dp.register_callback_query_handler(
        detect_like_call,
        lambda call: "like_" in call.data
    )
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == "my_profile"
    )
    dp.register_callback_query_handler(
        detect_dis_call,
        lambda call: "dis_" in call.data
    )
    dp.register_callback_query_handler(
        delete_profile,
        lambda call: call.data == "delete_profile"
    )
