from typing import List
from uuid import UUID

from pydantic import BaseModel

from models.orders import Order


class PaymentMethodRequest(BaseModel):
    title: str
    worker: str
    postpaid: bool


class PaymentMethodData(PaymentMethodRequest):
    id: int
    identifier: UUID


class PaymentMethodUpdateData(PaymentMethodRequest):
    id: int


class OrderItemRequest(BaseModel):
    product_id: int
    count: int


class OrderItemData(OrderItemRequest):
    id: int


class OrderRequest(BaseModel):
    customer_id: int
    organization_id: int
    items: List[OrderItemRequest]
    delivery_method: Order.DeliveryMethods
    payment_method: Order.PaymentMethods


class OrderData(BaseModel):
    id: int
    status: str
    customer_id: int
    provider_id: int
    items: List[OrderItemData]
    delivery_method: str
    payment_method: Order.PaymentMethods


class OrderUpdateData(BaseModel):
    id: int
    delivery_method: str
    payment_method: Order.PaymentMethods


class AdOrderItemRequest(BaseModel):
    order_id: int
    product_id: int
    count: int


class DelOrderItemRequest(BaseModel):
    order_id: int
    order_item_id: int


class OrderOnlyStatus(BaseModel):
    status: str


class CreatePaymentRequest(BaseModel):
    order_id: int


class PaymentCallbackRequest(BaseModel):
    id: UUID
