from enum import Enum
from typing import Optional

from pydantic import BaseModel

from entities import interested, trade


class OfferCategoryRequest(BaseModel):
    title: str
    explanation: str


class OfferCategoriesRequest(BaseModel):
    class Statuses(str, Enum):
        all = "all"
        new = "new"
        accepted = "accepted"
        rejected = "rejected"


class OfferCategoryData(BaseModel):
    id: int
    title: str
    explanation: str
    user_email: str
    status: str
    answer: Optional[str]


class SelectedCategoryRequest(BaseModel):
    class Types(str, Enum):
        trade = trade
        interested = interested

    category_id: int
    type: Types


class SelectedCategoryData(BaseModel):
    id: int
    category: str
    type: str


class SelectedCategoryDelRequest(BaseModel):
    id: int
