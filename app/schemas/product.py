from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    categories_id: int
    name: str
    description: str | None
    price: Decimal
    stock_quantity: int = 0


class ProductUpdate(BaseModel):
    categories_id: int
    name: str
    description: str | None
    price: Decimal
    stock_quantity: int
    is_active: bool

class ProductResponse(BaseModel):
    id: int
    categories_id: int
    name: str
    description: str | None
    price: Decimal
    stock_quantity: int
    is_active: bool 
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ProductPatch(BaseModel):
    categories_id: int | None = None
    name: str | None = None
    description: str | None = None
    price: float | None = None
    stock_quantity: int | None = None
    is_active: bool | None = None     

