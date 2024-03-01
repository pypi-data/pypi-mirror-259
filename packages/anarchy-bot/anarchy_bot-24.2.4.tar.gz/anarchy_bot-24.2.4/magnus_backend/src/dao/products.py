from typing import List

from models.products import Product

from .general import BaseDao


class ProductDao(BaseDao):
    async def number_products_in_category(self, cat_id: int) -> int:
        return await self._model.filter(category_id=cat_id).count()

    @staticmethod
    async def get_producers(product_ids: List[int]) -> List[int]:
        products = await Product.filter(id__in=product_ids)
        return list(set([(await i.producer).id for i in products if i.producer]))
