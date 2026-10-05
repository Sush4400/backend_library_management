from sqlalchemy import ForeignKey, String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.category import Category
    from app.models.publisher import Publisher
    from app.models.author import Author
    from app.models.loan import Loan



class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    isbn: Mapped[str] = mapped_column(String(200), index=True, unique=True, nullable=False)
    description: Mapped[str|None] = mapped_column(Text, nullable=True)
    publication_year: Mapped[int|None] = mapped_column(Integer, nullable=True)
    total_copies: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    available_copies: Mapped[int] = mapped_column(Integer, default=1, nullable=False)

    # foreign key
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="RESTRICT"), nullable=False, index=True)
    publisher_id: Mapped[int|None] = mapped_column(ForeignKey("publishers.id", ondelete="SET NULL"), nullable=True, index=True)

    # relationships
    category: Mapped["Category"] = relationship(
        back_populates="books"
    )
    publisher: Mapped["Publisher"] = relationship(
        back_populates="books"
    )
    authors: Mapped[list["Author"]] = relationship(
        secondary="book_authors",
        back_populates="books",
    )
    loans: Mapped[list["Loan"]] = relationship(
        back_populates="book"
    )