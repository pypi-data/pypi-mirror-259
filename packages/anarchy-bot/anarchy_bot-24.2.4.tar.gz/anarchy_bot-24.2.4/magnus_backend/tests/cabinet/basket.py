import src.setup
from tests.common import Test


def check_add_to_basket(self: Test):
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

    request = self.client.get("/api/cabinet/user/get_me")

    organization_id = request.json().get("organization_id")
    producer_id = response.json().get("id")

    url = "/api/warehouses/warehouses/add-warehouse"
    self.client.post(
        url,
        json={
            "title": "string",
            "location": "string",
            "organization_id": organization_id,
        },
    )

    url = "/api/warehouses/warehouses/warehouses"
    response = self.client.get(
        url,
    )

    warehouse_id = response.json()[0]["id"]

    url = "/api/cabinet/admin/add_category"
    response = self.client.post(
        url,
        json={"title": "Cat"},
    )

    category_id = response.json().get("id")

    self.client.post(
        "/api/warehouses/warehouses/add-warehouse",
        json={
            "title": "string",
            "location": "string",
            "organization_id": organization_id,
        },
    )

    url = "/api/cabinet/user/add_product"
    self.client.post(
        url,
        json={
            "title": "New",
            "price": 100,
            "producer_id": producer_id,
            "description": "description",
            "category_id": category_id,
            "img": "img",
            "amount": 100,
            "organization_id": organization_id,
            "warehouse_id": warehouse_id,
            "weight": 1,
            "length": 1,
            "width": 1,
            "height": 1,
        },
    )

    url = "/api/cabinet/user/products"
    response = self.client.get(url)
    product_id = response.json()["items"][0]["id"]

    url = "/api/basket/basket/add-to-basket"

    response = self.client.post(
        url,
        json={
            "product_id": product_id,
            "count": 100,
        },
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_basket_items(self: Test):
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

    url = "/api/basket/basket/basket-items"

    response = self.client.get(url)

    assert response.status_code == 200
    assert len(response.json()) > 0
    self.log_passed(url)


def check_update_to_basket(self: Test):
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

    url = "/api/basket/basket/basket-items"

    response = self.client.get(url)

    url = "/api/basket/basket/update-to-basket"

    item_id = response.json()[0]["id"]

    response = self.client.post(
        url,
        json={"id": item_id, "count": 110},
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_del_from_basket(self: Test):
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

    url = "/api/basket/basket/basket-items"

    response = self.client.get(url)

    url = "/api/basket/basket/del-from-basket"

    item_id = response.json()[0]["id"]

    response = self.client.post(
        url,
        json={"id": item_id},
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_checkout(self: Test):
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
    product_id = response.json()["items"][0]["id"]

    url = "/api/basket/basket/add-to-basket"

    self.client.post(
        url,
        json={
            "product_id": product_id,
            "count": 100,
        },
    )

    url = "/api/basket/basket/checkout"

    response = self.client.post(
        url,
        json={
          "payment_method": "cashless",
          "delivery_method": "delivery"
        },
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)