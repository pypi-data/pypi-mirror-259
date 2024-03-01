import string
from random import choice
from typing import Annotated, Dict, List

from fastapi import APIRouter, Depends, Request

from auth import get_current_active_user
from dao.orders import order_dao
from models.basket import ProductInBasket
from models.users import User
from schemas.basket import (
    CheckOutRequest,
    ProductInBasketData,
    ProductInBasketDelRequest,
    ProductInBasketRequest,
    ProductInBasketUpdateRequest,
)
from schemas.orders import OrderItemRequest, OrderRequest
from schemas.statuses import ResponseStatus

router = APIRouter(prefix="/basket")


@router.post("/add-to-basket")
async def add_to_basket(
    request_data: ProductInBasketRequest, user: User = Depends(get_current_active_user)
) -> ResponseStatus:
    product_in_basket = await ProductInBasket.get_or_none(
        product_id=request_data.product_id, user=user
    )

    if not product_in_basket:
        await ProductInBasket.create(
            product_id=request_data.product_id, user=user, count=request_data.count
        )
    else:
        product_in_basket.count = request_data.count
        await product_in_basket.save(update_fields=["count"])
    return ResponseStatus(status=True, message="Product added")


@router.get("/basket-items", dependencies=[Depends(get_current_active_user)])
async def basket_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> List[ProductInBasketData]:
    return [
        ProductInBasketData(
            id=item.id,
            product_id=item.product.id,
            title=item.product.title,
            count=item.count,
            img=item.product.img,
        )
        for item in await ProductInBasket.filter(user=current_user).prefetch_related(
            "product"
        )
    ]


@router.post("/update-to-basket")
async def update_to_basket(
    request_data: ProductInBasketUpdateRequest,
    user: User = Depends(get_current_active_user),
) -> ResponseStatus:
    product_in_basket = await ProductInBasket.get_or_none(id=request_data.id, user=user)

    if not product_in_basket:
        return ResponseStatus(status=False, message="Object not found")

    product_in_basket.count = request_data.count
    await product_in_basket.save(update_fields=["count"])
    return ResponseStatus(status=True, message="Object updated")


@router.post("/del-from-basket")
async def del_from_basket(
    request_data: ProductInBasketDelRequest,
    user: User = Depends(get_current_active_user),
) -> ResponseStatus:
    product_in_basket = await ProductInBasket.get_or_none(id=request_data.id, user=user)

    if not product_in_basket:
        return ResponseStatus(status=False, message="Object not found")

    await product_in_basket.delete()
    return ResponseStatus(status=True, message="Object deleted")


@router.post("/checkout")
async def checkout(
    request_data: CheckOutRequest,
    user: User = Depends(get_current_active_user),
) -> ResponseStatus:
    items = await ProductInBasket.filter(user=user).prefetch_related("product")

    check_data = [
        {
            "status": False if item.product.amount < item.count else True,
            "title": item.product.title,
            "count": item.product.amount,
        }
        for item in items
    ]

    if all([item["status"] for item in check_data]) is False:
        return ResponseStatus(
            status=False,
            message="There is no required quantity",
            payload={"check_data": check_data},
        )

    organizations = list(
        set([getattr(item.product, "organization_id") for item in items])
    )

    if len(organizations) == 1:
        order_data = OrderRequest(
            customer_id=user.id,
            organization_id=organizations[0],
            items=[
                OrderItemRequest(product_id=item.product.id, count=item.count)
                for item in items
            ],
            payment_method=request_data.payment_method,
            delivery_method=request_data.delivery_method,
        )
        await order_dao.create(order_data)
    else:
        data = {}
        for item in items:
            if data.get(item.product.id) is None:
                data.update({item.product.organization_id: [item]})
            else:
                data[item.product.organization_id].append(item)

        for k in data.keys():
            order_data = OrderRequest(
                customer_id=user.id,
                organization_id=k,
                items=[
                    OrderItemRequest(product_id=item.product.id, count=item.count)
                    for item in data.get(k, [])
                ],
                payment_method=request_data.payment_method,
                delivery_method=request_data.delivery_method,
            )
            await order_dao.create(order_data)

    await ProductInBasket.filter(user=user).delete()
    return ResponseStatus(status=True, message="Order created")
