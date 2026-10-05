from pydantic import BaseModel, EmailStr, Field
from datetime import date



class MemberBase(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    phone: str = Field(min_length=10, max_length=20)
    address: str|None = Field(default=None, max_length=255)
    membership_date: date
    is_active: bool = True


class MemberCreate(MemberBase):
    pass


class MemberUpdate(BaseModel):
    name: str|None = Field(default=None, min_length=2, max_length=50)
    email: EmailStr|None = None
    phone: str|None = Field(default=None, min_length=10, max_length=20)
    address: str|None = Field(default=None, max_length=255)
    is_active: bool|None = None


class MemberResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    address: str|None
    membership_date: date
    is_active: bool

    model_config = {
        'from_attributes': True
    }