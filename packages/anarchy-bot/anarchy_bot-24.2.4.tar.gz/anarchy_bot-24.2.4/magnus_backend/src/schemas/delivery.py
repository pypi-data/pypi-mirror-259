from pydantic import BaseModel

from models.delivery import DeliveryCompany


class DeliveryCompanyRequest(BaseModel):
    title: str
    slug: DeliveryCompany.Slugs


class DeliveryCompanyData(DeliveryCompanyRequest):
    id: int


class DeliveryCompanyDelRequest(BaseModel):
    id: int


class DelLinRegionRequest(BaseModel):
    title: str
    identifier: str


class DelLinCityRequest(BaseModel):
    title: str
    identifier: str
    region_id: str
