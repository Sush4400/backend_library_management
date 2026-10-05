from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.dao import category_dao
from app.models.category import Category
from app.schemas.category_schemas import CategoryCreate, CategoryUpdate



def get_categories(db: Session):
    return category_dao.get_categories(db)


def get_category(db: Session, category_id: int):
    category = category_dao.get_category(db, category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    return category


def create_category(db: Session, data: CategoryCreate):
    category = Category(**data.model_dump())
    return category_dao.create_category(db, category)


def update_category(db: Session, category_id: int, data: CategoryUpdate):
    category = get_category(db, category_id)
    return category_dao.update_category(db, category, data)


def delete_category(db: Session, category_id: int):
    category = get_category(db, category_id)
    return category_dao.delete_category(db, category)