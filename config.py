from decouple import config
from aiogram import Bot, Dispatcher

TOKEN = config("TOKEN")
MEDIA_DESTINATION = config("MEDIA_DESTINATION")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
