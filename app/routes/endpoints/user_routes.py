from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services import user_services
from app.schemas.user_schemas import UserCreate, UserUpdate, UserResponse
from app.db.database import get_db



router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserResponse])
def get_users(db: Session=Depends(get_db)):
    return user_services.get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session=Depends(get_db)):
    return user_services.get_user(db, user_id)


@router.post("/", response_model=UserResponse)
def create_user(data: UserCreate, db: Session=Depends(get_db)):
    return user_services.create_user(db, data)


@router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserUpdate, db: Session=Depends(get_db)):
    return user_services.update_user(db, user_id, data)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session=Depends(get_db)):
    return user_services.delete_user(db, user_id)