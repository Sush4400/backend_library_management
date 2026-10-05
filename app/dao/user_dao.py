from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.user import User, UserRole
from app.schemas.user_schemas import UserUpdate



def get_users(db: Session) -> list[User]:
    stmt = select(User).order_by(User.id)
    return list(db.scalars(stmt).all())


def get_user(db: Session, user_id: int) -> User|None:
    stmt = select(User).where(User.id==user_id)
    return db.scalar(stmt)


def get_user_by_email(db: Session, email: str) -> User|None:
    stmt = select(User).where(User.email==email)
    return db.scalar(stmt)


def create_user(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(db: Session, user: User, update_data: dict) -> User:
    for field, value in update_data.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: User) -> None:
    db.delete(user)
    db.commit()
