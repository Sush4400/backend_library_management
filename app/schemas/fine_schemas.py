from pydantic import BaseModel, Field


class FineBase(BaseModel):
    pass


class FineCreate(FineBase):
    pass


class FineUpdate(BaseModel):
    pass


class FineResponse(FineBase):
    pass