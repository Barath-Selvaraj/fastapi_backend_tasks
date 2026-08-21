from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    text
)

from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.category import Category

class Product(Base):
    __tablename__ = "products"

    __table_args__ = (
        CheckConstraint(
            "price >= 0",
            name = "chk_product_price"
        ),
        CheckConstraint(
            "stock_quantity >= 0",
            name = "chk_product_stock_quantity"
        )
    )

    id : Mapped[int] = mapped_column(
        Integer,
        primary_key = True
    )

    categories_id : Mapped[int] = mapped_column(
        Integer,
        ForeignKey("categories.id"),
        nullable = False
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    stock_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        server_default=text("0"),
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default=text("TRUE"),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )