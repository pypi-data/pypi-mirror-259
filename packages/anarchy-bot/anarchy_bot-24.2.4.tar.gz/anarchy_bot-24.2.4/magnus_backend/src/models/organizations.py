from enum import Enum
from uuid import uuid4

from tortoise import fields
from tortoise.models import Model

from . import CreatedUpdatedModel


class Organization(Model):
    id = fields.IntField(pk=True)
    inn = fields.CharField(max_length=15, unique=True)
    ogrn = fields.CharField(max_length=15, unique=True)
    org_name = fields.TextField()
    org_actual_address = fields.TextField()
    org_legal_address = fields.TextField()
    users = fields.ManyToManyField("models.User", related_name="organization")


class Employee(Model):
    class Roles(str, Enum):
        admin = "admin"
        manager = "manager"

    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="employees")
    organization = fields.ForeignKeyField(
        "models.Organization", related_name="organization_employees"
    )
    role = fields.CharEnumField(Roles, default=Roles.manager)


async def check_user_in_organisation(user_id: int, organisation) -> bool:
    owner = await organisation.users
    employees = await organisation.organization_employees.all().prefetch_related("user")
    if user_id in (org.id for org in owner) or user_id in [emp.user.id for emp in employees]:
        return True
    return False


class OnBoardEmployee(Model, CreatedUpdatedModel):
    class Roles(str, Enum):
        admin = "admin"
        manager = "manager"

    id = fields.IntField(pk=True)
    identifier = fields.UUIDField(default=uuid4)
    email = fields.CharField(max_length=255)
    organization = fields.ForeignKeyField(
        "models.Organization", related_name="organization_on_board_employees"
    )
    user = fields.ForeignKeyField("models.User", related_name="user_on_board_employees")
    role = fields.CharEnumField(Roles, default=Roles.manager)
    used = fields.BooleanField(default=False)


class DeliveryService(Model):
    id = fields.IntField(pk=True)
    delivery_company = fields.ForeignKeyField("models.DeliveryCompany",
                                              related_name="delivery_services")
    organization = fields.ForeignKeyField(
        "models.Organization", related_name="organization_delivery_services"
    )
