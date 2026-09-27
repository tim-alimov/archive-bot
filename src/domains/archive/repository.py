from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.exceptions import ArchiveNotFoundError
from src.domains.archive.model import Archive
from src.domains.archive.schema import ArchiveCreate, ArchiveResponse, ArchiveUpdate


class ArchiveRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, archive_id: UUID) -> ArchiveResponse:
        statement = select(Archive).where(Archive.id == archive_id)
        result = await self._session.execute(statement)
        db_archive = result.scalar_one_or_none()
        if not db_archive:
            raise ArchiveNotFoundError(archive_id=archive_id)
        return ArchiveResponse.model_validate(db_archive)

    async def get_all(self) -> list[ArchiveResponse]:
        statement = select(Archive).order_by(Archive.title)
        result = await self._session.execute(statement)
        db_archives = result.scalars().all()
        return [ArchiveResponse.model_validate(a) for a in db_archives]


    async def create(self, archive: ArchiveCreate) -> ArchiveResponse:
        db_archive = Archive(**archive.model_dump())
        self._session.add(db_archive)
        await self._session.commit()
        await self._session.refresh(db_archive)
        return ArchiveResponse.model_validate(db_archive)

    async def update(self, archive: ArchiveUpdate) -> ArchiveResponse:
        statement = select(Archive).where(Archive.id == archive.id)
        result = await self._session.execute(statement)
        db_archive = result.scalar_one_or_none()

        if not db_archive:
            raise ArchiveNotFoundError(archive_id=archive.id)

        update_data = archive.model_dump(exclude_unset=True, exclude={"id"})
        for key, value in update_data.items():
            setattr(db_archive, key, value)

        await self._session.commit()
        await self._session.refresh(db_archive)
        return ArchiveResponse.model_validate(db_archive)

    async def delete(self, archive_id: UUID) -> ArchiveResponse:
        statement = select(Archive).where(Archive.id == archive_id)
        result = await self._session.execute(statement)
        db_archive = result.scalar_one_or_none()

        if not db_archive:
            raise ArchiveNotFoundError(archive_id=archive_id)

        response = ArchiveResponse.model_validate(db_archive)
        await self._session.delete(db_archive)
        await self._session.commit()
        return response
