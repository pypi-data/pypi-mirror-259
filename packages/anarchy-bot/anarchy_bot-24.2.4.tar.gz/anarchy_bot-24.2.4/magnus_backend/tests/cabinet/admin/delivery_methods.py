from tests.common import Test


def check_create_delivery_company(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": self.email,
            "password": self.password,
        },
    )
    access_token = response.json().get("access_token")
    self.client.headers.update({"Authorization": f"Bearer {access_token}"})

    url = "/api/cabinet/admin/add-delivery-company"
    response = self.client.post(
        url,
        json={"title": "Cdek", "slug": "cdek"},
    )
    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_delete_delivery_company(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": self.email,
            "password": self.password,
        },
    )
    access_token = response.json().get("access_token")
    self.client.headers.update({"Authorization": f"Bearer {access_token}"})

    url = "/api/cabinet/admin/del-delivery-company"
    response = self.client.post(url, json={"id": 1})

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)
