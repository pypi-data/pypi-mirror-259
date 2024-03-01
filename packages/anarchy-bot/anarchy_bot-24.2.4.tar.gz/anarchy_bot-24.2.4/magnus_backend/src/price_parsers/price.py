from abc import ABC, abstractmethod
from typing import Dict, List

from models.products import Category


class IPrice(ABC):
    def __init__(self, raw_data, producer, organization_id, price_item_structure):
        self.raw_data = raw_data
        self.producer = producer
        self.price_item_structure = price_item_structure
        self.organization_id = organization_id

    async def get_category(self, value):
        category = await Category.filter(title=value).first()
        return category

    @abstractmethod
    async def get_clean_data(self) -> List[Dict]:
        pass

    def get_data_field(self, keys, item):
        if len(keys) == 0:
            return item
        key = keys[0]
        return self.get_data_field(keys[1:], item[key])
