from tests.common import Test


def check_create_notification(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": self.email,
            "password": self.password,
        },
    )
    jwt = response.json().get("access_token")
    self.client.headers.update({"Authorization": f"Bearer {jwt}"})

    url = "/api/cabinet/admin/add_notification"
    response = self.client.post(
        url,
        json={
            "subject": "Уведомление",
            "text": "ПРивет",
            "user_id": 2,
            "sender": "email",
        },
    )

    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)
