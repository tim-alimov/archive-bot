from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ArchiveCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    category_id: UUID = Field(...)
    telegram_message_id: int = Field(...)


class ArchiveUpdate(BaseModel):
    id: UUID = Field(...)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    category_id: UUID | None = Field(default=None)
    telegram_message_id: int | None = Field(default=None)


class ArchiveResponse(ArchiveCreate):
    id: UUID = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)

    model_config = ConfigDict(from_attributes=True)
