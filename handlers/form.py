from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from dp import User
from utils.logic import create
from utils.statesform import StepsForm


# async def user_register(message: Message, state: FSMContext):
#     await message.answer('Введите имя для регистрации')
#     async with state.proxy() as data:
#         data['fio'] = message.text
#     try:
#         await User.create(User(name=tg_name["name"]))
#         await message.answer("Пользователь успешно зарегистрирован")
#     except:
#         await message.answer("Пользователь с таким именем уже существует")
#
#     finally:
#         await state.clear()


async def user_register(message: Message, state: FSMContext):
    await message.answer('Введите имя для регистрации')
    await state.set_state(StepsForm.GET_NAME)


async def get_user(message: Message, state: FSMContext):
    try:
        await User.create(User(name=message.text))
        await message.answer("Пользователь успешно зарегистрирован")
    except Exception as e:
        await message.answer("Пользователь с таким именем уже существует. Введите другое имя")
        print(e)

    finally:
        await state.clear()
