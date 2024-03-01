from fastapi.testclient import TestClient
from tests.common import Test
from tests.auth import user_agents, urls


class UserCabinetTest(Test):
    def __init__(
        self,
        client: TestClient,
    ) -> None:
        super().__init__(client)
        self.email = 'test@example.com'
        self.methods_to_test = [
            self.registration,
            self.get_categories,
            self.set_username,
            self.get_me,
            self.test_update_email,
            self.test_update_password,
            self.delete_user_account,
        ]

    def registration(self):
        '''user registration'''
        self.register_data = self.validate_json_data({'email': self.email, 'password': self.password})
        response = self.client.post(
            urls.register_url,
            headers={'user-agent': user_agents[0]},
            json=self.register_data,
        )
        assert response.status_code == 200
        self.access_token = response.json()['access_token']
        self.refresh_token = response.json()['refresh_token']
        self.log_passed(url=urls.register_url, doc=self.registration.__doc__)

    def get_categories(self):
        '''user sent a request for categories'''
        url = '/api/cabinet/user/categories'
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.json() == []
        self.log_passed(url=url, doc=self.get_categories.__doc__)

    def set_username(self):
        '''user sent a name change request'''
        url = '/api/cabinet/user/set_username'
        response = self.client.post(
            url,
            json={'username': 'test_username'},
            headers={'Authorization': f'Bearer {self.access_token}'},
        )
        assert response.status_code == 200
        self.log_passed(url=url, doc=self.set_username.__doc__)

    def get_me(self):
        '''the user has sent a request for personal information '''
        url = '/api/cabinet/user/get_me'
        response = self.client.get(
            url,
            headers={'Authorization': f'Bearer {self.access_token}'},
        )
        assert response.status_code == 200
        user = response.json()
        assert isinstance(user, dict)
        self.log_passed(url=url, doc=self.get_me.__doc__)

    def test_update_email(self):
        '''test for updating user email'''

        update_email_url = '/api/cabinet/user/update_email'
        password = 'password'

        # Registration
        old_json_data = {'email': 'test_email_1@example.com', 'password': password}
        reg_json_data = self.validate_json_data(old_json_data)
        new_json_data = {'email': 'test_email_2@example.com', 'password': password}

        # Registration session
        response = self.client.post(
            url='/auth/register',
            headers={'user-agent': user_agents[0]},
            json=reg_json_data
        )
        assert response.status_code == 200

        # Auth with old email
        response = self.client.post(
            url='/auth/login',
            headers={'user-agent': user_agents[0]},
            json=old_json_data
        )
        assert response.status_code == 200
        access_token = response.json()['access_token']

        # Update user email
        response = self.client.post(
            url=update_email_url,
            headers={'Authorization': f'Bearer {access_token}'},
            json={'new_email': 'test_email_2@example.com', 'password': password}
        )
        assert response.status_code == 200

        # Auth with new email
        response = self.client.post(
            url='/auth/login',
            headers={'user-agent': user_agents[0]},
            json=new_json_data
        )
        assert response.status_code == 200

        # Auth with old email
        response = self.client.post(
            url='/auth/login',
            headers={'user-agent': user_agents[0]},
            json=old_json_data
        )
        assert response.status_code == 401

        # Update user email with incorrect email
        response = self.client.post(
            url=update_email_url,
            headers={'Authorization': f'Bearer {access_token}'},
            json={'email': 'test_email_3'}
        )
        assert response.status_code == 422

        self.log_passed(update_email_url, doc=self.test_update_email.__doc__)

    def test_update_password(self):
        '''test for updating user password'''

        update_pswd_url = '/api/cabinet/user/update_password'

        # Registration
        old_json_data = {'email': 'example@example.com', 'password': 'test_1'}
        reg_json_data = self.validate_json_data(old_json_data)
        new_json_data = {'email': 'example@example.com', 'password': 'test_2'}
        confirm_code_data = {'code': '111111'}

        # Registration session
        response = self.client.post(
            url='/auth/register',
            headers={'user-agent': user_agents[0]},
            json=reg_json_data
        )
        assert response.status_code == 200

        # Auth with old password
        response = self.client.post(
            url='/auth/login',
            headers={'user-agent': user_agents[0]},
            json=old_json_data
        )
        assert response.status_code == 200
        access_token = response.json()['access_token']

        # Update user password
        response = self.client.post(
            url=update_pswd_url,
            headers={'Authorization': f'Bearer {access_token}'},
            json={'password': 'test_1', 'new_password': 'test_2'}
        )
        assert response.status_code == 200

        # Auth with old password
        response = self.client.post(
            url='/auth/login',
            headers={'user-agent': user_agents[0]},
            json=old_json_data
        )
        assert response.status_code == 401

        # Auth with new password
        response = self.client.post(
            url='/auth/login',
            headers={'user-agent': user_agents[0]},
            json=new_json_data
        )
        assert response.status_code == 200

        # Update user password with incorrect password
        response = self.client.post(
            url=update_pswd_url,
            headers={'Authorization': f'Bearer {access_token}'},
            json={'password': ''}
        )
        assert response.status_code == 422

        # Auth with confirm code
        response = self.client.post(
            url='/auth/f2a-login',
            headers={'user-agent': user_agents[0]},
            json=confirm_code_data
        )
        assert response.status_code == 200

        self.log_passed(update_pswd_url, doc=self.test_update_password.__doc__)

    def delete_user_account(self):
        '''delete user account and all user refresh tokens'''

        account_delete_url = '/api/cabinet/user/delete_account'
        account_delete_confirm_url = "/api/cabinet/user/delete_account_confirm"
        check_email_url = '/auth/check'
        test_jwt_url = '/auth/test_jwt'
        email = 'test_email@example.com'

        json_data = {'email': email, 'password': 'password'}
        reg_json_data = self.validate_json_data(json_data)
        json_del = {'password': 'password'}
        json_del_confirm = {'code': '111111'}

        # Registration session
        response = self.client.post(
            url='/auth/register',
            headers={'user-agent': user_agents[0]},
            json=reg_json_data
        )
        assert response.status_code == 200
        access_token = response.json()['access_token']

        # Test before delete account
        user_registered = self.client.post(url=check_email_url, json={'email': email})
        assert user_registered.json() == {'registered': True}
        jwt_status = self.client.get(
            url=test_jwt_url,
            headers={'Authorization': f'Bearer {access_token}'},
        )
        assert jwt_status.status_code == 200

        # Delete user
        response = self.client.post(
            url=account_delete_url,
            headers={'Authorization': f'Bearer {access_token}'},
            json=json_del
        )
        assert response.status_code == 200

        response = self.client.post(
            url=account_delete_confirm_url,
            headers={'Authorization': f'Bearer {access_token}'},
            json=json_del_confirm
        )
        assert response.status_code == 200

        # Test after delete account
        user_registered = self.client.post(url=check_email_url, json={'email': email})

        assert user_registered.json() == {'registered': False}
        jwt_status = self.client.get(
            url=test_jwt_url,
            headers={'Authorization': f'Bearer {access_token}'},
        )
        assert jwt_status.status_code == 401

        # Get session list for user
        response = self.client.get(
            urls.session_list_url,
            headers={'Authorization': f'Bearer {access_token}'},
        )
        assert response.status_code == 401

        self.log_passed(
            account_delete_url,
            doc=self.delete_user_account.__doc__
        )


def check_offer_category(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": "org@example.com",
            "password": "1qazxsw2",
        },
    )
    access_token = response.json().get("access_token")

    self.client.headers.update({"Authorization": f"Bearer {access_token}"})

    url = "/api/categories/categories/offer-category"

    response = self.client.post(
        url=url,
        headers={'Authorization': f'Bearer {access_token}'},
        json={
              "title": "string",
              "explanation": "string"
            }
    )
    assert response.status_code == 200
    assert response.json().get("status") is True
    self.log_passed(url)


def check_offer_categories(self: Test):
    response = self.client.post(
        "/auth/login",
        json={
            "email": "org@example.com",
            "password": "1qazxsw2",
        },
    )
    access_token = response.json().get("access_token")

    self.client.headers.update({"Authorization": f"Bearer {access_token}"})

    url = "/api/categories/categories/offer-categories?status=all"

    response = self.client.get(
        url=url,
        headers={'Authorization': f'Bearer {access_token}'},
    )
    assert response.status_code == 200
    assert len(response.json()) > 0
    self.log_passed(url)
