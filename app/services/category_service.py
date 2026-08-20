from sqlalchemy.orm import Session

from app.models.category import Category
from app.repositories.category_repository import create_category, get_category_by_id
from app.schemas.category import CategoryCreate


def create_category_service(
    db: Session,
    category_data: CategoryCreate,
) -> Category:

    category = Category(
        name=category_data.name,
        discription=category_data.discription,
    )

    return create_category(
        db,
        category,
    )

def get_category_service(
    db: Session,
    category_id: int,
) -> Category | None:

    return get_category_by_id(
        db,
        category_id,
    )