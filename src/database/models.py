from datetime import UTC, datetime
from uuid import UUID

from sqlalchemy import BigInteger, DateTime, ForeignKey, String, Uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from uuid6 import uuid7


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "categories"

    archives: Mapped[list["Archive"]] = relationship(
        back_populates="category",
    )

    id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid7,
    )
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )
    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False,
    )


class Archive(Base):
    __tablename__ = "archives"

    category: Mapped["Category"] = relationship(
        back_populates="archives",
    )

    id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid7,
    )
    title: Mapped[str] = mapped_column(
        String(255),
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
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False,
    )
