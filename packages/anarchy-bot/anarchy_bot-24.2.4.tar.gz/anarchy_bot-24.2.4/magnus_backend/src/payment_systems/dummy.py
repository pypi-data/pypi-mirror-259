from dao.orders import order_dao
from entities import new, paid, success

from .base import PaymentSystem


class Dummy(PaymentSystem):
    base_url: str = ""
    account_id: str = ""
    secret_key: str = ""

    async def payment_verification(self) -> bool:
        return True

    async def create_payment(self):
        return "This is payment link"
