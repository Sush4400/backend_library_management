from pydantic import BaseModel, Field


class LoanBase(BaseModel):
    pass


class LoanCreate(LoanBase):
    pass


class LoanUpdate(BaseModel):
    pass


class LoanResponse(LoanBase):
    pass