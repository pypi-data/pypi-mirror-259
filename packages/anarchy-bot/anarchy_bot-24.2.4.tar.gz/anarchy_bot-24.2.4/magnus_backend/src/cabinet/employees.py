import string
from random import choice
from typing import Annotated, Dict, List

from fastapi import APIRouter, Depends, Request

from auth import get_current_active_user
from core.security import ph
from models.organizations import Employee, OnBoardEmployee
from models.users import User
from permissions import check_permission_to_organisation
from schemas.employees import (
    DelEmployeeRequest,
    EmployeeData,
    EmployeeRequest,
    OnBoardEmployeeRequest,
)
from schemas.statuses import ResponseStatus
from utils import send_mail

router = APIRouter(prefix="/user")


@router.get("/employees")
async def employees(
    organization_id: str,
    user: User = Depends(get_current_active_user),
    check_permission: bool = Depends(check_permission_to_organisation),
) -> List[EmployeeData]:

    employees = [
        EmployeeData(
            id=emp.id,
            user_id=emp.user.id,
            organization_id=emp.organization.id,
            role=emp.role,
        )
        for emp in await Employee.filter(
            organization_id=organization_id
        ).prefetch_related("user", "organization")
    ]
    return employees


@router.post("/add-employee")
async def add_employee(
    request_data: EmployeeRequest,
    user: User = Depends(get_current_active_user),
    check_permission: bool = Depends(check_permission_to_organisation),
) -> ResponseStatus:
    await Employee.get_or_create(**request_data.model_dump())
    return ResponseStatus(status=True, message="Employee added")


@router.post("/del-employee")
async def del_employee(
    request_data: DelEmployeeRequest,
    user: User = Depends(get_current_active_user),
    check_permission: bool = Depends(check_permission_to_organisation),
) -> ResponseStatus:
    employee = await Employee.get_or_none(
        user_id=request_data.user_id, organization_id=request_data.organization_id
    )
    if not employee:
        return ResponseStatus(status=False, message="Employee not fount")
    await employee.delete()
    return ResponseStatus(status=True, message="Employee deleted")


@router.post("/on-board-employee")
async def on_board_employee(
    request_data: OnBoardEmployeeRequest,
    request: Request,
    user: User = Depends(get_current_active_user),
    check_permission: bool = Depends(check_permission_to_organisation),
) -> ResponseStatus:
    on_board_employee = await OnBoardEmployee.create(
        **request_data.model_dump(), user=user
    )

    message = f"You identifier: {on_board_employee.identifier}"
    await send_mail([request_data.email], "On Board Employee", message)
    return ResponseStatus(
        status=True,
        message="Email sent",
        payload={"identifier": on_board_employee.identifier},
    )


@router.get("/make-on-board")
async def make_on_board(identifier: str) -> ResponseStatus:
    on_board_employee = (
        await OnBoardEmployee.filter(identifier=identifier, used=False)
        .prefetch_related("organization")
        .first()
    )

    if not on_board_employee:
        return ResponseStatus(status=False, message="Identifier invalid")
    user = await User.filter(email=on_board_employee.email).first()

    if not user:
        mother_string = f"{string.ascii_letters}{string.digits}"
        password = "".join([choice(mother_string) for _ in range(10)])
        username = "".join([choice(mother_string) for _ in range(10)])
        password_hash = ph.hash(password)
        new_user = await User.create(
            email=on_board_employee.email,
            password_hash=password_hash,
            username=username,
        )
        await Employee.create(
            user=new_user,
            organization=on_board_employee.organization,
            role=on_board_employee.role,
        )
    else:
        await Employee.create(
            user=user,
            organization=on_board_employee.organization,
            role=on_board_employee.role,
        )
    on_board_employee.used = True
    await on_board_employee.save()
    return ResponseStatus(status=True, message="Onboarded")
