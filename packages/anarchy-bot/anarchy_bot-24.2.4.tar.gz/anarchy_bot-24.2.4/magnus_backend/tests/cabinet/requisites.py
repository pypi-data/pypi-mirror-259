from tests.common import Test


def check_create_props(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": self.email,
            "password": self.password,
        },
    )
    jwt = response.json().get("access_token")
    self.client.headers.update({"Authorization": f"Bearer {jwt}"})

    response = self.client.get("/api/cabinet/user/get_me")
    organization_id = response.json().get("organization_id")

    url = "/api/requisites/user/add-props"

    request_data = {"data": "Props data", "organization_id": organization_id}

    response = self.client.post(
        url,
        json=request_data,
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_update_props(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": self.email,
            "password": self.password,
        },
    )
    jwt = response.json().get("access_token")
    self.client.headers.update({"Authorization": f"Bearer {jwt}"})

    response = self.client.get("/api/cabinet/user/get_me")
    organization_id = response.json().get("organization_id")

    url = "/api/requisites/user/update-props"

    request_data = {
        "id": 1,
        "data": "Props data update",
        "organization_id": organization_id,
    }

    response = self.client.post(
        url,
        json=request_data,
    )
    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_delete_props(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": self.email,
            "password": self.password,
        },
    )
    jwt = response.json().get("access_token")
    self.client.headers.update({"Authorization": f"Bearer {jwt}"})

    url = "/api/requisites/user/delete-props"

    request_data = {"id": 1}

    response = self.client.post(
        url,
        json=request_data,
    )
    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)
