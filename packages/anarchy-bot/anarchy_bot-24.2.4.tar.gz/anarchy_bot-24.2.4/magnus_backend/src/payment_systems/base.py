from typing import Dict
from abc import ABC, abstractmethod

from dao.orders import order_dao
from models.payments import PaymentLog


class PaymentSystem(ABC):
    base_url: str = ""
    account_id: str = ""
    secret_key: str = ""

    def __init__(self, params: Dict):
      self.params: Dict = params

    async def get_pyment_logs(self):
        return await PaymentLog.filter(order_id=self.params.get("order_id"))

    async def get_order(self):
        return await order_dao.get(self.params.get("order_id", 0))

    @staticmethod
    async def record_log(order_id, status, payload):
        await PaymentLog.create(order_id=order_id, status=status, payload=payload)

    @abstractmethod
    async def payment_verification(self) -> bool:
        pass

    @abstractmethod
    async def create_payment(self) -> str:
        pass
