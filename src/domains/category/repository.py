from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.exceptions import CategoryAlreadyExistsError, CategoryNotFoundError
from src.domains.category.model import Category
from src.domains.category.schema import CategoryCreate, CategoryResponse, CategoryUpdate


class CategoryRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, category_id: UUID) -> CategoryResponse:
        statement = select(Category).where(Category.id == category_id)
        result = await self._session.execute(statement)
        db_category = result.scalar_one_or_none()
        if not db_category:
            raise CategoryNotFoundError(category_id=category_id)
        return CategoryResponse.model_validate(db_category)

    async def get_by_title(self, title: str) -> CategoryResponse:
        statement = select(Category).where(Category.title == title)
        result = await self._session.execute(statement)
        db_category = result.scalar_one_or_none()
        if not db_category:
            raise CategoryNotFoundError(title=title)
        return CategoryResponse.model_validate(db_category)

    async def get_all(self) -> list[CategoryResponse]:
        statement = select(Category).order_by(Category.title)
        result = await self._session.execute(statement)
        db_categories = result.scalars().all()
        return [CategoryResponse.model_validate(c) for c in db_categories]


    async def create(self, category: CategoryCreate) -> CategoryResponse:
        db_category = Category(**category.model_dump())
        self._session.add(db_category)
        try:
            await self._session.commit()
        except IntegrityError:
            await self._session.rollback()
            raise CategoryAlreadyExistsError(title=category.title)

        await self._session.refresh(db_category)
        return CategoryResponse.model_validate(db_category)

    async def update(self, category: CategoryUpdate) -> CategoryResponse:
        statement = select(Category).where(Category.id == category.id)
        result = await self._session.execute(statement)
        db_category = result.scalar_one_or_none()

        if not db_category:
            raise CategoryNotFoundError(category_id=category.id)

        update_data = category.model_dump(exclude_unset=True, exclude={"id"})
        for key, value in update_data.items():
            setattr(db_category, key, value)

        await self._session.commit()
        await self._session.refresh(db_category)
        return CategoryResponse.model_validate(db_category)

    async def delete(self, category_id: UUID) -> CategoryResponse:
        statement = select(Category).where(Category.id == category_id)
        result = await self._session.execute(statement)
        db_category = result.scalar_one_or_none()

        if not db_category:
            raise CategoryNotFoundError(category_id=category_id)

        response = CategoryResponse.model_validate(db_category)
        await self._session.delete(db_category)
        await self._session.commit()
        return response
