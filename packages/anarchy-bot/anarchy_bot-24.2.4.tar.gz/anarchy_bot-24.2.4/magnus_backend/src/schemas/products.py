from decimal import Decimal
from typing import Optional, List, Annotated

from pydantic import BaseModel, field_validator, Field


class CategoryRequest(BaseModel):
    title: str
    master_id: Optional[int] = None


class CategoryData(CategoryRequest):
    id: int


class ProductRequest(BaseModel):
    title: str
    price: Decimal
    producer_id: Optional[int] = None
    description: str
    category_id: int
    img: str
    amount: int
    warehouse_id: int
    organization_id: int
    weight: Annotated[int, Field(gt=0)]
    length: Annotated[int, Field(gt=0)]
    width: Annotated[int, Field(gt=0)]
    height: Annotated[int, Field(gt=0)]

    @field_validator("price")
    def convert_decimal(v):
        return Decimal("{:.{prec}f}".format(v, prec=2))


class ProductData(ProductRequest):
    id: int


class MinimumQuantityGoodRequest(BaseModel):
    organization_id: int
    products: List[int]
    quantity: int


class DeleteMinimumQuantityGoodRequest(BaseModel):
    organization_id: int
    id: int
