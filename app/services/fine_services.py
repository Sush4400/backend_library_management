from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime, timezone

from app.dao import fine_dao



def get_fines(db: Session):
    return fine_dao.get_fines(db)


def get_fine(db: Session, fine_id: int):
    fine = fine_dao.get_fine(db, fine_id)
    if not fine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fine not found"
        )
    return fine


def pay_fine(db: Session, fine_id: int):
    fine = get_fine(db, fine_id)
    if fine.paid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Fine has already been paid."
        )
    paid_at = datetime.now(timezone.utc)
    return fine_dao.pay_fine(db, fine, paid_at)