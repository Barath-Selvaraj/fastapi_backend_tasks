from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product


def get_product_by_id(
    db: Session,
    product_id: int,
) -> Product | None:

    statement = select(Product).where(
        Product.id == product_id
    )

    return db.scalar(statement)

def create_product(
        db: Session,
        product: Product
) -> Product:
    
    db.add(product)
    db.commit()
    db.refresh(product)

    return product

def update_product(
        db: Session,
        product: Product
) -> Product:
    db.commit()
    db.refresh(product)

    return product

def update_product(
    db: Session,
    product: Product
) -> Product:

    db.commit()
    db.refresh(product)

    return product    

def delete_product(
    db: Session,
    product: Product
) -> None:

    db.delete(product)
    db.commit()