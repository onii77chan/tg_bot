from decouple import config
from aiogram import Bot, dispatcher, Dispatcher

TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=Bot)