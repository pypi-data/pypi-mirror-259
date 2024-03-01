import src.setup
from tests.common import Test


def check_select_category(self: Test):
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

    response = self.client.get("/api/cabinet/user/categories")

    url = "/api/categories/categories/select-category"
    response = self.client.post(
        url,
        json={"category_id": response.json()[0].get("id"), "type": "trade"},
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_select_categories(self: Test):
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

    url = "/api/categories/categories/select-categories"

    response = self.client.get(url)

    assert response.status_code == 200
    assert len(response.json()) > 0
    self.log_passed(url)


def check_del_selected_category(self: Test):
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

    url = "/api/categories/categories/del-selected-category"

    response = self.client.post(
        url,
        json={
            "id": 1,
        },
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)
