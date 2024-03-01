from pydantic import BaseModel, EmailStr

from models.organizations import Employee, OnBoardEmployee


class EmployeeRequest(BaseModel):
    user_id: int
    organization_id: int
    role: Employee.Roles


class EmployeeData(EmployeeRequest):
    id: int


class DelEmployeeRequest(BaseModel):
    user_id: int
    organization_id: int


class OnBoardEmployeeRequest(BaseModel):
    email: EmailStr
    organization_id: int
    role: OnBoardEmployee.Roles
