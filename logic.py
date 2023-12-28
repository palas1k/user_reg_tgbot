from models import User, async_db_session


async def check_user_in_db(tg_name: str):
    try:
        name = await User.create(User(name=tg_name))
        print(name)
    except:
        # await User.get_all()
        print(await User.get_user('test'))
        print("Не создано")
