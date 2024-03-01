from tests.common import Test


def check_add_warehouse(self: Test):
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
    organization_id = response.json().get("id")

    url = "/api/warehouses/warehouses/add-warehouse"
    response = self.client.post(
        url,
        json={
            "title": "string",
            "location": "string",
            "organization_id": organization_id,
        },
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_update_warehouse(self: Test):
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
    organization_id = response.json().get("id")

    url = "/api/warehouses/warehouses/update-warehouse"
    response = self.client.post(
        url,
        json={
            "id": 1,
            "title": "string",
            "location": "string",
            "organization_id": organization_id,
        },
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_warehouses(self: Test):
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

    url = "/api/warehouses/warehouses/warehouses"
    response = self.client.get(
        url,
    )

    assert response.status_code == 200
    assert len(response.json()) > 0
    self.log_passed(url)


def check_del_warehouse(self: Test):
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
    organization_id = response.json().get("id")

    url = "/api/warehouses/warehouses/del-warehouse"
    response = self.client.post(
        url,
        json={"id": 1, "organization_id": organization_id},
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_add_delivery_company_point(self: Test):
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

    self.client.post(
        'api/cabinet/admin/add-delivery-company',
        json={
              "title": "cdek",
              "slug": "cdek"
            }
        )

    url = "/api/cabinet/user/delivery_companies"
    response = self.client.get(
        url,
    )

    delivery_company_id = response.json()[0]["id"]

    url = "/api/warehouses/warehouses/warehouses"
    response = self.client.get(
        url,
    )
    warehouse_id = response.json()[0]["id"]

    url = "/api/warehouses/warehouses/add-delivery-company-point"
    response = self.client.post(
        url,
        json={
            "title": "Point",
            "identifier": "ind",
            "warehouse_id": warehouse_id,
            "delivery_company_id": delivery_company_id
        },
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_del_delivery_company_point(self: Test):
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

    url = "/api/warehouses/warehouses/del-delivery-company-point"
    response = self.client.post(
        url,
        json={
            "id": 1,
        },
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)
