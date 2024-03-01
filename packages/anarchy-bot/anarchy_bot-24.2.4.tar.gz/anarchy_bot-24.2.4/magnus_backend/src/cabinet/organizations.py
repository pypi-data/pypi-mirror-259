from typing import Annotated, List

from fastapi import APIRouter, Depends

from auth import get_current_active_user
from models.organizations import (
    DeliveryService,
    Organization,
    check_user_in_organisation,
)
from models.users import User
from permissions import check_permission_to_organisation
from schemas.organizations import (
    DeliveryServiceData,
    DeliveryServiceDelRequest,
    DeliveryServiceRequest,
)
from schemas.statuses import ResponseStatus

router = APIRouter(prefix="/organizations")


@router.post("/add-delivery-service", dependencies=[Depends(get_current_active_user)])
async def add_delivery_service(
    data_request: DeliveryServiceRequest,
    current_user: Annotated[User, Depends(get_current_active_user)],
    check_permission: bool = Depends(check_permission_to_organisation),
) -> ResponseStatus:
    await DeliveryService.get_or_create(data_request.model_dump())
    return ResponseStatus(status=True, message="Delivery service added")


@router.get("/delivery-services")
async def delivery_services(organization_id: int) -> List[DeliveryServiceData]:
    return [
        DeliveryServiceData(
            id=item.id,
            delivery_company_id=item.delivery_company.id,
            title=item.delivery_company.title,
        )
        for item in (
            await DeliveryService.filter(
                organization_id=organization_id
            ).prefetch_related("delivery_company")
        )
    ]


@router.post("/del-delivery-service", dependencies=[Depends(get_current_active_user)])
async def del_delivery_service(
    data_request: DeliveryServiceDelRequest,
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> ResponseStatus:
    delivery_service = await DeliveryService.get_or_none(id=data_request.id)

    if not delivery_service:
        return ResponseStatus(status=False, message="Object not found")

    organisation = (
        await Organization.filter(id=getattr(delivery_service, "organization_id"))
        .prefetch_related("organization_employees")
        .first()
    )

    is_in_organisation = await check_user_in_organisation(current_user.id, organisation)
    if is_in_organisation is True:
        await delivery_service.delete()
    return ResponseStatus(status=True, message="Delivery service deleted")
