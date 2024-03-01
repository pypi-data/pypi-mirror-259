import asyncio
import os
import subprocess
from datetime import date, timedelta

from fastapi import APIRouter, Depends, HTTPException, status

import common
import setup
from core.config import config
from core.security import get_current_active_admin_user, get_current_active_user
from dao.general import BaseDao, PaginationRequest
from dao.notifications import notification_dao
from dao.products import ProductDao
from db import User
from models.delivery import DeliveryCompany, DelLinRegion, DelLinCity
from models.payments import PaymentMethod
from models.products import Category, Product
from schemas.delivery import DeliveryCompanyRequest, DeliveryCompanyDelRequest, DelLinRegionRequest, DelLinCityRequest
from schemas.notifications import NotificationRequest
from schemas.orders import (
    PaymentMethodData,
    PaymentMethodRequest,
    PaymentMethodUpdateData,
)
from schemas.products import CategoryData, CategoryRequest
from schemas.statuses import ResponseStatus
from schemas.users import MessageResponse, SetLockUserRequest

router = APIRouter(prefix="/admin")
user_dao = BaseDao(User)
product_dao = ProductDao(Product)
category_dao = BaseDao(Category)
payment_method_dao = BaseDao(PaymentMethod)


@router.get(
    "/pull_and_restart",
)
async def pull_and_restart(
    user: User = Depends(get_current_active_user),
) -> MessageResponse:
    '''
    runs `git pull`, then restarts code
    '''
    if not user.is_admin and not user.email in config.pull_restart_emails:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not_admin")
    result = subprocess.run(
        ["git", "pull"],
        cwd=setup.app_path,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0 or "up to date" in result.stdout.lower():
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=result.stderr.strip() + result.stdout.strip(),
        )
    asyncio.create_task(common.delay_and_restart())
    return MessageResponse(message='restarting')


@router.get(
    "/status",
)
async def get_status(
    user: User = Depends(get_current_active_user),
) -> dict:
    '''
    get uptime, os, python version
    '''
    if not user.is_admin and not user.email in config.pull_restart_emails:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not_admin")
    return config.system_info


@router.get(
    "/backup_db",
    dependencies=[Depends(get_current_active_admin_user)],
)
async def backup_db() -> MessageResponse:
    if not config.db_postgres_used:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="postgres is not used",
        )
    if not config.db_pg_dump:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="pg_dump is not available, please install postgresql package",
        )
    backup_file_name = common.generate_filename(
        dir_path=setup.db_backups_path,
        extension="sql",
    )
    os.environ["PGPASSWORD"] = str(config.db_password)
    command = [
        config.db_pg_dump,
        "-h",
        config.db_hostname,
        "-U",
        config.db_username,
        config.db_name,
    ]
    with open(backup_file_name, "w") as backup_file:
        process = subprocess.Popen(
            command,
            stdout=backup_file,
            stderr=subprocess.PIPE,
        )
        _, stderr = process.communicate()
        if process.returncode != 0:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=stderr.decode(),
            )
        return MessageResponse(
            message=f"succesfully writed backup to {backup_file_name}"
        )


@router.get(
    "/users",
    dependencies=[Depends(get_current_active_admin_user)],
)
async def get_users(params: PaginationRequest = Depends(PaginationRequest)):
    return [u.info() for u in (await user_dao.list(params)).get("items", [])]


@router.post("/del_user", dependencies=[Depends(get_current_active_admin_user)])
async def del_user(user_id: int) -> bool:
    return await user_dao.delete(user_id)


@router.post("/block_user", dependencies=[Depends(get_current_active_admin_user)])
async def block_user(req: SetLockUserRequest) -> bool:
    user = await user_dao.get(req.user_id)
    if user is None:
        return False
    else:
        user.blocked_until = date.today() + timedelta(days=req.days)
        await user.save()
        return True


@router.post("/add_category", dependencies=[Depends(get_current_active_admin_user)])
async def add_category(cat: CategoryRequest) -> CategoryData:
    category = await category_dao.create(cat)
    return CategoryData(
        id=category.id, title=category.title, master_id=category.master_id
    )


@router.post("/update_category", dependencies=[Depends(get_current_active_admin_user)])
async def update_category(data: CategoryData) -> ResponseStatus:
    await category_dao.update(data)
    return ResponseStatus(status=True, message="The category was update")


@router.post("/del_category", dependencies=[Depends(get_current_active_admin_user)])
async def del_category(category_id: int) -> ResponseStatus:
    products: int = await product_dao.number_products_in_category(category_id)

    if products > 0:
        return ResponseStatus(
            status=False, message="There are products in the category"
        )

    await category_dao.delete(category_id)
    return ResponseStatus(status=True, message="The category was delete")


@router.post(
    "/add_payment_method", dependencies=[Depends(get_current_active_admin_user)]
)
async def add_payment_method(payment_method: PaymentMethodRequest) -> PaymentMethodData:
    payment_method_obj = await payment_method_dao.create(payment_method)
    return PaymentMethodData(
        id=payment_method_obj.id,
        title=payment_method.title,
        postpaid=payment_method.postpaid,
        worker=payment_method.worker,
        identifier=payment_method_obj.identifier,
    )


@router.post(
    "/update_payment_method", dependencies=[Depends(get_current_active_admin_user)]
)
async def update_payment_method(data: PaymentMethodUpdateData) -> ResponseStatus:
    await payment_method_dao.update(data)
    return ResponseStatus(status=True, message="The Payment method was update")


@router.post(
    "/del_payment_method", dependencies=[Depends(get_current_active_admin_user)]
)
async def del_payment_method(payment_method_id: int) -> ResponseStatus:
    await payment_method_dao.delete(payment_method_id)
    return ResponseStatus(status=True, message="The Payment method was delete")

@router.post("/add_notification", dependencies=[Depends(get_current_active_admin_user)])
async def add_notification(data: NotificationRequest) -> ResponseStatus:
    await notification_dao.create(data)
    return ResponseStatus(status=True, message="The notification added")


@router.post(
    "/add-delivery-company", dependencies=[Depends(get_current_active_admin_user)]
)
async def add_delivery_company(
    request_data: DeliveryCompanyRequest,
) -> ResponseStatus:
    await DeliveryCompany.create(**request_data.model_dump())
    return ResponseStatus(status=True, message="Object added")



@router.post(
    "/del-delivery-company", dependencies=[Depends(get_current_active_admin_user)]
)
async def del_delivery_company(request_data: DeliveryCompanyDelRequest) -> ResponseStatus:
    delivery_company = await DeliveryCompany.get_or_none(id=request_data.id)

    if not delivery_company:
        return ResponseStatus(status=False, message="Company not found")
    await delivery_company.delete()
    return ResponseStatus(status=True, message="Company was delete")


@router.post(
    "/add-del_line-region", dependencies=[Depends(get_current_active_admin_user)]
)
async def add_del_line_region(request_data: DelLinRegionRequest) -> ResponseStatus:
    region = await DelLinRegion.get_or_none(identifier=request_data.identifier)

    if not region:
        await DelLinRegion.create(
            title=request_data.title,
            identifier=request_data.identifier
        )
    return ResponseStatus(status=True, message="Region added")


@router.post(
    "/add-del_line-city", dependencies=[Depends(get_current_active_admin_user)]
)
async def add_del_line_city(request_data: DelLinCityRequest) -> ResponseStatus:
    city = await DelLinCity.get_or_none(identifier=request_data.identifier)

    if not city:
        await DelLinCity.create(
            title=request_data.title,
            identifier=request_data.identifier,
            region_id=request_data.region_id
        )
    return ResponseStatus(status=True, message="Region added")