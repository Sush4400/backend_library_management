from pydantic import BaseModel, Field, ConfigDict



class BookBase(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    isbn: str = Field(min_length=2, max_length=50)
    description: str|None = Field(default=None, min_length=2, max_length=255)
    publication_year: int|None = Field(default=None, ge=1000, le=2100)
    total_copies: int = Field(default=1, ge=1)
    category_id: int
    publisher_id: int|None = None


class BookCreate(BookBase):
    author_ids: list[int] = Field(default_factory=list)


class BookUpdate(BaseModel):
    title: str|None = Field(default=None, min_length=2, max_length=100)
    is_bn: str|None = Field(default=None, min_length=2, max_length=50)
    description: str|None = Field(default=None, min_length=2, max_length=255)
    publication_year: int|None = Field(default=None, ge=1000, le=2100)
    total_copies: int|None = Field(default=None, ge=1)
    category_id: int|None = None
    publisher: int|None = None
    author_ids: list[int]|None = None


class BookResponse(BookBase):
    id: int
    available_copies: int

    model_config = ConfigDict(
        from_attributes=True
    )
