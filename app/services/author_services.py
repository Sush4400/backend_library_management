from sqlalchemy.orm import Session
from app.dao import author_dao
from app.models.author import Author
from fastapi import HTTPException, status
from app.schemas.author_schemas import AuthorCreate, AuthorUpdate



def get_authors(db: Session):
    return author_dao.get_authors(db)


def get_author(db: Session, author_id: int):
    author = author_dao.get_author(db, author_id)
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Author not found"
        )
    return author


def create_author(db: Session, data: AuthorCreate):
    author = Author(**data.model_dump())
    return author_dao.create_author(db, author)


def update_author(db: Session, author_id: int, data: AuthorUpdate):
    author = get_author(db, author_id)
    return author_dao.update_author(db, author, data)


def delete_author(db: Session, author_id):
    author = get_author(db, author_id)
    return author_dao.delete_author(db, author)