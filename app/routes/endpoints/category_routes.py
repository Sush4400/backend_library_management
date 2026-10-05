from fastapi import APIRouter, Depends
from app.schemas.category_schemas import CategoryUpdate, CategoryCreate, CategoryResponse
from app.services import category_services
from sqlalchemy.orm import Session
from app.db.database import get_db


router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session=Depends(get_db)):
    return category_services.get_categories(db)


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session=Depends(get_db)):
    return category_services.get_category(db, category_id)


@router.post("/", response_model=CategoryResponse)
def create_category(data: CategoryCreate, db: Session=Depends(get_db)):
    return category_services.create_category(db, data)


@router.patch("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, data: CategoryUpdate, db: Session=Depends(get_db)):
    return category_services.update_category(db, category_id, data)


@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session=Depends(get_db)):
    return category_services.delete_category(db, category_id)