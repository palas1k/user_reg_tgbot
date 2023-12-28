from sqlalchemy import String, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declarative_base

Base = declarative_base()


class AsyncDBSession:
    name_admin_db: str = "postgres"  # Имя админа
    password_db: str = "666666"  # Пароль бд
    ip_db: str = "localhost"  # IP бд
    name_db: str = "test_db"  # Имя бд
    connect_db: str = f"{name_admin_db}:{password_db}@{ip_db}/"

    def __init__(self):
        self._session = None
        self._engine = None

    def __getattr__(self, name):
        return getattr(self._session, name)

    async def init(self):
        self._engine = create_async_engine(f"postgresql+asyncpg://{self.connect_db}", echo=True)
        #self._engine = create_async_engine(f"postgresql+asyncpg://postgres:666666@localhost/test_db", echo=True)
        self._session = async_sessionmaker(self._engine, expire_on_commit=False, class_=AsyncSession())

    async def create_all(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


async_db_session = AsyncDBSession()


class MethodClassAll:
    @classmethod
    async def create(cls, name: str) -> None:
        async_db_session.add(name)
        await async_db_session.commit()


class MethodClassUser(MethodClassAll):
    @classmethod
    async def get_user(cls, name: str):
        query = select(cls).where(cls.name == name)
        res = await async_db_session.execute(query)
        try:
            (res,) = res.one()
        except NoResultFound:
            res = None
        return res

    @classmethod
    async def get_all(cls):
        query = select(cls)
        try:
            res = await async_db_session.execute(query)
            (res,) = res.one()
        except NoResultFound:
            res = None
        return res


class User(Base, MethodClassUser):
    __tablename__ = "user_profile"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(55))

    def __init__(self, name: Mapped[str]):
        self.name = name

    def __repr__(self):
        return f"ID: {self.id}, Name: {self.name}"
