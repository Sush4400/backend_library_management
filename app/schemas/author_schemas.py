from pydantic import BaseModel, Field


class AuthorBase(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    biography: str|None = Field(default=None, max_length=255)


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(BaseModel):
    name: str|None = Field(default=None, min_length=2, max_length=50)
    biography: str|None = Field(default=None, max_length=255)


class AuthorResponse(AuthorBase):
    id: int

    model_config = {
        "from_attributes": True
    }