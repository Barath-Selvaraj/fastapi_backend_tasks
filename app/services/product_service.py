from sqlalchemy.orm import Session

from app.repositories.product_repository import get_product_by_id, create_product, update_product, delete_product

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate, ProductPatch


def get_product(
    db: Session,
    product_id: int,
):

    product = get_product_by_id(
        db,
        product_id,
    )

    return product

def create_product_service(
    db: Session,
    product_data: ProductCreate
) -> Product:
    product = Product(
        categories_id=product_data.categories_id,
        name=product_data.name,
        description=product_data.description,
        price=product_data.price,
        stock_quantity=product_data.stock_quantity
    )
    return create_product(
        db,
        product
    )

def update_product_service(
    db: Session,
    product_id: int,
    product_data: ProductUpdate,
) -> Product | None:

    product = get_product_by_id(
        db,
        product_id,
    )

    if product is None:
        return None

    product.categories_id = product_data.categories_id
    product.name = product_data.name
    product.description = product_data.description
    product.price = product_data.price
    product.stock_quantity = product_data.stock_quantity
    product.is_active = product_data.is_active

    return update_product(
        db,
        product,
    )

def patch_product_service(
    db: Session,
    product_id: int,
    product_data: ProductPatch,
) -> Product | None:

    product = get_product_by_id(
        db,
        product_id,
    )

    if product is None:
        return None

    update_data = product_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(product, field, value)

    return update_product(
        db,
        product,
    )

def delete_product_service(
    db: Session,
    product_id: int,
) -> bool:

    product = get_product_by_id(
        db,
        product_id,
    )

    if product is None:
        return False

    delete_product(
        db,
        product,
    )

    return True