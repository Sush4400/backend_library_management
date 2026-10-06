from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.models.loan import LoanStatus



class LoanBase(BaseModel):
    book_id: int
    member_id: int
    

class LoanCreate(LoanBase):
    due_date: datetime


class LoanReturn(BaseModel):
    returned_at: datetime|None = None


class LoanResponse(LoanBase):
    id: int
    book_id: int
    member_id: int
    issued_at: datetime
    due_date: datetime
    returned_at: datetime|None
    status = LoanStatus

    model_config = ConfigDict(
        from_attributes=True
    )