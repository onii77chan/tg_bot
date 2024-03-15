# from aiogram import types, Dispatcher
# from config import bot
# from profanity_check import predict, predict_prob
# from DB.bot_DB import Database
# import datetime
#
#
# async def chat_messages(message: types.Message):
#     db = Database()
#     ban_word_predict_prob = predict_prob([message.text])
#     print(ban_word_predict_prob)
#
#     if ban_word_predict_prob > 0.6:
#         ban_user = db.select_ban_user(
#             tg_id=message.from_user.id
#         )
#         if not ban_user:
#             db.insert_ban_user(
#                 tg_id=message.from_user.id
#             )
#         elif ban_user['count'] >= 3:
#             await bot.ban_chat_member(
#                 chat_id=message.chat.id,
#                 user_id=message.from_user.id,
#                 until_date=datetime.datetime.now() + datetime.timedelta(hours=1)
#             )
#         else:
#             db.update_ban_count(
#                 tg_id=message.from_user.id
#             )
#
#         await message.delete()
#         await bot.send_message(
#             chat_id=message.chat.id,
#             text=f'User: {message.from_user.first_name}\n'
#                  f'Dont curse in this group otherwise we will banned you'
#         )
#
#
# def register_group_actions_handlers(dp: Dispatcher):
#     dp.register_message_handler(
#         chat_messages
#     )
