from enum import Enum

from tortoise import fields
from tortoise.models import Model

from entities import format_json


class PriceItemStructure(Model):
    class Formats(str, Enum):
        format_json = format_json

    id = fields.IntField(pk=True)
    format = fields.CharEnumField(Formats)
    title = fields.CharField(max_length=255)
    price = fields.CharField(max_length=255)
    description = fields.CharField(max_length=255)
    category = fields.CharField(max_length=255)
    amount = fields.CharField(max_length=255)
    img = fields.CharField(max_length=255)
    user = fields.ForeignKeyField("models.User", related_name="price_item_structures")
    warehouse = fields.CharField(max_length=255)
    weight = fields.CharField(max_length=255)
    length = fields.CharField(max_length=255)
    width = fields.CharField(max_length=255)
    height = fields.CharField(max_length=255)

    def __str__(self):
        return self.format
