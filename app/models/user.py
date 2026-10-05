from sqlalchemy.orm import mapped_column, Mapped
from app.db.base import Base
from sqlalchemy import String
from enum import Enum
from sqlalchemy import Enum as SqlEnum


class UserRole(str, Enum):
    ADMIN = "admin"
    LIBRARIAN = "librarian"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(200), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[UserRole] = mapped_column(SqlEnum(UserRole), default=UserRole.LIBRARIAN, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)