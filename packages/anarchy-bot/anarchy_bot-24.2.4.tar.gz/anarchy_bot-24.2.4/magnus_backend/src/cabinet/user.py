from typing import Annotated, Dict, List

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from starlette.status import HTTP_403_FORBIDDEN

from auth import get_current_active_user, ph
from core.security import invalidate_all_user_refresh_tokens, make_confirmation_code
from dao.general import BaseDao, PaginationRequest
from dao.orders import OrderDao
from dao.products import ProductDao
from entities import content_types, format_json
from models.delivery import DeliveryCompany
from models.orders import Order, OrderItem
from models.organizations import Employee, Organization, check_user_in_organisation
from models.payments import PaymentMethod
from models.prices import PriceItemStructure
from models.products import (
    Category,
    MinimumQuantity,
    MinimumQuantityToProduct,
    OfferCategory,
    Product,
)
from models.users import ConfirmationCode, User
from models.warehouses import Warehouse
from payment_systems import payment_systems_items
from payment_systems.dummy import Dummy
from permissions import check_permission_to_organisation
from price_parsers.price_in_json import PriceInJson
from schemas.delivery import DeliveryCompanyData
from schemas.orders import (
    AdOrderItemRequest,
    CreatePaymentRequest,
    DelOrderItemRequest,
    OrderData,
    OrderItemData,
    OrderItemRequest,
    OrderOnlyStatus,
    OrderRequest,
    OrderUpdateData,
    PaymentCallbackRequest,
    PaymentMethodData,
)
from schemas.prices import PriceItemStructureRequest
from schemas.products import (
    CategoryData,
    CategoryRequest,
    DeleteMinimumQuantityGoodRequest,
    MinimumQuantityGoodRequest,
    ProductData,
    ProductRequest,
)
from schemas.categories import OfferCategoriesRequest,OfferCategoryData, OfferCategoryRequest
from schemas.statuses import ResponseStatus
from schemas.users import (
    ConfirmCodeModel,
    EmailUpdate,
    OrganizationForm,
    PasswordModel,
    PasswordUpdate,
    SetUsernameRequest,
    UserResponse,
)
from utils import send_mail

from .state import (
    STATUSES,
    Context,
    Direction,
    DummyState,
    checking_access_rights_to_order,
)

category_dao = BaseDao(Category)
payment_method_dao = BaseDao(PaymentMethod)
order_dao = OrderDao(Order)
product_dao = ProductDao(Product)
router = APIRouter(prefix="/user")


exc_update = HTTPException(status_code=401, detail="invalid password verification")


@router.get("/get_me")
async def get_me(user: User = Depends(get_current_active_user)) -> UserResponse:
    """
    return dict with id, email, username
    """
    organization = await Organization.get(users=user)
    result = user.info()
    result["organization_id"] = organization.id
    return UserResponse(**result)


@router.post('/update/organization')
async def update_or_create_organization(
    form_data: OrganizationForm,
    user: User = Depends(get_current_active_user)
):
    """create or update info of user organization"""
    if not all([v for _, v in form_data]):
        HTTPException(status_code=400, detail="incomplete data about the organization")
    org = await Organization.get_or_none(users=user)
    if org is None:
        data = form_data.model_dump()
        data['users'] = user
        await Organization.create(**data)
    else:
        await org.update_from_dict(form_data.model_dump())
        await org.save()
    return {"message": "successfull update data of orgamization"}


@router.post("/update_email")
async def update_email(
    form_data: EmailUpdate, user: User = Depends(get_current_active_user)
):
    """allows to update email with password verification"""
    try:
        ph.verify(user.password_hash, form_data.password.get_secret_value())
    except:
        raise exc_update
    await user.update_email(email=form_data.new_email)
    return {"message": "Successfull update user email"}


@router.post("/update_password")
async def update_password(
    form_data: PasswordUpdate, user: User = Depends(get_current_active_user)
):
    """allows to update password with old password verification"""
    try:
        ph.verify(user.password_hash, form_data.password.get_secret_value())
    except:
        raise exc_update
    password_hash = ph.hash(form_data.new_password.get_secret_value())
    await user.update_password(password_hash=password_hash)
    return {"message": "successfull update user password"}


@router.post("/set_username")
async def set_username(
    request: SetUsernameRequest, user: User = Depends(get_current_active_user)
) -> dict:
    """
    allows to set username

    english letthers, numbers, and underscores only
    """
    await user.update_username(username=request.username)
    return {"message": "succesfull set username"}


@router.post("/delete_account")
async def delete_account(
    form_data: PasswordModel, user: User = Depends(get_current_active_user)
):
    """delete account and kill all refresh tokens"""
    try:
        ph.verify(user.password_hash, form_data.password.get_secret_value())
    except:
        raise exc_update
    await make_confirmation_code(user.email)
    return {"message": "We have sent you a confirmation code by email"}


