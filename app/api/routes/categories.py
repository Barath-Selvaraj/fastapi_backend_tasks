from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.category import (
    CategoryCreate,
    CategoryResponse,
)
from app.services.category_service import (
    create_category_service,
    get_category_service,
)


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)

@router.post(
    "",
    response_model=CategoryResponse,
)
def create_category(
    category_data: CategoryCreate,
    db: Session = Depends(get_db),
):

    category = create_category_service(
        db,
        category_data,
    )

    return category

@router.get(
    "/{category_id}",
    response_model=CategoryResponse,
)
def get_category(
    category_id: int,
    db: Session = Depends(get_db),
):

    category = get_category_service(
        db,
        category_id,
    )

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )

    return category