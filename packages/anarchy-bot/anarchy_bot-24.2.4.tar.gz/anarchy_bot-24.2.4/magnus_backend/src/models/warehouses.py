from tortoise import fields
from tortoise.models import Model

from . import CreatedUpdatedModel


class Warehouse(Model, CreatedUpdatedModel):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    location = fields.CharField(max_length=255)
    organization = fields.ForeignKeyField(
        "models.Organization", related_name="warehouses"
    )

    def __str__(self):
        return self.title


class PointDeliveryCompany(Model, CreatedUpdatedModel):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    identifier = fields.CharField(max_length=255)
    warehouse = fields.ForeignKeyField(
        "models.Warehouse", related_name="points"
    )
    delivery_company = fields.ForeignKeyField("models.DeliveryCompany",
                                              related_name="delivery_company_points")

    def __str__(self):
        return self.title
