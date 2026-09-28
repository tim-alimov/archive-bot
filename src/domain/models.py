from uuid import UUID

from sqlalchemy import BigInteger, ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base, IdMixin, TimestampMixin

TITLE_MAX_LENGTH = 255
DESCRIPTION_MAX_LENGTH = 500


class Category(IdMixin, TimestampMixin, Base):
    __tablename__ = "categories"

    title: Mapped[str] = mapped_column(
        String(TITLE_MAX_LENGTH),
        nullable=False,
        unique=True,
    )
    description: Mapped[str | None] = mapped_column(
        String(DESCRIPTION_MAX_LENGTH),
        nullable=True,
    )

    archives: Mapped[list["Archive"]] = relationship(back_populates="category")


class Archive(IdMixin, TimestampMixin, Base):
    __tablename__ = "archives"

    title: Mapped[str] = mapped_column(
        String(TITLE_MAX_LENGTH),
        nullable=False,
    )
    category_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey("categories.id"),
        nullable=False,
    )
    telegram_message_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
    )

    category: Mapped[Category] = relationship(back_populates="archives")
