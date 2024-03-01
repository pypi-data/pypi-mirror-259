from enum import Enum
from typing import Dict, List

from fastapi import APIRouter, Depends
import core.config as config
from auth import get_current_active_user
from dao.orders import OrderDao
from delivery.cdek import cdek_worker
from delivery.pec import PEC
from models.delivery import DeliveryCompany
from models.orders import Order
from models.users import User
from schemas.delivery import DeliveryCompanyData

order_dao = OrderDao(Order)
router = APIRouter(prefix="/user")


delivery_companies = {
    "cdek": cdek_worker,
    "pec": PEC
}


class DeliveryCompanyNames(str, Enum):
    cdek = "cdek"


@router.get("/get_regions")
async def get_regions(
    delivery_company: str, user: User = Depends(get_current_active_user)
) -> List[Dict]:
    delivery_company_worker = delivery_companies.get(delivery_company, cdek_worker)
    return delivery_company_worker.get_regions()


@router.get("/get_cities")
async def get_cities(
    delivery_company: str,
    region_code: str,
    user: User = Depends(get_current_active_user),
) -> List[Dict]:
    delivery_company_worker = delivery_companies.get(delivery_company, cdek_worker)
    return delivery_company_worker.get_cities(region_code)


@router.get("/get_delivery_points")
async def get_delivery_points(
    delivery_company: str, city_code: str, user: User = Depends(get_current_active_user)
) -> List[Dict]:
    delivery_company_worker = delivery_companies.get(delivery_company, cdek_worker)
    return delivery_company_worker.get_delivery_points(city_code)


@router.get("/available-transport-companies")
async def available_transport_companies(
) -> List[DeliveryCompanyData]:
    return [DeliveryCompanyData(id=item.id, title=item.title,
                                slug=item.slug) for item in await DeliveryCompany.all()]
