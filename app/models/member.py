from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.loan import Loan


class Member(Base):
    __tablename__ = "members"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), index=True, unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(20), index=True, unique=True, nullable=False)
    address: Mapped[str|None] = mapped_column(String(255), nullable=True)
    membership_date: Mapped[date] = mapped_column(Date, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)

    loans: Mapped[list["Loan"]] = relationship(back_populates="member")