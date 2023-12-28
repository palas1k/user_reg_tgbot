from sqlalchemy.exc import PendingRollbackError

from dp import User


async def create(tg_name: str)-> None:
    await User.create(User(name=tg_name))

