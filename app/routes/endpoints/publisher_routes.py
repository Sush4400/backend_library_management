from fastapi import APIRouter, Depends
from app.services import publisher_services
from app.schemas.publisher_schemas import PublisherCreate, PublisherUpdate, PublisherResponse
from app.db.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/publishers", tags=["Publishers"])


@router.get("/", response_model=list[PublisherResponse])
def get_publishers(db: Session=Depends(get_db)):
    return publisher_services.get_publishers(db)


@router.get("/{publisher_id}", response_model=PublisherResponse)
def get_publisher(publisher_id: int, db: Session=Depends(get_db)):
    return publisher_services.get_publisher(db, publisher_id)


@router.post("/", response_model=PublisherResponse)
def create_publisher(data: PublisherCreate, db: Session=Depends(get_db)):
    return publisher_services.create_publisher(db, data)


@router.patch("/{publisher_id}", response_model=PublisherResponse)
def update_publisher(publisher_id: int, data: PublisherUpdate, db: Session=Depends(get_db)):
    return publisher_services.update_publisher(db, publisher_id, data)

@router.delete("/{publisher_id}")
def delete_publisher(publisher_id: int, db: Session=Depends(get_db)):
    return publisher_services.delete_publisher(db, publisher_id)