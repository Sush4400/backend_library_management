from pydantic import BaseModel, Field



class PublisherBase(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    address: str|None = Field(default=None, max_length=50)


class PublisherCreate(PublisherBase):
    pass


class PublisherUpdate(BaseModel):
    name: str|None = Field(default=None, max_length=50)
    address: str|None = Field(default=None, max_length=255)


class PublisherResponse(PublisherBase):
    id: int

    model_config = {
        "from_attributes": True
    }