from pydantic import BaseModel, Field, EmailStr
from app.models.user import UserRole



class UserBase(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    role: UserRole = UserRole.LIBRARIAN


class UserCreate(UserBase):
    password: str = Field(min_length=6, max_length=100)


class UserUpdate(BaseModel):
    name: str|None = Field(default=None, min_length=2, max_length=50)
    email: EmailStr|None = None
    password: str|None = Field(default=None, min_length=6, max_length=100)
    role: UserRole|None = None
    is_active: bool|None = None


class UserResponse(UserBase):
    id: int
    is_active: bool