from app.db.base import Base
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.book import Book


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    description: Mapped[str|None] = mapped_column(String(500), nullable=True)
    books: Mapped[list["Book"]] = relationship(
        back_populates="category"
    )