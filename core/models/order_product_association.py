from sqlalchemy import Table, Column, Integer, ForeignKey, UniqueConstraint

from .base import Base

order_product_associations_table = Table(
    "order_product_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", ForeignKey("order.id"), nullable=False),
    Column("product_id", ForeignKey("product.id"), nullable=False),
    UniqueConstraint("order_id", "product_id", name="idx_unique_order_product"),
)
