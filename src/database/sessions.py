from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.database.engine import get_async_engine

session_factory = async_sessionmaker(
    get_async_engine(),
    class_=AsyncSession,
    expire_on_commit=False,
)