@router.post("/delete_account_confirm")
async def delete_account_confirm(
    form_data: ConfirmCodeModel, user: User = Depends(get_current_active_user)
):
    """Confirm delete account, user devices and kill all jwt"""

    confirm_code = await ConfirmationCode.filter(
        code=form_data.code.get_secret_value(), confirmed=False
    ).first()

    if confirm_code is None:
        return {"message": "Invalid code"}

    await confirm_code.update_from_dict({"confirmed": True}).save()
    await invalidate_all_user_refresh_tokens(user)
    await user.delete()
    return {"message": "successfull delete user account"}


@router.get(
    "/categories",
)
async def categories(
    params: PaginationRequest = Depends(PaginationRequest),
) -> List[CategoryData]:
    return [
        CategoryData(id=c.id, title=c.title, master_id=c.master_id)
        for c in (await category_dao.list(params)).get("items", [])
    ]


@router.get(
    "/payment_methods",
)
async def payment_methods(
    params: PaginationRequest = Depends(PaginationRequest),
) -> List[PaymentMethodData]:
    return [
        PaymentMethodData(
            id=i.id,
            title=i.title,
            worker=i.worker,
            postpaid=i.postpaid,
            identifier=i.identifier,
        )
        for i in (await payment_method_dao.list(params)).get("items", [])
    ]


@router.get(
    "/delivery_companies",
)
async def delivery_methods(
    params: PaginationRequest = Depends(PaginationRequest),
) -> List[DeliveryCompanyData]:
    return [
        DeliveryCompanyData(id=i.id, title=i.title, slug=i.slug)
        for i in (await DeliveryCompany.all())
    ]


@router.post("/add_product", dependencies=[Depends(get_current_active_user)])
async def add_product(
    prod: ProductRequest,
    current_user: Annotated[User, Depends(get_current_active_user)],
    check_permission: bool = Depends(check_permission_to_organisation),
) -> ResponseStatus:

    prod.producer_id = current_user.id
    warehouse = await Warehouse.filter(id=prod.warehouse_id).prefetch_related("organization").first()

    if not warehouse or warehouse.organization.id != prod.organization_id:
        return ResponseStatus(status=False, message="Warehouse not found")
    await product_dao.create(prod)
    return ResponseStatus(status=True, message="Products added")


@router.get("/products")
async def products(args: PaginationRequest = Depends(PaginationRequest)) -> Dict:
    query_rows = await product_dao.list(args)

    return {
        "count": query_rows.get("count"),
        "items": [
            ProductData(
                id=i.id,
                title=i.title,
                price=i.price,
                producer_id=i.producer_id,
                description=i.description,
                category_id=i.category_id,
                img=i.img,
                amount=i.amount,
                organization_id=i.organization_id,
                warehouse_id=i.warehouse_id,
                weight=i.weight,
                length=i.length,
                width=i.width,
                height=i.height
            )
            for i in query_rows.get("items", [])
        ],
    }


