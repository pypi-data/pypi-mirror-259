from tests.common import Test


def check_create_employee(self: Test):
    response = self.client.post(
        "/auth/register",
        json={
            "password": "1qazxsw2",
            "email": "org@example.com",
            "firstname": "string",
            "lastname": "string",
            "inn": "string",
            "ogrn": "string",
            "org_name": "string",
            "org_legal_address": "string",
            "org_actual_address": "string",
            "phone_number": "string",
        },
    )
    access_token = response.json().get("access_token")

    self.client.headers.update({"Authorization": f"Bearer {access_token}"})

    request = self.client.get("/api/cabinet/user/get_me")

    data_request = {
        "user_id": request.json().get("id"),
        "organization_id": request.json().get("organization_id"),
        "role": "admin",
    }
    url = "/api/employees/user/add-employee"
    response = self.client.post(
        url,
        json=data_request,
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_employees(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": "org@example.com",
            "password": "1qazxsw2",
        },
    )
    access_token = response.json().get("access_token")

    self.client.headers.update({"Authorization": f"Bearer {access_token}"})

    request = self.client.get("/api/cabinet/user/get_me")

    url = f'/api/employees/user/employees?organization_id={request.json().get("organization_id")}'
    response = self.client.get(
        url,
    )

    assert response.status_code == 200
    assert len(response.json()) > 0
    self.log_passed(url)


def check_delete_employee(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": "org@example.com",
            "password": "1qazxsw2",
        },
    )
    access_token = response.json().get("access_token")

    self.client.headers.update({"Authorization": f"Bearer {access_token}"})

    request = self.client.get("/api/cabinet/user/get_me")

    data_request = {
        "user_id": request.json().get("id"),
        "organization_id": request.json().get("organization_id"),
        "role": "admin",
    }
    url = "/api/employees/user/del-employee"
    response = self.client.post(
        url,
        json=data_request,
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_on_board_employee(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": "org@example.com",
            "password": "1qazxsw2",
        },
    )
    access_token = response.json().get("access_token")

    self.client.headers.update({"Authorization": f"Bearer {access_token}"})

    request = self.client.get("/api/cabinet/user/get_me")

    data_request = {
        "email": "newemployee@example.com",
        "organization_id": request.json().get("organization_id"),
        "role": "admin",
    }

    url = "/api/employees/user/on-board-employee"
    response = self.client.post(
        url,
        json=data_request,
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)

    identifier = response.json().get("payload").get("identifier")

    url = f"/api/employees/user/make-on-board?identifier={identifier}"
    response = self.client.get(
        url,
    )
    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)
