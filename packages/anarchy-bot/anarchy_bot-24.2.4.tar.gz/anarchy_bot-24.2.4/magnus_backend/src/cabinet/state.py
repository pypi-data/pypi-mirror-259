from __future__ import annotations
from abc import ABC, abstractmethod

from models.orders import Order
from dao.orders import OrderDao
from enum import Enum
from schemas.statuses import ResponseStatus

order_dao = OrderDao(Order)


class Context:
    def __init__(self, state: State) -> None:
        self._state = state

    @property
    def state(self):
        return self._state

    async def positive(self):
        await self._state.positive()

    async def negative(self):
        await self._state.negative()


class State(ABC):
    def __init__(self, order, user):
        self._order = order
        self._user = user

    @abstractmethod
    async def positive(self):
        pass

    @abstractmethod
    async def negative(self):
        pass


class InProgressState(State):
    async def positive(self):
        await order_dao.update_status(self._order.id, Order.Statuses.accepted)

    async def negative(self):
        await order_dao.update_status(self._order.id, Order.Statuses.deal_refusal)

    def __str__(self):
        return 'In progress'


class AcceptedState(State):
    async def positive(self):
        await order_dao.update_status(self._order.id, Order.Statuses.awaiting_customer_decision)

    async def negative(self):
        await order_dao.update_status(self._order.id, Order.Statuses.not_available)


class NotAvailableState(State):
    async def positive(self):
        await order_dao.update_status(self._order.id, Order.Statuses.canceled)

    async def negative(self):
        await order_dao.update_status(self._order.id, Order.Statuses.accepted)


class AwaitingCustomerDecisionState(State):
    async def positive(self):
        await order_dao.update_status(self._order.id, Order.Statuses.completed)

    async def negative(self):
        await order_dao.update_status(self._order.id, Order.Statuses.canceled)


class DummyState(State):
    async def positive(self):
        pass

    async def negative(self):
        pass


STATUSES = {
    Order.Statuses.accepted.value: AcceptedState,
    Order.Statuses.in_processing.value: InProgressState,
    Order.Statuses.not_available.value: NotAvailableState,
    Order.Statuses.awaiting_customer_decision.value: AwaitingCustomerDecisionState,
}


class Direction(str, Enum):
    positive = 'positive'
    negative = 'negative'


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, order, user) -> ResponseStatus:
        pass


class AbstractHandler(Handler):

    _next_handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, order, user) -> ResponseStatus:
        if self._next_handler:
            return self._next_handler.handle(order, user)

        return None


class ExistsOrderHandler(AbstractHandler):
    def handle(self, order, user) -> ResponseStatus:
        if order is None:
            return ResponseStatus(status=False, message='Order does not exist')
        else:
            return super().handle(order, user)


class AccessRightsOrderHandler(AbstractHandler):
    def handle(self, order, user) -> ResponseStatus:
        if order.customer != user and order.provider != user:
            return ResponseStatus(status=False, message='You do not have access rights')
        else:
            return super().handle(order, user)


class StatusDoesNotExistHandler(AbstractHandler):
    def handle(self, order, user) -> ResponseStatus:
        if STATUSES.get(order.status) is None:
            return ResponseStatus(status=False, message='Invalid status for change')
        else:
            return ResponseStatus(status=True, message='')


def checking_access_rights_to_order(order, user) -> ResponseStatus:
        exists_order_handler = ExistsOrderHandler()
        access_rights_order_handler = AccessRightsOrderHandler()
        status_does_not_exist_handler = StatusDoesNotExistHandler()

        exists_order_handler.set_next(access_rights_order_handler).set_next(status_does_not_exist_handler)
        return exists_order_handler.handle(order, user)
