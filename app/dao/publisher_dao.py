from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.publisher import Publisher
from app.schemas.publisher_schemas import PublisherUpdate



def get_publishers(db: Session) -> list[Publisher]:
    stmt = select(Publisher).order_by(Publisher.id)
    return list(db.scalars(stmt).all())


def get_publisher(db: Session, publisher_id: int) -> Publisher|None:
    stmt = select(Publisher).where(Publisher.id==publisher_id)
    return db.scalar(stmt)


def create_publisher(db: Session, publisher: Publisher) -> Publisher:
    db.add(publisher)
    db.commit()
    db.refresh(publisher)
    return publisher


def update_publisher(db: Session, publisher: Publisher, data: PublisherUpdate) -> Publisher:
    updated_data = data.model_dump(exclude_unset=True)
    for field, value in updated_data.items():
        setattr(publisher, field, value)

    db.commit()
    db.refresh(publisher)
    return publisher


def delete_publisher(db: Session, publisher: Publisher) -> None:
    db.delete(publisher)
    db.commit()
