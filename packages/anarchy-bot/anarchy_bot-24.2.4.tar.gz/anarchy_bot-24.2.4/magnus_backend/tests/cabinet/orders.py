from decimal import Decimal

from dao.general import BaseDao
from models.organizations import Organization
from models.payments import PaymentMethod
from models.products import Category, Product
from models.users import User
from models.warehouses import Warehouse
from schemas.orders import PaymentMethodRequest
from schemas.products import CategoryRequest, ProductRequest
from tests.common import Test

product_dao = BaseDao(Product)
category_dao = BaseDao(Category)
payment_dao = BaseDao(PaymentMethod)


async def init_order_data():
    category = await category_dao.create(CategoryRequest(title="title"))
    await payment_dao.create(
        PaymentMethodRequest(title="yoo_money", worker="yoo_money", postpaid=False)
    )
    await payment_dao.create(
        PaymentMethodRequest(title="cash", worker="cash", postpaid=True)
    )
    new_user = await User.create(
        email="user@gmail.com",
        password_hash="password_hash",
        is_admin=False,
    )
    organization = await Organization.all().first()
    organization_id = 1 if not organization else organization.id
    warehouse = await Warehouse.create(title="Supper Warehouse", organization=organization, location="Here")

    await product_dao.create(
        ProductRequest(
            title="title",
            price=Decimal("100"),
            description="description",
            category_id=category.id,
            img="img",
            producer_id=new_user.id,
            amount=14,
            organization_id=organization_id,
            warehouse_id=warehouse.id,
            weight=1,
            length=1,
            width=1,
            height=1
        )
    )
    await product_dao.create(
        ProductRequest(
            title="title 2",
            price=Decimal("100"),
            description="description",
            category_id=category.id,
            img="img",
            producer_id=new_user.id,
            amount=24,
            organization_id=organization_id,
            warehouse_id=warehouse.id,
            weight=1,
            length=1,
            width=1,
            height=1
        )
    )


def check_create_order(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": self.email,
            "password": self.password,
        },
    )

    self.client.headers.update(
        {"Authorization": f'Bearer {response.json().get("access_token")}'}
    )

    url = "/api/cabinet/user/products"
    response = self.client.get(url)

    product_id = response.json().get("items")[0].get("id")

    url = "/api/cabinet/user/payment_methods"
    response = self.client.get(url)
    payment_method_id = response.json()[0].get("id")

    order_data = {
        "customer_id": 1,
        "organization_id": 0,
        "items": [{"product_id": product_id, "count": 10}],
        "delivery_method": "delivery",
        "payment_method": "cash",
    }

    url = "/api/cabinet/user/create_order"
    response = self.client.post(
        url,
        json=order_data,
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_change_order_status(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": self.email,
            "password": self.password,
        },
    )

    self.client.headers.update(
        {"Authorization": f'Bearer {response.json().get("access_token")}'}
    )

    url = f"/api/cabinet/user/change_order_status?order_id=1&direction=positive"
    response = self.client.post(
        url,
    )
    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url=f"/api/cabinet/user/change_order_status")


def check_update_order(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": self.email,
            "password": self.password,
        },
    )

    self.client.headers.update(
        {"Authorization": f'Bearer {response.json().get("access_token")}'}
    )

    url = "/api/cabinet/user/update_order"
    response = self.client.post(
        url,
        json={"id": 1, "delivery_method": "delivery", "payment_method": "cash"},
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_order_add_item(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": self.email,
            "password": self.password,
        },
    )

    self.client.headers.update(
        {"Authorization": f'Bearer {response.json().get("access_token")}'}
    )

    url = "/api/cabinet/user/products?limit=25&offset=0&op=%3D&sort_order=desc&gate=and"
    response = self.client.get(url)

    product_id = response.json().get("items")[-1].get("id")
    url = "/api/cabinet/user/order_add_item"
    response = self.client.post(url, json={"order_id": 1, "product_id": product_id, "count": 10})
    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_order_del_item(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": self.email,
            "password": self.password,
        },
    )

    self.client.headers.update(
        {"Authorization": f'Bearer {response.json().get("access_token")}'}
    )

    url = "/api/cabinet/user/order_del_item"
    response = self.client.post(url, json={"order_id": 1, "order_item_id": 2})
    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)
