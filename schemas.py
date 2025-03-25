from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AddressInfo(BaseModel):
    address: str
    bandwidth: Optional[int]
    energy: Optional[int]
    trx_balance: Optional[float]

    class Config:
        orm_mode = True


class AddressRequestCreate(AddressInfo):
    pass


class AddressRequest(AddressInfo):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class PaginatedAddressRequests(BaseModel):
    count: int
    limit: int
    offset: int
    items: list[AddressRequest]
