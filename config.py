from decouple import config
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

PROXY_URL = 'http://proxy.server:3128'
storage = MemoryStorage()
TOKEN = config("TOKEN")
MEDIA_DESTINATION = config("MEDIA_DESTINATION")
bot = Bot(token=TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot=bot, storage=storage)
