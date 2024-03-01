from tortoise import fields
from tortoise.models import Model

from . import CreatedUpdatedModel


class Props(Model, CreatedUpdatedModel):
    id = fields.IntField(pk=True)
    data = fields.TextField()
    organization = fields.ForeignKeyField(
        "models.Organization", related_name="requisites"
    )

    def __str__(self):
        return self.data
