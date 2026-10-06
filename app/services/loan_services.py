from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime, timezone

from app.models.loan import Loan, LoanStatus
from app.dao import loan_dao
from app.schemas.loan_schemas import LoanCreate, LoanReturn



def get_loans(db: Session):
    return loan_dao.get_loans(db)


def get_loan(db: Session, loan_id: int):
    loan = loan_dao.get_loan_by_id(db, loan_id)
    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Loan not found"
        )
    return loan


def create_loan(db: Session, data: LoanCreate):
    existing_loan = loan_dao.get_active_loan_for_book(db, data.book_id)
    if existing_loan:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Book is already borrowed"
        )
    issued_at = datetime.now(timezone.utc)
    loan = Loan(
        book_id=data.book_id,
        member_id=data.member_id,
        issued_at=issued_at,
        due_dat=data.due_date,
        status=LoanStatus.BORROWED
    )
    return loan_dao.create_loan(db, loan)


def return_loan(db: Session, loan_id: int, return_data: LoanReturn):
    loan = loan_dao.get_loan_by_id(db, loan_id)
    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Loan not found"
        )

    if loan.status == LoanStatus.RETURNED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Loan has already been returned."
        )
    returned_at = return_data.returned_at if return_data.returned_at else datetime.now(timezone.utc)
    return loan_dao.return_loan(db, loan, returned_at)