from pydantic import BaseModel

from models.prices import PriceItemStructure


class PriceItemStructureRequest(BaseModel):
    format: PriceItemStructure.Formats
    title: str
    price: str
    description: str
    category: str
    amount: str
    img: str
    warehouse: str
    weight: str
    length: str
    width: str
    height: str
