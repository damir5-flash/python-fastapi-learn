from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker
from core.config import settings

class DatabaseHelper:
    async def despose(self):
        await self.engine.dispose()
    async def session_getter(self):
        async with self.session_fabric() as session:
            yield session
    def __init__(
            self,
            url: str,
            echo: bool = False,
            echo_pool: bool = False,
            pool_size: int = 5,
            max_overflow: int = 10
    ):
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,

        )
        self.session_fabric = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )


db_helper = DatabaseHelper(
    url=str(settings.db.url),
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow
)
