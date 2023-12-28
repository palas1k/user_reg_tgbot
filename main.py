import asyncio

from aiogram.filters import Command

from aiogram import Bot

from config import dp, bot
from handlers import form
from dp import User, async_db_session
from utils.commands import set_commands
from utils.statesform import StepsForm


async def start_bot(bot: Bot):
    await set_commands(bot)


async def start():
    await async_db_session.init()
    dp.startup.register(start_bot)
    dp.message.register(form.user_register, Command(commands='registration'))
    dp.message.register(form.get_user)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
