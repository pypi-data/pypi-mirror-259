from pydantic import BaseModel
from typing import List


class PointDeliveryCompanyRequest(BaseModel):
    title: str
    identifier: str
    warehouse_id: int
    delivery_company_id: int


class PointDeliveryCompanyDelRequest(BaseModel):
    id: int


class PointDeliveryCompanyData(PointDeliveryCompanyRequest):
    id: int
    delivery_company_title: str


class WarehouseRequest(BaseModel):
    title: str
    location: str
    organization_id: int


class WarehouseData(BaseModel):
    id: int
    title: str
    location: str
    organization_id: int
    points: List[PointDeliveryCompanyData] = []


class WarehouseDelRequest(BaseModel):
    id: int
    organization_id: int
