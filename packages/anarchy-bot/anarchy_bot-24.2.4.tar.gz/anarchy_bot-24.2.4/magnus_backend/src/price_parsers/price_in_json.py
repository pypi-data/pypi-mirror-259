import json

from schemas.prices import PriceItemStructureRequest

from .price import IPrice
from models.warehouses import Warehouse


class PriceInJson(IPrice):
    async def get_clean_data(self):
        products = []
        json_object = json.loads(self.raw_data)

        for product in json_object:
            product_data = {}
            for key in PriceItemStructureRequest.model_fields.keys():
                if key != "format":
                    value = self.get_data_field(
                        getattr(self.price_item_structure, key).split("/"), product
                    )
                    product_data.update({key: value})
            category = await self.get_category(product_data.get("category"))
            warehouse = await Warehouse.get(id=product_data.get("warehouse"))
            if category is None:
                continue
            product_data.update({"category_id": category.id})
            product_data.update({"producer_id": self.producer.id})
            product_data.update({"organization_id": self.organization_id})
            product_data.update({"warehouse_id": warehouse.id})
            products.append(product_data)
        return products
