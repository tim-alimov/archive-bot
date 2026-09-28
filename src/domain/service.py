from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.exceptions import (
    ArchiveNotFoundError,
    CategoryAlreadyExistsError,
    CategoryNotFoundError,
    InvalidArchiveError,
    InvalidCategoryError,
)
from src.domain.models import (
    DESCRIPTION_MAX_LENGTH,
    TITLE_MAX_LENGTH,
    Archive,
    Category,
)
from src.domain.repository import ArchiveRepository, CategoryRepository


class CategoryService:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._categories = CategoryRepository(session)

    async def get(self, category_id: UUID) -> Category:
        category = await self._categories.get_by_id(category_id)
        if category is None:
            raise CategoryNotFoundError(category_id=category_id)
        return category

    async def list(self) -> list[Category]:
        return await self._categories.get_all()

    async def create(self, title: str, description: str | None = None) -> Category:
        _validate_category(title, description)
        if await self._categories.get_by_title(title) is not None:
            raise CategoryAlreadyExistsError(title=title)
        category = Category(title=title, description=description)
        try:
            await self._categories.add(category)
            await self._session.commit()
        except IntegrityError:
            await self._session.rollback()
            raise CategoryAlreadyExistsError(title=title)
        return category

    async def update(
        self,
        category_id: UUID,
        title: str | None = None,
        description: str | None = None,
    ) -> Category:
        category = await self.get(category_id)
        _validate_category(title, description)
        if (
            title is not None
            and title != category.title
            and await self._categories.get_by_title(title) is not None
        ):
            raise CategoryAlreadyExistsError(title=title)
        if title is not None:
            category.title = title
        if description is not None:
            category.description = description
        try:
            await self._session.commit()
        except IntegrityError:
            await self._session.rollback()
            raise CategoryAlreadyExistsError(title=title)
        return category

    async def delete(self, category_id: UUID) -> None:
        category = await self.get(category_id)
        await self._categories.delete(category)
        await self._session.commit()


def _validate_category(title: str | None, description: str | None) -> None:
    if title is not None and not 1 <= len(title) <= TITLE_MAX_LENGTH:
        raise InvalidCategoryError(
            f"Title must be 1-{TITLE_MAX_LENGTH} characters long."
        )
    if description is not None and len(description) > DESCRIPTION_MAX_LENGTH:
        raise InvalidCategoryError(
            f"Description must be at most {DESCRIPTION_MAX_LENGTH} characters long."
        )


class ArchiveService:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._archives = ArchiveRepository(session)
        self._categories = CategoryRepository(session)

    async def get(self, archive_id: UUID) -> Archive:
        archive = await self._archives.get_by_id(archive_id)
        if archive is None:
            raise ArchiveNotFoundError(archive_id=archive_id)
        return archive

    async def list(self) -> list[Archive]:
        return await self._archives.get_all()

    async def create(
        self, title: str, category_id: UUID, telegram_message_id: int
    ) -> Archive:
        if not 1 <= len(title) <= TITLE_MAX_LENGTH:
            raise InvalidArchiveError(
                f"Title must be 1-{TITLE_MAX_LENGTH} characters long."
            )
        if await self._categories.get_by_id(category_id) is None:
            raise CategoryNotFoundError(category_id=category_id)
        archive = Archive(
            title=title,
            category_id=category_id,
            telegram_message_id=telegram_message_id,
        )
        await self._archives.add(archive)
        await self._session.commit()
        return archive

    async def delete(self, archive_id: UUID) -> None:
        archive = await self.get(archive_id)
        await self._archives.delete(archive)
        await self._session.commit()
