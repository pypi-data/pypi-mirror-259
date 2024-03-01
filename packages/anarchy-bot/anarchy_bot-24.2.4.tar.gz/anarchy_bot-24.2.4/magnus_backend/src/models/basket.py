from tortoise import fields
from tortoise.models import Model

from . import CreatedUpdatedModel


class ProductInBasket(Model, CreatedUpdatedModel):
    id = fields.IntField(pk=True)
    product = fields.ForeignKeyField("models.Product", related_name="basket_products")
    user = fields.ForeignKeyField("models.User", related_name="user_basket_products")
    count = fields.IntField()
