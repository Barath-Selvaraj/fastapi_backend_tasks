from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.product import ProductResponse, ProductCreate, ProductUpdate, ProductPatch
from app.services.product_service import get_product, create_product_service, update_product_service, patch_product_service, delete_product_service


router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
)
def get_product_endpoint(
    product_id: int,
    db: Session = Depends(get_db),
):

    product = get_product(
        db,
        product_id,
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product

@router.post(
    "",
    response_model = ProductResponse,
    status_code = 201 
)
def create_product_endpoint(
    product_data: ProductCreate,
    db: Session = Depends(get_db)
):
    product = create_product_service(
        db,
        product_data
    )
    return product

@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update_product(
    product_id: int,
    product_data: ProductUpdate,
    db: Session = Depends(get_db),
):

    product = update_product_service(
        db,
        product_id,
        product_data,
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product

@router.patch(
    "/{product_id}",
    response_model=ProductResponse
)
def patch_product(
    product_id: int,
    product_data: ProductPatch,
    db: Session = Depends(get_db),
):

    product = patch_product_service(
        db,
        product_id,
        product_data,
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product

@router.delete(
    "/{product_id}"
)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
):

    deleted = delete_product_service(
        db,
        product_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return {
        "message": "Product deleted successfully"
    }

