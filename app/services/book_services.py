from sqlalchemy.orm import Session
from app.models.book_author import BookAuthor
from app.models.book import Book
from fastapi import HTTPException, status
from app.schemas.book_schemas import BookCreate, BookUpdate
from app.dao import book_dao, author_dao



def get_books(db: Session):
    return book_dao.get_books(db)


def get_book(db: Session, book_id: int):
    book = book_dao.get_book(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    return book


def create_book(db: Session, data: BookCreate):
    existing_book = book_dao.get_book_by_isbn(db, data.isbn)
    if existing_book:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="ISBN already registered"
        )

    authors = author_dao.get_authors_by_ids(db, data.author_ids)
    if len(authors) != len(set(data.author_ids)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="One or more author doesn't exist."
        )

    book = Book(
        title=data.title,
        isbn=data.isbn,
        description=data.description,
        publication_year=data.publication_year,
        total_copies=data.total_copies,
        avaiable_copies=data.total_copies,
        category_id=data.category_id,
        publisher_id=data.publisher_id,
        authors=authors
    )
    return book_dao.create_book(db, book)


def update_book(db: Session, book_id: int, data: BookUpdate):
    book = get_book(db, book_id)
    update_data = data.model_dump(exclude_unset=True)
    if "isbn" in update_data:
        existing_book = book_dao.get_book_by_isbn(db, update_data["isbn"])
        


def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    return book_dao.delete_book(db, book)





def update_book(
    db: Session,
    book_id: int,
    data: BookUpdate
) -> Book:

    book = get_book(db, book_id)

    update_data = data.model_dump(
        exclude_unset=True
    )

    # Check duplicate ISBN
    if "isbn" in update_data:

        existing_book = book_dao.get_book_by_isbn(
            db,
            update_data["isbn"]
        )

        if (
            existing_book
            and existing_book.id != book.id
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="ISBN already registered."
            )

    # Handle total copies
    if "total_copies" in update_data:

        new_total = update_data["total_copies"]

        borrowed_copies = (
            book.total_copies -
            book.available_copies
        )

        if new_total < borrowed_copies:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=(
                    "Total copies cannot be less than "
                    "the number of borrowed copies."
                )
            )

        update_data["available_copies"] = (
            new_total - borrowed_copies
        )

    return book_dao.update_book(
        db,
        book,
        update_data
    )