from tortoise import fields
from tortoise.models import Model
from enum import Enum

from entities import interested, trade
from . import CreatedUpdatedModel


class Category(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    master = fields.ForeignKeyField(
        "models.Category", related_name="categories", null=True
    )

    def get_master_id(self):
        return None if self.master is None else self.master.pk

    def __str__(self):
        return self.title


class Product(Model, CreatedUpdatedModel):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    producer = fields.ForeignKeyField("models.User", related_name="producer_products")
    description = fields.TextField(null=True)
    category = fields.ForeignKeyField("models.Category", related_name="products")
    img = fields.TextField(null=True)
    amount = fields.IntField(default=1)
    warehouse = fields.ForeignKeyField("models.Warehouse", related_name="warehouse_products")
    organization = fields.ForeignKeyField("models.Organization", related_name="organization_products")
    weight = fields.IntField(default=1)
    length = fields.IntField(default=1)
    width = fields.IntField(default=1)
    height = fields.IntField(default=1)

    def __str__(self):
        return self.title


class MinimumQuantity(Model, CreatedUpdatedModel):
    id = fields.IntField(pk=True)
    organization = fields.ForeignKeyField(
        "models.Organization", related_name="organization_minimum_quantity_goods"
    )
    quantity = fields.IntField()


class MinimumQuantityToProduct(Model, CreatedUpdatedModel):
    minimum_quantity = fields.ForeignKeyField("models.MinimumQuantity",
                                                   related_name="minimum_quantity_products")
    product = fields.ForeignKeyField("models.Product",
                                     related_name="minimum_quantity_product_products")


class OfferCategory(Model, CreatedUpdatedModel):
    class Statuses(str, Enum):
        new = "new"
        accepted = "accepted"
        rejected = "rejected"

    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    user = fields.ForeignKeyField(
        "models.User"
    )
    explanation = fields.TextField()
    status = fields.CharEnumField(Statuses, default=Statuses.new)
    answer = fields.TextField(null=True)

    def __str__(self):
        return self.title


class SelectedCategory(Model, CreatedUpdatedModel):
    class Types(str, Enum):
        trade = trade
        interested = interested

    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User")
    category = fields.ForeignKeyField("models.Category", related_name="selected_categories")
    type = fields.CharEnumField(Types)

    def __str__(self):
        return self.category.title
