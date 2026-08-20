from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.category import Category


def create_category(
    db: Session,
    category: Category,
) -> Category:

    db.add(category)
    db.commit()
    db.refresh(category)

    return category

def get_category_by_id(
    db: Session,
    category_id: int,
) -> Category | None:

    statement = select(Category).where(
        Category.id == category_id
    )

    category = db.scalar(statement)

    return category