from app.db.base import Base
from sqlalchemy import String, Text
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.book import Book



class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    biography: Mapped[str|None] = mapped_column(Text, nullable=True)

    # relationships
    books: Mapped[list["Book"]] = relationship(
        secondary="book_authors",
        back_populates="authors",
    )