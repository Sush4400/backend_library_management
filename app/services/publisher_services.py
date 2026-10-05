from sqlalchemy.orm import Session
from app.models import Publisher
from app.schemas.publisher_schemas import PublisherCreate, PublisherUpdate
from app.dao import publisher_dao
from fastapi import HTTPException, status



def get_publishers(db: Session):
    return publisher_dao.get_publishers(db)


def get_publisher(db: Session, publisher_id: int):
    publisher = publisher_dao.get_publisher(db, publisher_id)
    if not publisher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Publisher not found"
        )
    return publisher


def create_publisher(db: Session, data: PublisherCreate):
    publisher = Publisher(**data.model_dump())
    return publisher_dao.create_publisher(db, publisher)


def update_publisher(db: Session, publisher_id: int, data: PublisherUpdate):
    publisher = get_publisher(db, publisher_id)
    return publisher_dao.update_publisher(db, publisher, data)


def delete_publisher(db: Session, publisher_id: int):
    publisher = get_publisher(db, publisher_id)
    return publisher_dao.delete_publisher(db, publisher)