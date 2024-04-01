from aiogram import types, Dispatcher

from config import bot
from profanity_check import predict_prob
from DB.bot_DB import Database
import datetime
db = Database()


async def chat_messages(message: types.Message):

    ban_word_predict_prob = predict_prob([message.text])
    print(ban_word_predict_prob)

    if ban_word_predict_prob > 0.5:
        ban_user = db.select_ban_user(
            tg_id=message.from_user.id
        )
        if not ban_user:
            db.insert_ban_user(
                tg_id=message.from_user.id
            )
        elif ban_user['count'] >= 3:
            await bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.from_user.id,
                until_date=datetime.datetime.now() + datetime.timedelta(hours=1)
            )
        else:
            db.update_ban_count(
                tg_id=message.from_user.id
            )

        await message.delete()
        await bot.send_message(
            chat_id=message.chat.id,
            text=f'User: {message.from_user.first_name}\n'
                 f'Dont curse in this group otherwise we will banned you'
        )


async def check_user_reputation(call: types.CallbackQuery):
    user_reputation = db.reputation_check(call.from_user.id)
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f'число ваших нарушений: {user_reputation}',
    )


async def select_ban_count():
    db.reputation_check(
        Dispatcher.get
    )


def register_group_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(
        chat_messages
    )
    dp.register_callback_query_handler(
        check_user_reputation,
        lambda call: call.data == "reputation_check"
    )
