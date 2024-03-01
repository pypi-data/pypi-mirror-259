from typing import Dict, List

from .base import Delivery


class PEC(Delivery):
    def __init__(self, *args) -> None:
        pass

    def authenticate(self) -> None:
        response = self.client.post(
            f"{self.base_url}oauth/token?parameters",
            data={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "client_credentials",
            },
        )
        self.access_token = f"Bearer {response.json().get('access_token')}"
        self.client.headers.update({"Authorization": self.access_token})

    def post_order(self, data: Dict) -> Dict:
        response = self.client.post(f"{self.base_url}orders", json=data)
        return response.json()

    def get_order_info(self, order_d: str) -> Dict:
        return {}

    def get_delivery_points(self, city_code: str) -> List[Dict]:
        return []

    def get_regions(self) -> List[Dict]:
        return []

    def get_cities(self, region_code: str) -> List[Dict]:
        return []

    def check_delivery_point(self, point_id: str) -> bool:
        return False


pec_worker = PEC()
