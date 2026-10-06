from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import datetime

from app.models.loan import Loan, LoanStatus



def get_loans(db: Session) -> list[Loan]:
    stmt = select(Loan).order_by(Loan.id)
    return list(db.scalars(stmt).all())


def get_loan_by_id(db: Session, loan_id: int) -> Loan|None:
    stmt = select(Loan).where(Loan.id==loan_id)
    return db.scalar(stmt)


def get_active_loan_for_book(db: Session, book_id: int) -> Loan|None:
    stmt = select(Loan).where(
        Loan.book_id==book_id,
        Loan.status==LoanStatus.BORROWED
    )
    return db.scalar(stmt)


def get_active_loan_for_member_and_book(db: Session, member_id: int, book_id: int) -> Loan|None:
    stmt = select(Loan).where(
        Loan.member_id==member_id,
        Loan.book_id==book_id,
        Loan.status==LoanStatus.BORROWED
    )
    return db.scalar(stmt)


def create_loan(db: Session, loan: Loan) -> Loan:
    db.add(loan)
    db.commit()
    db.refresh(loan)
    
    return loan


def return_loan(db: Session, loan: Loan, returned_at: datetime) -> Loan:
    loan.returned_at = returned_at
    loan.status = LoanStatus.RETURNED

    db.commit()
    db.refresh(loan)

    return loan