from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from src.core.settings import settings


def get_async_engine() -> AsyncEngine:
    return create_async_engine(
        settings.database_url.get_secret_value(),
    )
