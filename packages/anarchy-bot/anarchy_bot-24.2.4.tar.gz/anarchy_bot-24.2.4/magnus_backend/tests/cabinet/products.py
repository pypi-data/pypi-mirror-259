import src.setup
from tests.common import Test


def check_add_product(self: Test):
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

    url = "/api/cabinet/user/get_me"
    response = self.client.get(url)
    producer_id = response.json().get("id")

    url = "/api/cabinet/admin/add_category"
    response = self.client.post(
        url,
        json={"title": "Cat"},
    )

    category_id = response.json().get("id")

    request = self.client.get("/api/cabinet/user/get_me")

    organization_id = request.json().get("organization_id")

    self.client.post("/api/warehouses/warehouses/add-warehouse",
                     json={
                         "title": "string",
                         "location": "string",
                         "organization_id": organization_id
                     })

    url = "/api/cabinet/user/add_product"
    response = self.client.post(
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
            "warehouse_id": 1,
            "weight": 1,
            "length": 1,
            "width": 1,
            "height": 1
        },
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_update_product(self: Test):
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

    url = "/api/cabinet/user/get_me"
    response = self.client.get(url)
    producer_id = response.json().get("id")

    url = "/api/cabinet/admin/add_category"
    response = self.client.post(
        url,
        json={"title": "Cat"},
    )

    category_id = response.json().get("id")

    request = self.client.get("/api/cabinet/user/get_me")

    organization_id = request.json().get("organization_id")

    url = "/api/cabinet/user/update_product"
    response = self.client.post(
        url,
        json={
            "title": "New updated",
            "price": "100.00",
            "id": 1,
            "producer_id": producer_id,
            "description": "description",
            "category_id": category_id,
            "img": "img",
            "amount": 100,
            "organization_id": organization_id,
            "warehouse_id": 1,
            "weight": 1,
            "length": 1,
            "width": 1,
            "height": 1
        },
    )
    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_get_products(self: Test):
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
    assert response.status_code == 200
    assert response.json().get("count") > 0
    self.log_passed(url)


def check_del_product(self: Test):
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

    url = f"/api/cabinet/user/del_product?product_id={1}"
    response = self.client.post(url)
    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url="/api/cabinet/user/del_product")


def check_create_product_structure(self: Test):
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
    url = "/api/cabinet/user/add-or-update-price-item-structure"
    response = self.client.post(
        url,
        json={
            "format": "json",
            "title": "data/product/title",
            "price": "data/product/price",
            "description": "description",
            "category": "category",
            "amount": "amount",
            "img": "img",
            "warehouse": "warehouse",
            "weight": "weight",
            "length": "length",
            "width": "width",
            "height": "height"
        },
    )
    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_upload_price(self: Test):
    products_json_path = src.setup.app_path / "tests/test_data/products.json"
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

    url = "/api/cabinet/admin/add_category"
    self.client.post(
        url,
        json={"title": "Candies"},
    )

    response = self.client.get("/api/cabinet/user/get_me")

    organization_id = response.json().get("organization_id")

    url = "/api/cabinet/user/upload-price?organization_id={}".format(organization_id)

    files = {"file": products_json_path.open("rb")}

    response = self.client.post(
        url,
        files=files,
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_add_update_delete_list_minimum_quantity_goods(self: Test):
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

    url = "/api/cabinet/user/add-or-update-minimum-quantity-goods"

    response = self.client.post(
        url,
        json={"organization_id": organization_id, "quantity": 10, "products": []},
    )

    assert response.status_code == 200
    assert response.json().get("status") is True

    url = "/api/cabinet/user/minimum-quantity-goods"
    response = self.client.get(
        url,
    )

    assert len(response.json()) == 1

    url = "/api/cabinet/user/add-or-update-minimum-quantity-goods"
    response = self.client.post(
        url,
        json={"organization_id": organization_id, "quantity": 10, "products": []}
    )
    assert response.status_code == 200
    assert response.json().get("status") is True

    url = "/api/cabinet/user/minimum-quantity-goods"
    response = self.client.get(
        url,
    )
    assert len(response.json()) == 1

    request = self.client.get("/api/cabinet/user/get_me")


    organization_id = request.json().get("organization_id")

    url = "/api/cabinet/user/delete-minimum-quantity-goods"
    response = self.client.post(url,
                                json={"organization_id": organization_id, "id": 1})
    assert response.status_code == 200
    assert response.json().get("status") is True

    url = "/api/cabinet/user/minimum-quantity-goods"
    response = self.client.get(
        url,
    )

    assert len(response.json()) == 0
    self.log_passed("/api/cabinet/user/add-or-update-minimum-quantity-goods")
    self.log_passed(url)
