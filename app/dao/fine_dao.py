from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime

from app.models.fine import Fine



def get_fines(db: Session) -> list[Fine]:
    stmt = select(Fine).order_by(Fine.id)
    return list(db.scalars(stmt).all())


def get_fine(db: Session, fine_id: int) -> Fine|None:
    stmt = select(Fine).where(Fine.id==fine_id)
    return db.scalar(stmt)


def pay_fine(db: Session, fine: Fine, paid_at: datetime) -> Fine:
    fine.paid = True
    fine.paid_at = paid_at

    db.commit()
    db.refresh(fine)
    
    return fine