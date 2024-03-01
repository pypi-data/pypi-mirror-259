from typing import List

from models.orders import OrderItem, Order

from .general import BaseDao


class OrderDao(BaseDao):
    async def get(self, obj_id: int):
        obj = await super().get(obj_id)
        await obj.fetch_related('customer')
        await obj.fetch_related('organization')
        return obj

    async def create(self, model):
        obj = await self._model.create(**model.model_dump())
        for i in model.model_dump().get('items', []):
            i.update({'order_id': obj.id})
            await OrderItem.create(**i)
        return obj

    @staticmethod
    async def order_items(order_id: int) -> List:
        return await OrderItem.filter(order_id=order_id)

    async def update_status(self, order_id, value):
        obj = await self.get(order_id)
        if obj is None:
            return False
        await obj.update_from_dict({'status': value}).save()
        return True

    @staticmethod
    async def add_item(item) -> bool:
        await OrderItem.create(**item.model_dump())
        return True

    @staticmethod
    async def delete_item(obj_id: int) -> bool:
        obj = await OrderItem.get_or_none(id=obj_id)
        if obj is None:
            return False
        else:
            await obj.delete()
            return True


order_dao = OrderDao(Order)
