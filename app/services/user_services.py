from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.dao import user_dao
from app.schemas.user_schemas import UserCreate, UserUpdate
from app.models.user import User
from app.core.security import hash_password


def get_users(db: Session):
    return user_dao.get_users(db)


def get_user(db: Session, user_id:int):
    user = user_dao.get_user(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


def create_user(db: Session, data: UserCreate):
    existing_user = user_dao.get_user_by_email(db, data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered."
        )
    password_hash = hash_password(data.password)
    user = User(
        name=data.name,
        email=data.email,
        password_hash=password_hash,
        role=data.role,
    )
    return user_dao.create_user(db, user)


def update_user(db: Session, user_id, data: UserUpdate):
    user = get_user(db, user_id)
    update_data = data.model_dump(exclude_unset=True)
    if "email" in update_data:
        existing_user = user_dao.get_user_by_email(db, update_data["email"])
        if existing_user and existing_user.id != user.id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered."
            )
    if "password" in update_data:
        password = update_data.pop("password")
        update_data["password_hash"] = hash_password(password)
    return user_dao.update_user(db, user, update_data)


def delete_user(db: Session, user_id):
    user = get_user(db, user_id)
    user_dao.delete_user(db, user)