from tortoise.models import Model
from tortoise import fields
from enum import Enum
from uuid import uuid4

from . import CreatedUpdatedModel
from entities import (in_processing, accepted, awaiting_payment, paid, not_available, awaiting_customer_decision,
                      completed, canceled, deal_refusal, delivery, pickup, cashless, cash, draft)


class Order(Model, CreatedUpdatedModel):
    class DeliveryMethods(str, Enum):
        delivery = delivery
        pickup = pickup

    class Statuses(str, Enum):
        draft = draft
        in_processing = in_processing
        accepted = accepted
        awaiting_payment = awaiting_payment
        paid = paid
        not_available = not_available
        awaiting_customer_decision = awaiting_customer_decision
        completed = completed
        canceled = canceled
        deal_refusal = deal_refusal

    class PaymentMethods(str, Enum):
        cashless = cashless
        cash = cash

    id = fields.IntField(pk=True)
    status = fields.CharEnumField(Statuses, default=Statuses.in_processing)
    customer = fields.ForeignKeyField('models.User', related_name='customer_orders')
    organization = fields.ForeignKeyField('models.Organization', related_name='organization_orders')
    payment_method = fields.CharEnumField(PaymentMethods)
    delivery_method = fields.CharEnumField(DeliveryMethods)


class OrderItem(Model, CreatedUpdatedModel):
    id = fields.IntField(pk=True)
    order = fields.ForeignKeyField("models.Order", related_name="order_items")
    product = fields.ForeignKeyField(
        'models.Product', related_name='product_order_items'
    )
    count = fields.IntField()
