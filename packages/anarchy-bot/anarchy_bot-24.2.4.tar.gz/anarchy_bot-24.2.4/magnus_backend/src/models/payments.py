from tortoise.models import Model
from tortoise import fields
from uuid import uuid4
from enum import Enum

from . import CreatedUpdatedModel
from entities import new, success, failure


class PaymentMethod(Model):
    class Workers(str, Enum):
        cash = 'cash'
        yoo_money = 'yoo_money'

    title = fields.CharField(max_length=255)
    identifier = fields.UUIDField(default=uuid4)
    worker = fields.CharEnumField(Workers, unique=True)
    postpaid = fields.BooleanField(default=False)

    def __str__(self):
        return self.title


class PaymentLog(Model, CreatedUpdatedModel):
    class Statuses(str, Enum):
        new = new
        success = success
        failure = failure

    order = fields.ForeignKeyField("models.Order", related_name="payment_logs")
    status = fields.CharEnumField(Statuses)
    payload = fields.TextField()
