from tests.common import Test


def check_create_payment_method(self: Test):
    response = self.client.post(
        '/auth/login',
        json={
            'email': self.email,
            'password': self.password,
        },
    )
    access_token = response.json().get('access_token')
    self.client.headers.update(
        {'Authorization': f'Bearer {access_token}'}
    )

    expected_result = {'id': 1, 'title': 'New', 'worker': 'cash', 'postpaid': True}
    url = '/api/cabinet/admin/add_payment_method'

    response = self.client.post(
        url,
        json={'title': expected_result.get('title'),
              'worker': expected_result.get('worker'),
              'postpaid': expected_result.get('postpaid')},
    )

    assert response.status_code == 200
    assert response.json().get("id") == expected_result.get("id")
    assert response.json().get("title") == expected_result.get("title")
    assert response.json().get("worker") == expected_result.get("worker")
    assert response.json().get("postpaid") == expected_result.get("postpaid")
    self.log_passed(url)


def check_update_payment_method(self: Test):
    response = self.client.post(
        '/auth/login',
        json={
            'email': self.email,
            'password': self.password,
        },
    )
    access_token = response.json().get('access_token')
    self.client.headers.update(
        {'Authorization': f'Bearer {access_token}'}
    )

    expected_result = {'id': 1, 'title': 'Updated', 'worker': 'cash', 'postpaid': True}

    url = '/api/cabinet/admin/update_payment_method'
    response = self.client.post(
        url,
        json=expected_result
    )

    assert response.status_code == 200
    assert response.json().get('status') is True
    self.log_passed(url)


def check_delete_payment_method(self: Test):
    response = self.client.post(
        '/auth/login',
        json={
            'email': self.email,
            'password': self.password,
        },
    )
    access_token = response.json().get('access_token')
    self.client.headers.update(
        {'Authorization': f'Bearer {access_token}'}
    )

    response = self.client.post(
        '/api/cabinet/admin/del_payment_method?payment_method_id=1'
    )

    assert response.status_code == 200
    assert response.json().get('status') is True
    self.log_passed('/api/cabinet/admin/del_payment_method')

