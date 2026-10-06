from fastapi import APIRouter, Depends
from app.services import loan_services
from app.schemas.loan_schemas import LoanCreate, LoanResponse, LoanReturn
from app.db.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/loans", tags=["Loans"])


@router.get("/", response_model=list[LoanResponse])
def get_loans(db: Session=Depends(get_db)):
    return loan_services.get_loans(db)


@router.get("/{loan_id}", response_model=LoanResponse)
def get_loan(loan_id: int, db: Session=Depends(get_db)):
    return loan_services.get_loan(db, loan_id)


@router.post("/", response_model=LoanResponse)
def create_loan(data: LoanCreate, db: Session=Depends(get_db)):
    return loan_services.create_loan(db, data)


@router.patch("/{loan_id}", response_model=LoanResponse)
def return_loan(loan_id: int, return_data: LoanReturn, db: Session=Depends(get_db)):
    return loan_services.return_loan(db, loan_id, return_data)
