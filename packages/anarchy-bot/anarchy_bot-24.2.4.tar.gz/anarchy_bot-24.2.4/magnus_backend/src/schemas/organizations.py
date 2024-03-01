from pydantic import BaseModel


class OrganizationResponse(BaseModel):
    inn: str
    ogrn: str
    name: str
    legal_address: str
    firstname: str
    lastname: str
    phone_number: str


class DeliveryServiceRequest(BaseModel):
    delivery_company_id: int
    organization_id: int


class DeliveryServiceData(BaseModel):
    id: int
    delivery_company_id: int
    title: str


class DeliveryServiceDelRequest(BaseModel):
    id: int
