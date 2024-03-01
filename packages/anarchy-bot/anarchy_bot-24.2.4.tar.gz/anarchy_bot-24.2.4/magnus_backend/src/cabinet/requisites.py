from typing import Annotated, Dict, List

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from starlette.status import HTTP_403_FORBIDDEN

from auth import get_current_active_user, ph
from models.organizations import check_user_in_organisation
from models.requisites import Props
from models.users import ConfirmationCode, User
from permissions import check_permission_to_organisation
from schemas.requisites import PropsDeleteRequest, PropsRequest, PropsUpdateRequest
from schemas.statuses import ResponseStatus

router = APIRouter(prefix="/user")


@router.post("/add-props")
async def add_props(
    request_data: PropsRequest,
    user: User = Depends(get_current_active_user),
    check_permission: bool = Depends(check_permission_to_organisation),
):
    await Props.create(**request_data.model_dump())

    return ResponseStatus(status=True, message="Props added")


@router.post("/update-props")
async def update_props(
    request_data: PropsUpdateRequest,
    user: User = Depends(get_current_active_user),
    check_permission: bool = Depends(check_permission_to_organisation),
):
    props = await Props.filter(id=request_data.id).first()

    if not props:
        return ResponseStatus(status=False, message="Props not found")
    props.data = request_data.data
    await props.save()
    return ResponseStatus(status=True, message="Props updated")


@router.post("/delete-props")
async def delete_props(
    request_data: PropsDeleteRequest, user: User = Depends(get_current_active_user)
):
    props = await Props.filter(id=request_data.id).first()

    if not props:
        return ResponseStatus(status=False, message="Props not found")

    organisation = await props.organization
    is_employee = await check_user_in_organisation(user.id, organisation)
    if is_employee is False:
        return ResponseStatus(status=False, message="Permission denied")

    await props.delete()
    return ResponseStatus(status=True, message="Props deleted")
