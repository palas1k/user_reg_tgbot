import asyncio
import os

from aiogram.dispatcher.router import Router
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message

from logic import check_user_in_db
from models import User

load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)
dp = Dispatcher()
router = Router(name=__name__)


async def user_register(message: Message):
    await bot.send_message(message.from_user.id, 'Для регистрация, набери имя')
    message_text = message.text
    await check_user_in_db(str(message_text))
    await message.reply('Готово')


async def start():
    dp.message.register(user_register)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
