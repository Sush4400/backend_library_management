from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services import fine_services
from app.schemas.fine_schemas import FineResponse
from app.db.database import get_db


router = APIRouter(prefix="/fines", tags=["Fines"])


@router.get("/", response_model=list[FineResponse])
def get_fines(db: Session=Depends(get_db)):
    return fine_services.get_fines(db)


@router.get("/{fine_id}", response_model=FineResponse)
def get_fine(fine_id: int, db: Session=Depends(get_db)):
    return fine_services.get_fine(db, fine_id)


@router.post("/{fine_id}/pay", response_model=FineResponse)
def pay_fine(fine_id: int, db: Session=Depends(get_db)):
    return fine_services.pay_fine(db, fine_id)
