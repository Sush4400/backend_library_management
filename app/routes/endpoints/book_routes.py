from fastapi import APIRouter, Depends
from app.services import book_services
from app.schemas.book_schemas import BookCreate, BookUpdate, BookResponse
from app.db.database import get_db
from sqlalchemy.orm import Session



router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookResponse])
def get_books(db: Session=Depends(get_db)):
    return book_services.get_books(db)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session=Depends(get_db)):
    return book_services.get_book(db, book_id)


@router.post("/", response_model=BookResponse)
def create_book(data: BookCreate, db: Session=Depends(get_db)):
    return book_services.create_book(db, data)


@router.patch("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, data: BookUpdate, db: Session=Depends(get_db)):
    return book_services.update_book(db, book_id, data)


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session=Depends(get_db)):
    return book_services.delete_book(db, book_id)
