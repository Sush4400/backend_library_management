from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.book import Book
from app.models.book_author import BookAuthor
from app.schemas.book_schemas import BookUpdate, BookCreate



def get_books(db: Session) -> list[Book]:
    stmt = select(Book).order_by(Book.id)
    return list(db.scalars(stmt).all())


def get_book(db: Session, book_id: int) -> Book|None:
    stmt = select(Book).where(Book.id==book_id)
    return db.scalar(stmt)


def get_book_by_isbn(db: Session, isbn: str) -> Book|None:
    stmt = select(Book).where(Book.isbn==isbn)
    return db.scalar(stmt)


def create_book(db: Session, book: Book) -> Book:
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def update_book(db: Session, book: Book, update_data: dict) -> Book:
    for field, value in update_data.items():
        setattr(book, field, value)
    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book: Book) -> None:
    db.delete(book)
    db.commit()