# id, name, address, books
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.book import Book


class Publisher(Base):
    __tablename__ = "publishers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), unique=True, index=True, nullable=False)
    address: Mapped[str|None] = mapped_column(String(500), nullable=True)

    # relationships
    books: Mapped[list["Book"]] = relationship(
        back_populates="publisher"
    )