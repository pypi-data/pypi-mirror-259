import jwt
from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from core.security import jwt_decode, crypto_user
from models.organizations import Organization, check_user_in_organisation, Employee

security = HTTPBearer()


async def get_user_data(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail="Bearer token missing")
    try:
        token = credentials.credentials
        encrypt_payload = await jwt_decode(token)
        access_payload = crypto_user.decrypt_data(encrypt_payload.get('encrypt', ''))
        return access_payload
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


async def check_permission_to_organisation(
    request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)
):
    user_data = await get_user_data(credentials)
    user_id = user_data.get("user_id", 0)

    if not request.query_params.get("organization_id"):
        organization_id = (await request.json()).get("organization_id")
    else:
        organization_id = request.query_params.get("organization_id")
    organisation = (
        await Organization.filter(id=organization_id)
        .prefetch_related("organization_employees")
        .first()
    )
    if not organisation:
        raise HTTPException(status_code=404, detail="Organisation not found")
    is_in_organisation = await check_user_in_organisation(user_id, organisation)
    if is_in_organisation is False:
        raise HTTPException(status_code=404, detail="Access is denied")
    return True


async def check_permission_to_warehouse(
    warehouse, user
) -> bool:
    organization = await warehouse.organization
    owner = await organization.users

    if user in owner:
        return True

    employees = [emp.user for emp in await Employee.filter(organization=organization).prefetch_related("user")]

    if user in employees:
        return True
    return False
