from app.models.author import Author
from sqlalchemy.orm import Session
from app.schemas.author_schemas import AuthorCreate, AuthorUpdate
from sqlalchemy import select



def get_authors(db: Session) -> list[Author]:
    stmt = select(Author).order_by(Author.id)
    return list(db.scalars(stmt).all())


def get_author(db: Session, author_id: int) -> Author|None:
    stmt = select(Author).where(Author.id==author_id)
    return db.scalar(stmt)


def create_author(db: Session, author: Author) -> Author:
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


def update_author(db: Session, author: Author, data: AuthorUpdate) -> Author:
    updated_data = data.model_dump(exclude_unset=True)
    for field, value in updated_data.items():
        setattr(author, field, value)
    db.commit()
    db.refresh(author)
    return author


def delete_author(db: Session, author: Author) -> None:
    db.delete(author)
    db.commit()


def get_authors_by_ids(db: Session, author_ids: list[int]) -> list[Author]:
    if not author_ids:
        return []
    stmt = select(Author).where(Author.id.in_(author_ids))
    return list(db.scalars(stmt).all())