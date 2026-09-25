from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class CategoryCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=500)


class CategoryUpdate(BaseModel):
    id: UUID = Field(...)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=500)

class CategoryResponse(CategoryCreate):
    id: UUID = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)

    model_config = ConfigDict(from_attributes=True)
