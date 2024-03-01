from tortoise import fields
from tortoise.models import Model


class CreatedUpdatedModel:
    created = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)

