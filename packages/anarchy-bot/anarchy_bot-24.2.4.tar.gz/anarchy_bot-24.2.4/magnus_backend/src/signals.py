from typing import Dict, List, Optional

from tortoise.backends.base.client import BaseDBAsyncClient
from tortoise.signals import post_save

from models.notifications import Notification
from models.organizations import Employee, Organization
from models.products import MinimumQuantity, MinimumQuantityToProduct, Product


async def make_notification(quantity: int, organization: Organization):

    users = [
        employee.user
        for employee in (
            await Employee.filter(organization=organization).prefetch_related("user")
        )
    ]
    users.append((await organization.users))
    for user in users:
        await Notification.create(
            subject="Products are running out",
            text=f"Now in stock {quantity}",
            user=user,
            sender=Notification.Senders.email,
        )


@post_save(Product)
async def signal_post_save(
    sender: Product,
    instance: Product,
    created: bool,
    using_db: Optional[BaseDBAsyncClient],
    update_fields: List[str],
) -> None:

    minimum_quantity_to_product = (
        await MinimumQuantityToProduct.filter(product=instance)
        .prefetch_related("minimum_quantity")
        .first()
    )

    organization_id = getattr(instance, "organization_id")

    organization = (
        await Organization.filter(id=organization_id)
        .prefetch_related("organization_employees")
        .first()
    )

    if organization is not None:

        if not minimum_quantity_to_product:
            minimum_quantity = await MinimumQuantity.filter(
                organization_id=organization_id
            ).first()
            if (
                minimum_quantity is not None
                and instance.amount <= minimum_quantity.quantity
            ):
                await make_notification(instance.amount, organization)
        else:
            if instance.amount <= minimum_quantity_to_product.minimum_quantity.quantity:
                await make_notification(instance.amount, organization)
