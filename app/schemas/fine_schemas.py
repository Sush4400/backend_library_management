from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from decimal import Decimal



class FineBase(BaseModel):
    loan_id: int
    amount: Decimal = Field(ge=0)


class FineResponse(FineBase):
    id: int
    paid: bool
    paid_at: datetime|None = None

    model_config = ConfigDict(
        from_attributes=True
    )