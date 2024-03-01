from typing import Dict, List

from .base import Delivery, use_authenticate
import core.config as config


class CDEK(Delivery):
    tariffs: Dict[str, int] = {
        "warehouse_warehouse": 136,
        "warehouse_door": 137
    }

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

    @use_authenticate
    def post_order(self, data: Dict) -> Dict:
        response = self.client.post(f"{self.base_url}orders", json=data)
        return response.json()

    @use_authenticate
    def get_order_info(self, order_d: str) -> Dict:
        response = self.client.get(
            f"{self.base_url}orders/{order_d}",
        )
        return response.json()

    @use_authenticate
    def get_delivery_points(self, city_code: str) -> List[Dict]:
        response = self.client.get(
            f"{self.base_url}deliverypoints?city_code={city_code}",
        )
        return response.json()

    @use_authenticate
    def get_regions(self) -> List[Dict]:
        response = self.client.get(
            f"{self.base_url}location/regions?country_codes=RU",
        )
        return response.json()

    @use_authenticate
    def get_cities(self, region_code: str) -> List[Dict]:
        response = self.client.get(
            f"{self.base_url}location/cities?region_code={region_code}",
        )
        return response.json()


    def check_delivery_point(self, point_id: str) -> bool:
        return False


cdek_worker = CDEK(
    config.config.cdek_client_id,
    config.config.cdek_client_secret,
    config.config.cdek_base_url
)

