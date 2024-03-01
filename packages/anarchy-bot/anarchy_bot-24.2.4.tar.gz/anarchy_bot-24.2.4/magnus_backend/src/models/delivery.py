from enum import Enum

from tortoise import fields
from tortoise.models import Model

cdek = "cdek"
pec = "pec"
dellin = "dellin"


class DeliveryCompany(Model):
    class Slugs(str, Enum):
        cdek = cdek
        pec = pec
        dellin = dellin

    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    slug = fields.CharEnumField(Slugs, unique=True)

    def __str__(self):
        return self.title


class DelLinRegion(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    identifier = fields.CharField(max_length=255)

    def __str__(self):
        return self.title


class DelLinCity(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    identifier = fields.CharField(max_length=255)
    region_id = fields.CharField(max_length=255)

    def __str__(self):
        return self.title
