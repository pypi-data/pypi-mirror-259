from tests.common import Test


def check_create_category(self: Test):
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
    expected_result = {'title': 'New', 'master_id': None, 'id': 1}
    url = '/api/cabinet/admin/add_category'
    response = self.client.post(
        url,
        json={'title': expected_result.get('title')},
    )
    assert response.status_code == 200
    assert response.json() == expected_result
    self.log_passed(url)


def check_update_category(self: Test):
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
    expected_result = {'title': 'Updated', 'master_id': None, 'id': 1}
    url = '/api/cabinet/admin/update_category'
    response = self.client.post(
        url,
        json=expected_result,
    )
    assert response.status_code == 200
    assert response.json().get('status') is True
    self.log_passed(url)


def check_delete_category(self: Test):
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
    response = self.client.post('/api/cabinet/admin/del_category?category_id=1')
    assert response.status_code == 200
    assert response.json().get('status') is True
    self.log_passed('/api/cabinet/admin/del_category')

