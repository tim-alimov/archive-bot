from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.models import Archive, Category


class CategoryRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, category_id: UUID) -> Category | None:
        return await self._session.get(Category, category_id)

    async def get_by_title(self, title: str) -> Category | None:
        statement = select(Category).where(Category.title == title)
        return await self._session.scalar(statement)

    async def get_all(self) -> list[Category]:
        statement = select(Category).order_by(Category.title)
        return list(await self._session.scalars(statement))

    async def add(self, category: Category) -> Category:
        self._session.add(category)
        await self._session.flush()
        return category

    async def delete(self, category: Category) -> None:
        await self._session.delete(category)
        await self._session.flush()


class ArchiveRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, archive_id: UUID) -> Archive | None:
        return await self._session.get(Archive, archive_id)

    async def get_all(self) -> list[Archive]:
        statement = select(Archive).order_by(Archive.title)
        return list(await self._session.scalars(statement))

    async def add(self, archive: Archive) -> Archive:
        self._session.add(archive)
        await self._session.flush()
        return archive

    async def delete(self, archive: Archive) -> None:
        await self._session.delete(archive)
        await self._session.flush()
