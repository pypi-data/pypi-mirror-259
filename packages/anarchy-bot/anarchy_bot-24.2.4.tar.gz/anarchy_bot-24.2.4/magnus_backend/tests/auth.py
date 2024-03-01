from fastapi.testclient import TestClient
from tests.common import Test

from src.schemas.users import JwtResponse


user_agents = [
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
]


class AuthUrls:
    def __init__(self) -> None:
        self.check_url = '/auth/check'
        self.register_url = '/auth/register'
        self.refresh_token = '/auth/refresh'
        self.login_url = '/auth/login'
        self.logout_url = '/auth/logout'
        self.test_jwt_url = '/auth/test_jwt'
        self.session_list_url = '/auth/session/list'
        self.kill_target_session_url = '/auth/session/kill'
        self.kill_sessions_url = '/auth/session/kill/all'
        self.refresh_token_url = '/auth/refresh'


urls = AuthUrls()


class AuthTest(Test):
    def __init__(self, client: TestClient) -> None:
        super().__init__(client)
        # self.email: str = 'test@example.com'
        self.register_data = {
            'email': self.email,
            'password': self.password,
        }
        self.login_error_message = {'detail': 'Invalid_email_or_password'}
        self.methods_to_test = [
            self.registration,
            self.already_registered,
            self.check_not_registered,
            self.check_registered,
            self.register_invalid_email,
            self.login_invalid_email,
            self.login_invalid_password,
            self.check_refresh_token_success,
            self.success_login,
            self.success_jwt_validation,
            self.try_validate_invalid_jwt,
            self.user_logout,
            self.check_refresh_token_after_logout,
            # self.ensure_logged_out,
            self.kill_target_session,
            self.kill_target_session_another_user,
            self.kill_all_sessions,
        ]

    def _registrarion_user(self, json_data=None):
        '''return response for registration user'''
        json_data = self.validate_json_data(json_data)
        response = self.client.post(
            urls.register_url,
            headers={'user-agent': user_agents[0]},
            json=json_data,
        )
        return response

    def _authorization_user(self, json_data=None, num_user_agent: int = 0):
        '''return response for auth user'''
        json_data = self.validate_json_data(json_data)
        user_agent = user_agents[num_user_agent]
        response = self.client.post(
            urls.login_url,
            headers={'user-agent': user_agent},
            json=json_data,
        )
        return response

    def _create_multiple_sessions(self, nums: int = len(user_agents)):
        '''create {nums} session for user (access and refresh tokens)'''
        self.list_access = []
        self.list_refresh = []
        for num in range(len(user_agents)):
            response = self._authorization_user(num_user_agent=num)
            self.list_access.append(response.json()['access_token'])
            self.list_refresh.append(response.json()['refresh_token'])

    def _delete_all_session(self, jwt):
        '''delete all jwt token for user'''
        response = self.client.post(
            urls.kill_sessions_url,
            headers={'Authorization': f'Bearer {jwt}'},
        )
        return response

    def _delete_target_session(self, jwt, token_key):
        '''delete target session except current'''
        response = self.client.post(
                urls.kill_target_session_url,
                headers={'Authorization': f'Bearer {jwt}'},
                params={'token_key': token_key}
            )
        return response

    def _logout_user(self, jwt):
        response = self.client.post(
            urls.logout_url,
            headers={'Authorization': f'Bearer {jwt}'},
        )
        return response

    def _test_jwt(self, jwt):
        response = self.client.get(
            urls.test_jwt_url,
            headers={'Authorization': f'Bearer {jwt}'},
        )
        return response

    def _refresh_tokens(self, refresh_token):
        response = self.client.post(
            urls.refresh_token_url,
            params={'refresh_token': refresh_token}
        )
        return response

    def _session_list(self, jwt):
        '''
        return [user_id_hash:device_hash, ...] (list[token_key])
        '''
        response = self.client.get(
            urls.session_list_url,
            headers={'Authorization': f'Bearer {jwt}'},
        )
        return response.json()

    def registration(self):
        '''user registration'''
        response = self._registrarion_user()
        assert response.status_code == 200
        tokens = JwtResponse(**response.json())
        self.access_token = tokens.access_token
        self.refresh_token = tokens.refresh_token
        self.log_passed(
            url=urls.register_url,
            doc=self.registration.__doc__,
        )

    def already_registered(self):
        '''user already registered'''
        response = self._registrarion_user()
        assert response.status_code == 400
        assert response.json() == {
            'detail': 'already_registered',
        }
        self.log_passed(
            url=urls.register_url,
            doc=self.already_registered.__doc__,
        )

    def check_not_registered(self):
        '''checking registration of not registered user'''
        self.not_existing_email = 'not_existing_email@example.com'
        response = self.client.post(
            urls.check_url,
            json={'email': self.not_existing_email},
        )
        assert response.status_code == 200
        assert response.json() == {'registered': False}
        self.log_passed(
            url=urls.check_url,
            doc=self.check_not_registered.__doc__,
        )

    def check_registered(self):
        '''check registrarion of registered user'''
        response = self.client.post(
            urls.check_url,
            json={'email': self.email},
        )
        assert response.status_code == 200
        assert response.json() == {'registered': True}
        self.log_passed(
            url=urls.check_url,
            doc=self.check_registered.__doc__,
        )

    def register_invalid_email(self):
        '''trying to register user with invalid email'''
        json_data = {'email': 'INCORRECT_EMAIL', 'password': self.password}
        response = self._registrarion_user(json_data)
        assert response.status_code == 422
        error_msg = response.json()['detail'][0]['msg']
        assert 'value is not a valid email address' in error_msg
        self.log_passed(
            url=urls.register_url,
            doc=self.register_invalid_email.__doc__,
        )

    def login_invalid_email(self):
        '''try to login with invalid email'''
        json_data = {'email': self.not_existing_email, 'password': self.password}
        response = self._authorization_user(json_data)
        assert response.status_code == 401
        assert response.json() == self.login_error_message
        self.log_passed(
            url=urls.login_url,
            doc=self.login_invalid_email.__doc__,
        )

    def login_invalid_password(self):
        '''try to login with invalid password'''
        json_data = {'email': self.email, 'password': 'ERROR'}
        response = self._authorization_user(json_data)
        assert response.status_code == 401
        assert response.json() == self.login_error_message
        self.log_passed(
            url=urls.login_url,
            doc=self.login_invalid_password.__doc__,
        )

    def check_refresh_token_success(self):
        '''user sends a request to update tokens'''
        response = self._refresh_tokens(self.refresh_token)
        assert response.status_code == 200
        tokens = JwtResponse(**response.json())
        self.access_token = tokens.access_token
        self.refresh_token = tokens.refresh_token
        self.log_passed(
            url=urls.refresh_token_url,
            doc=self.check_refresh_token_success.__doc__,
        )

    def success_login(self):
        '''successful login'''
        response = self._authorization_user()
        assert response.status_code == 200
        tokens = JwtResponse(**response.json())
        self.access_token = tokens.access_token
        self.refresh_token = tokens.refresh_token
        self.log_passed(
            url=urls.login_url,
            doc=self.success_login.__doc__
        )

    def success_jwt_validation(self):
        '''success jwt token validation'''
        response = self._test_jwt(self.access_token)
        assert response.status_code == 200
        self.log_passed(
            url=urls.test_jwt_url,
            doc=self.success_jwt_validation.__doc__,
        )

    def try_validate_invalid_jwt(self):
        '''try validate invalid jwt token'''
        invalid_jwt = 'invalid_token'
        response = self._test_jwt(invalid_jwt)
        assert response.status_code == 401
        assert response.json() == {'detail': 'token is invalid'}
        self.log_passed(
            url=urls.test_jwt_url,
            doc=self.try_validate_invalid_jwt.__doc__,
        )

    def user_logout(self):
        '''user logout'''
        response = self._logout_user(self.access_token)
        assert response.status_code == 200
        assert response.json() == {'message': 'logged out successfully'}

        self.log_passed(
            url=urls.logout_url,
            doc=self.user_logout.__doc__,
        )

    def check_refresh_token_after_logout(self):
        '''user sends a request to update tokens after a logout'''
        response = self._refresh_tokens(self.refresh_token)
        assert response.status_code == 400
        assert response.json() == {'detail': 'refresh token not found'}
        self.log_passed(
            url=urls.refresh_token_url,
            doc=self.check_refresh_token_after_logout.__doc__,
        )

    # def ensure_logged_out(self):
    #     '''ensure logged out by trying to validate killed jwt token'''
    #     response_after_logout = self._test_jwt(self.jwt)
    #     assert response_after_logout.status_code == 401
    #     assert response_after_logout.json() == {'detail': 'invalid_jwt'}
    #     self.log_passed(
    #         url=urls.test_jwt_url,
    #         doc=self.ensure_logged_out.__doc__,
    #     )

    def kill_target_session(self):
        ''' user kill target session'''
        i = 0
        self._create_multiple_sessions()
        session_list = self._session_list(self.list_access[0])
        assert len(session_list) == len(user_agents)
        for token_key in session_list:
            response = self._delete_target_session(self.list_access[0], token_key)
            if response.status_code == 200:
                i += 1
                session_list_after = self._session_list(self.list_access[0])
                assert len(session_list) - i == len(session_list_after)
            else:
                assert response.status_code == 400
                assert response.json() == {
                    'detail': 'current session cannot be terminated! use logout'
                }
        self.log_passed(
            url=urls.kill_target_session_url,
            doc=self.kill_target_session.__doc__,
        )

    def kill_target_session_another_user(self):
        '''user tries to kill another user's target session'''
        self._create_multiple_sessions()
        session_list = self._session_list(self.list_access[0])
        user_json = {'email': 'user_2@example.com', 'password': 'pswd'}
        response = self._registrarion_user(user_json)
        access_token = response.json()['access_token']
        response = self._delete_target_session(access_token, session_list[0])
        assert response.status_code == 400
        assert response.json() == {'detail': 'token is not owned by the session user'}
        self.log_passed(
            url=urls.kill_target_session_url,
            doc=self.kill_target_session_another_user.__doc__,
        )

    def kill_all_sessions(self):
        '''kill all user sessions except current'''
        self._create_multiple_sessions()
        session_list = self._session_list(self.list_access[0])
        assert len(session_list) == len(user_agents)
        response = self._delete_all_session(self.list_access[0])
        assert response.status_code == 200
        assert response.json() == {'message': 'sessions is terminated'}
        session_list = self._session_list(self.list_access[0])
        assert len(session_list) == 1
        self.log_passed(
            url=urls.kill_sessions_url,
            doc=self.kill_all_sessions.__doc__,
        )
