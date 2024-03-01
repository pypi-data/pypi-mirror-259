from .base import PaymentSystem

from entities import new, success

from dao.orders import order_dao
from entities import paid


class YooMoney(PaymentSystem):
    base_url: str = ""
    account_id: str = ""
    secret_key: str = ""

    async def payment_verification(self) -> bool:
        pyment_logs = await self.get_pyment_logs()
        if len(pyment_logs) == 0:
            return False
        order = await self.get_order()
        await self.record_log(self.params.get("order_id"), success, self.params)
        await order_dao.update_status(self.params.get("order_id"), paid)
        return True

    async def create_payment(self):
        pyment_logs = await self.get_pyment_logs()
        if len(pyment_logs) == 0:
            await self.record_log(self.params.get("order_id"), new, self.params)
        return "This is payment link"
