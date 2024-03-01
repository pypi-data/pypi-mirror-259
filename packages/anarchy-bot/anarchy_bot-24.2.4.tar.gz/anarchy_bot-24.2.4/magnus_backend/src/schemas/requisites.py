from pydantic import BaseModel


class PropsRequest(BaseModel):
    data: str
    organization_id: int


class PropsUpdateRequest(BaseModel):
    id: int
    data: str
    organization_id: int


class PropsDeleteRequest(BaseModel):
    id: int
