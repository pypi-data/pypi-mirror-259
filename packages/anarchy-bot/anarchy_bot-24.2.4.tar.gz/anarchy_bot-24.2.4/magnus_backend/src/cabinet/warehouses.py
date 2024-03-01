from typing import Annotated, List

from fastapi import APIRouter, Depends

from auth import get_current_active_user
from models.organizations import Employee, Organization
from models.users import User
from models.warehouses import Warehouse, PointDeliveryCompany
from permissions import check_permission_to_organisation, check_permission_to_warehouse
from schemas.statuses import ResponseStatus
from schemas.warehouses import WarehouseData, WarehouseDelRequest, WarehouseRequest, PointDeliveryCompanyRequest, \
    PointDeliveryCompanyDelRequest, PointDeliveryCompanyData

router = APIRouter(prefix="/warehouses")


@router.post("/add-warehouse", dependencies=[Depends(get_current_active_user)])
async def add_warehouse(
    data_request: WarehouseRequest,
    current_user: Annotated[User, Depends(get_current_active_user)],
    check_permission: bool = Depends(check_permission_to_organisation),
) -> ResponseStatus:
    await Warehouse.get_or_create(**data_request.model_dump())
    return ResponseStatus(status=True, message="Warehouse added")


@router.post("/update-warehouse", dependencies=[Depends(get_current_active_user)])
async def update_warehouse(
    data_request: WarehouseData,
    current_user: Annotated[User, Depends(get_current_active_user)],
    check_permission: bool = Depends(check_permission_to_organisation),
) -> ResponseStatus:
    warehouse = await Warehouse.get_or_none(id=data_request.id)

    if not warehouse:
        return ResponseStatus(status=True, message="Warehouse not found")

    warehouse.title = data_request.title
    warehouse.location = data_request.location
    await warehouse.save()
    return ResponseStatus(status=True, message="Warehouse updated")


@router.get("/warehouses", dependencies=[Depends(get_current_active_user)])
async def warehouses(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> List[WarehouseData]:
    organization_ids = [
        emp.organization.id
        for emp in await Employee.filter(user=current_user).prefetch_related(
            "organization"
        )
    ]
    organization_ids.extend(
        [org.id for org in await Organization.filter(users=current_user)]
    )
    return [
        WarehouseData(
            id=warehouse.id,
            title=warehouse.title,
            location=warehouse.location,
            organization_id=warehouse.organization.id,
            points=[PointDeliveryCompanyData(
                id=point.id,
                delivery_company_title=point.delivery_company.title,
                title=point.title,
                identifier=point.identifier,
                warehouse_id=warehouse.id,
                delivery_company_id=point.delivery_company.id
            ) for point in await PointDeliveryCompany.filter(
                warehouse=warehouse).prefetch_related("delivery_company")]
        )
        for warehouse in await Warehouse.filter(
            organization_id__in=organization_ids
        ).prefetch_related("organization")
    ]


@router.post("/del-warehouse", dependencies=[Depends(get_current_active_user)])
async def del_warehouse(
    data_request: WarehouseDelRequest,
    current_user: Annotated[User, Depends(get_current_active_user)],
    check_permission: bool = Depends(check_permission_to_organisation),
) -> ResponseStatus:
    warehouse = await Warehouse.get_or_none(
        id=data_request.id, organization_id=data_request.organization_id
    )

    if not warehouse:
        return ResponseStatus(status=True, message="Warehouse not found")
    await warehouse.delete()
    return ResponseStatus(status=True, message="Warehouse deleted")


@router.post("/add-delivery-company-point", dependencies=[Depends(get_current_active_user)])
async def add_delivery_company_point(
    data_request: PointDeliveryCompanyRequest,
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> ResponseStatus:
    warehouse = await Warehouse.get_or_none(id=data_request.warehouse_id)

    if not warehouse:
        return ResponseStatus(status=False, message="Warehouse not found")

    permission_to_warehouse = await check_permission_to_warehouse(warehouse, current_user)
    if permission_to_warehouse is False:
        return ResponseStatus(status=False, message="Access is denied")
    await PointDeliveryCompany.create(**data_request.model_dump())
    return ResponseStatus(status=True, message="Point added")


@router.post("/del-delivery-company-point", dependencies=[Depends(get_current_active_user)])
async def del_delivery_company_point(
    data_request: PointDeliveryCompanyDelRequest,
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> ResponseStatus:
    point = await PointDeliveryCompany.get_or_none(id=data_request.id)

    if not point:
        return ResponseStatus(status=False, message="Point not found")

    warehouse = await point.warehouse
    permission_to_warehouse = await check_permission_to_warehouse(warehouse, current_user)
    if permission_to_warehouse is False:
        return ResponseStatus(status=False, message="Access is denied")
    await point.delete()
    return ResponseStatus(status=True, message="Point deleted")
