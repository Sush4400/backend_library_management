from sqlalchemy import DateTime, ForeignKey, Enum as SQLEnum
from enum import Enum
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime
from app.db.base import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.book import Book
    from app.models.member import Member
    from app.models.fine import Fine


class LoanStatus(str, Enum):
    BORROWED = "borrowed"
    RETURNED = "returned"
    OVERDUE = "overdue"


class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id", ondelete="RESTRICT"), nullable=False, index=True)
    member_id: Mapped[int] = mapped_column(ForeignKey("members.id", ondelete="RESTRICT"), nullable=False, index=True)
    issued_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    due_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    returned_at: Mapped[datetime|None] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[LoanStatus] = mapped_column(
        SQLEnum(LoanStatus),
        default=LoanStatus.BORROWED,
        nullable=False,
        index=True
    )


    book: Mapped["Book"] = relationship(back_populates="loans")
    member: Mapped["Member"] = relationship(back_populates="loans")
    fine: Mapped["Fine|None"] = relationship(back_populates="loan", uselist=False)