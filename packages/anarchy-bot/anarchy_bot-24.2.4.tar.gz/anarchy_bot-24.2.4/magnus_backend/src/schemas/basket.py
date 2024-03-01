from pydantic import BaseModel

from models.orders import Order


class ProductInBasketRequest(BaseModel):
    product_id: int
    count: int


class ProductInBasketData(ProductInBasketRequest):
    id: int
    title: str
    img: str


class ProductInBasketDelRequest(BaseModel):
    id: int


class ProductInBasketUpdateRequest(ProductInBasketDelRequest):
    count: int


class CheckOutRequest(BaseModel):
    payment_method: Order.PaymentMethods
    delivery_method: Order.DeliveryMethods
