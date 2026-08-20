from pydantic import BaseModel
from datetime import datetime

class CategoryCreate(BaseModel):
    name: str
    discription: str | None = None

class CategoryResponse(BaseModel):
    id: int
    name: str
    discription: str | None
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

