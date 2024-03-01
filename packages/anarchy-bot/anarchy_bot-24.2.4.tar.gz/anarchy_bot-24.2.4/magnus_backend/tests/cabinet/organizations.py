import src.setup
from tests.common import Test


def check_add_delivery_service(self: Test):
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

    url = "/api/cabinet/user/available-transport-companies"
    response = self.client.get(url)
    delivery_company_id = response.json()[0]["id"]

    url = "/api/organization/organizations/add-delivery-service"
    response = self.client.post(
        url,
        json={
            "delivery_company_id": delivery_company_id,
            "organization_id": organization_id,
        },
    )
    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_get_delivery_services(self: Test):
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

    url = f"/api/organization/organizations/delivery-services?organization_id={organization_id}"
    response = self.client.get(url)
    assert response.status_code == 200
    assert len(response.json()) > 0
    self.log_passed(url)


def check_del_delivery_service(self: Test):
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

    url = f"/api/organization/organizations/delivery-services?organization_id={organization_id}"
    response = self.client.get(url)
    delivery_service_id = response.json()[0]["id"]

    url = "/api/organization/organizations/del-delivery-service"
    response = self.client.post(
        url,
        json={"id": delivery_service_id},
    )
    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)
