from tests.common import Test
from fastapi.testclient import TestClient

from src.schemas.users import JwtResponse

class AdminCabinetTest(Test):
    def __init__(self, client: TestClient) -> None:
        super().__init__(
            client = client,
        )
        self.email = 'admin@gmail.com'
        self.password = 'string'

    def register_admin(self):
        '''registering an admin, email should be set in config.admins_emails'''
        register_url = '/auth/register'
        register_data = self.validate_json_data({'email': 'admin@gmail.com', 'password': 'string'})
        response = self.client.post(
            register_url,
            json=register_data,
        )
        assert response.status_code == 200
        JwtResponse(**response.json())
        self.log_passed(
            url=register_url,
            doc=self.register_admin.__doc__,
        )
