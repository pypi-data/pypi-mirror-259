from tests.common import Test


def check_get_users(self: Test):
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
    url = '/api/cabinet/admin/users'
    response = self.client.get(
        url,
    )
    assert response.status_code == 200
    assert response.json()[0].get('email') == 'example@email.com'
    self.log_passed(url)


def check_del_user(self: Test):
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

    response = self.client.get(
        '/api/cabinet/admin/users',
    )
    users = response.json()
    id = users[0].get('id')
    response = self.client.post(
        f'/api/cabinet/admin/del_user?user_id={id}',
    )
    assert response.status_code == 200
    assert response.json() is True
    self.log_passed('/api/cabinet/admin/del_user')


def check_lock_user(self: Test):
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

    response = self.client.get(
        '/api/cabinet/admin/users',
    )
    users = response.json()

    url = '/api/cabinet/admin/block_user'
    response = self.client.post(
        url,
        json={'user_id': users[0].get('id'), 'days': 1},
    )
    assert response.status_code == 200
    assert response.json() is True
    self.log_passed(url)