@router.post("/del_product")
async def del_product(
    product_id: int,
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> ResponseStatus:
    product = await product_dao.get(product_id)
    if product is None:
        return ResponseStatus(status=False, message="Product not found")

    organisation = await Organization.get(id=product.organization_id)
    is_in_organisation = await check_user_in_organisation(current_user.id, organisation)
    if is_in_organisation is True:
        await product_dao.delete(product_id)
        return ResponseStatus(status=True, message="Product deleted")
    return ResponseStatus(status=False, message="Delete error")


@router.post("/update_product", dependencies=[Depends(get_current_active_user)])
async def update_product(
    data: ProductData,
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> ResponseStatus:
    product = await product_dao.get(data.id)
    if product is None:
        return ResponseStatus(status=False, message="Product not found")

    warehouse = await Warehouse.filter(id=data.warehouse_id).prefetch_related("organization").first()
    if not warehouse or warehouse.organization.id != data.organization_id:
        return ResponseStatus(status=False, message="Warehouse not found")
    producer = await product.producer
    data.producer_id = producer.id
    organisation = await Organization.get(id=product.organization_id)
    is_in_organisation = await check_user_in_organisation(current_user.id, organisation)
    if is_in_organisation is True:
        await product_dao.update(data)
        return ResponseStatus(status=True, message="Product updated")
    return ResponseStatus(status=False, message="Update error")


@router.post(
    "/create_order",
    dependencies=[Depends(get_current_active_user)],
)
async def create_order(
    current_user: Annotated[User, Depends(get_current_active_user)],
    request_data: OrderRequest,
) -> ResponseStatus:
    request_data.customer_id = current_user.id

    products = await Product.filter(id__in=[i.product_id for i in request_data.items]).prefetch_related("organization")
    organizations = list(
        set([getattr(product, "organization_id") for product in products])
    )
    if len(organizations) == 1:
        request_data.organization_id = organizations[0]
        await order_dao.create(request_data)
    else:
        data = {}
        for item in products:
            if data.get(item.organization.id) is None:
                data.update({item.organization.id: [item]})
            else:
                data[item.organization.id].append(item)

        for k in data.keys():
            order_data = OrderRequest(
                customer_id=current_user.id,
                organization_id=k,
                items=[
                    OrderItemRequest(product_id=item.product.id, count=item.count)
                    for item in data.get(k, [])
                ],
                payment_method=request_data.payment_method,
                delivery_method=request_data.delivery_method,
            )
            await order_dao.create(order_data)

    return ResponseStatus(status=True, message="Order was create")


@router.post(
    "/change_order_status",
    dependencies=[Depends(get_current_active_user)],
)
async def change_order_status(
    current_user: Annotated[User, Depends(get_current_active_user)],
    order_id: int,
    direction: Direction,
) -> ResponseStatus:
    order = await order_dao.get(order_id)
    response: ResponseStatus = checking_access_rights_to_order(order, current_user)
    if response.status is False:
        return response

    status = STATUSES.get(order.status, DummyState)
    context = Context(status(order, current_user))
    if direction.value == Direction.positive:
        await context.positive()
    else:
        await context.negative()
    return ResponseStatus(status=True, message="Order status changed")


@router.post(
    "/update_order",
    dependencies=[Depends(get_current_active_user)],
)
async def update_order(
    current_user: Annotated[User, Depends(get_current_active_user)],
    order_data: OrderUpdateData,
) -> ResponseStatus:
    order = await order_dao.get(order_data.id)
    response: ResponseStatus = checking_access_rights_to_order(order, current_user)
    if response.status is False:
        return response

    await order_dao.update(order_data)
    return ResponseStatus(status=True, message="The order has been updated")


@router.post(
    "/order_add_item",
    dependencies=[Depends(get_current_active_user)],
)
async def order_add_item(
    current_user: Annotated[User, Depends(get_current_active_user)],
    order_item_data: AdOrderItemRequest,
) -> ResponseStatus:
    order = await order_dao.get(order_item_data.order_id)
    response: ResponseStatus = checking_access_rights_to_order(order, current_user)
    if response.status is False:
        return response

    await order_dao.add_item(order_item_data)
    return ResponseStatus(status=True, message="The order has been updated")


@router.post(
    "/order_del_item",
    dependencies=[Depends(get_current_active_user)],
)
async def order_del_item(
    current_user: Annotated[User, Depends(get_current_active_user)],
    order_item_data: DelOrderItemRequest,
) -> ResponseStatus:
    order = await order_dao.get(order_item_data.order_id)
    response: ResponseStatus = checking_access_rights_to_order(order, current_user)
    if response.status is False:
        return response

    result_delete: bool = await order_dao.delete_item(order_item_data.order_item_id)
    if result_delete:
        return ResponseStatus(status=True, message="The order has been updated")
    else:
        return ResponseStatus(status=False, message="Del order item error")


@router.get("/orders")
async def orders(
    current_user: Annotated[User, Depends(get_current_active_user)],
    args: PaginationRequest = Depends(PaginationRequest),
):
    args.field.append("customer_id")
    args.value.append(current_user.id)
    args.op.append("=")
    args.field.append("provider_id")
    args.value.append(current_user.id)
    args.op.append("=")
    args.gate = "or"
    query_rows = await order_dao.list(args)

    return {
        "count": query_rows.get("count"),
        "items": [
            OrderData(
                id=order.id,
                status=order.status,
                customer_id=order.customer_id,
                provider_id=order.provider_id,
                delivery_method=order.delivery_method,
                payment_method=order.payment_method,
                items=[
                    OrderItemData(
                        id=item.id, product_id=item.product_id, count=item.count
                    )
                    for item in (await order_dao.order_items(order.id))
                ],
            )
            for order in query_rows.get("items", [])
        ],
    }


@router.post(
    "/create_payment",
    dependencies=[Depends(get_current_active_user)],
)
async def create_payment(
    current_user: Annotated[User, Depends(get_current_active_user)],
    create_payment_request: CreatePaymentRequest,
) -> ResponseStatus:
    order = await order_dao.get(create_payment_request.order_id)
    response: ResponseStatus = checking_access_rights_to_order(order, current_user)

    if order is None:
        return ResponseStatus(status=False, message="Order not found")
    if response.status is True:
        payment_method = await order.payment_method
        payment_method_worker = payment_method.worker
        payment_system_class = payment_systems_items.get(payment_method_worker, Dummy)
        payment_system_obj = payment_system_class(params={"order_id": order.id})
        message = await payment_system_obj.create_payment()
        return ResponseStatus(status=True, message=message)
    return ResponseStatus(status=False, message="Access error")


@router.post(
    "/payment_callback/{item_id}",
)
async def payment_callback(item_id: str, data: Dict) -> ResponseStatus:
    payment_method = await PaymentMethod.filter(identifier=item_id).first()

    if payment_method is None:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid id")
    payment_system_class = payment_systems_items.get(payment_method.worker, Dummy)
    payment_system = payment_system_class(data)
    status = await payment_system.payment_verification()
    return ResponseStatus(status=status, message="Result")


@router.post(
    "/add-or-update-price-item-structure",
    dependencies=[Depends(get_current_active_user)],
)
async def add_or_update_price_item_structure(
    current_user: Annotated[User, Depends(get_current_active_user)],
    ps_request: PriceItemStructureRequest,
) -> ResponseStatus:
    price_item_structure = await PriceItemStructure.filter(
        user=current_user, format=ps_request.format.value
    ).first()

    if price_item_structure is None:

        data = ps_request.model_dump()
        data.update({"user": current_user})
        await PriceItemStructure.create(**data)
        return ResponseStatus(status=True, message="Structure added")
    else:
        data = ps_request.model_dump()
        data.update({"user": current_user})
        await price_item_structure.update_from_dict(data).save()

        return ResponseStatus(status=True, message="Structure updated")


@router.post(
    "/upload-price",
    dependencies=[Depends(get_current_active_user)],
)
async def upload_price(
    current_user: Annotated[User, Depends(get_current_active_user)],
    file: UploadFile,
    organization_id: int,
) -> ResponseStatus:
    content_type = (
        "application/json" if file.content_type is None else file.content_type
    )
    price_format = content_types.get(content_type)
    price_item_structure = await PriceItemStructure.filter(
        user=current_user, format=price_format
    ).first()
    if price_item_structure is None:
        return ResponseStatus(
            status=False, message="You need to add a description of the price structure"
        )
    price_in = PriceInJson(
        file.file.read().decode("utf-8"),
        current_user,
        organization_id,
        price_item_structure,
    )

    clean_data = await price_in.get_clean_data()

    for i in clean_data:
        await product_dao.create(ProductRequest(**i))
    return ResponseStatus(status=True, message="Products added")


@router.post(
    "/add-or-update-minimum-quantity-goods",
    dependencies=[Depends(get_current_active_user)],
)
async def add_or_update_minimum_quantity_goods(
    current_user: Annotated[User, Depends(get_current_active_user)],
    check_permission: Annotated[bool, Depends(check_permission_to_organisation)],
    request_data: MinimumQuantityGoodRequest,
) -> ResponseStatus:
    obj, status = await MinimumQuantity.get_or_create(
        organization_id=request_data.organization_id, quantity=request_data.quantity
    )
    if status is False:
        await obj.update_from_dict({"quantity": request_data.quantity}).save()

    if len(request_data.products):
        minimum_quantity_products = await MinimumQuantityToProduct.filter(
            minimum_quantity=obj
        ).prefetch_related("product")

        # product_ids = request_data.products + [i.product.id for i in minimum_quantity_products]

        for i in minimum_quantity_products:
            if i.product.id not in request_data.products:
                await i.delete()

        for i in request_data.products:
            await MinimumQuantityToProduct.get_or_create(
                product_id=i, minimum_quantity=obj
            )

    return ResponseStatus(status=True, message="Successfully")


@router.get(
    "/minimum-quantity-goods",
    dependencies=[Depends(get_current_active_user)],
)
async def minimum_quantity_goods(
    current_user: Annotated[User, Depends(get_current_active_user)]
) -> List[MinimumQuantityGoodRequest]:
    employees = await Employee.filter(user=current_user).prefetch_related(
        "organization"
    )

    organization_ids = [emp.organization.id for emp in employees]

    organization = await Organization.filter(users=current_user).first()

    if organization is not None:
        organization_ids.append(organization.id)

    return [
        MinimumQuantityGoodRequest(
            quantity=i.quantity, organization_id=i.organization.id, products=[]
        )
        for i in await MinimumQuantity.filter(
            organization_id__in=organization_ids
        ).prefetch_related("organization")
    ]


@router.post(
    "/delete-minimum-quantity-goods",
    dependencies=[Depends(get_current_active_user)],
)
async def delete_minimum_quantity_goods(
    current_user: Annotated[User, Depends(get_current_active_user)],
    check_permission: Annotated[bool, Depends(check_permission_to_organisation)],
    request_data: DeleteMinimumQuantityGoodRequest,
) -> ResponseStatus:
    minimum_quantity_good = await MinimumQuantity.get_or_none(
        organization_id=request_data.organization_id, id=request_data.id
    )
    if minimum_quantity_good is not None:
        await minimum_quantity_good.delete()
    return ResponseStatus(status=True, message="Successfully")
