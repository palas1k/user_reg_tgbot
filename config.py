import os

from aiogram import Bot, Dispatcher

from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)
dp = Dispatcher()
