from fastapi import APIRouter, Depends
from app.services import loan_services
from app.schemas.loan_schemas import LoanCreate, LoanUpdate, LoanResponse
from app.db.database import get_db


router = APIRouter(prefix="/loans", tags=["Loans"])


router.get("/", response_model=list[LoanResponse])
def get_loans():
    pass


router.get("/{loan_id}", response_model=LoanResponse)
def get_loan():
    pass


router.post("/", response_model=LoanResponse)
def create_loan():
    pass


router.patch("/{loan_id}", response_model=LoanResponse)
def update_loan():
    pass


router.delete("/{loan_id}")
def delete_loan():
    pass