from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.category import Category
from app.schemas.category_schemas import CategoryUpdate



def get_categories(db: Session) -> list[Category]:
    stmt = select(Category).order_by(Category.id)
    return list(db.scalars(stmt).all())


def get_category(db: Session, category_id: int) -> Category|None:
    stmt = select(Category).where(Category.id==category_id)
    return db.scalar(stmt)


def create_category(db: Session, category: Category) -> Category:
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def update_category(db: Session, category: Category, data: CategoryUpdate) -> Category:
    updated_data = data.model_dump(exclude_unset=True)
    for field, value in updated_data.items():
        setattr(category, field, value)
    db.commit()
    db.refresh(category)
    return category


def delete_category(db: Session, category: Category) -> None:
    db.delete(category)
    db.commit()
