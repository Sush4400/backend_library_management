from fastapi import APIRouter, Depends
from app.services import author_services
from app.schemas.author_schemas import AuthorCreate, AuthorUpdate, AuthorResponse
from app.db.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/authors", tags=["Authors"])


@router.get("/", response_model=list[AuthorResponse])
def get_authors(db: Session=Depends(get_db)):
    return author_services.get_authors(db)


@router.get("/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int, db: Session=Depends(get_db)):
    return author_services.get_author(db, author_id)


@router.post("/", response_model=AuthorResponse)
def create_author(data: AuthorCreate, db: Session=Depends(get_db)):
    return author_services.create_author(db, data)


@router.patch("/{author_id}", response_model=AuthorResponse)
def update_author(author_id: int, data: AuthorUpdate, db: Session=Depends(get_db)):
    return author_services.update_author(db, author_id, data)


@router.delete("/{author_id}")
def delete_author(author_id: int, db: Session=Depends(get_db)):
    return author_services.delete_author(db, author_id)