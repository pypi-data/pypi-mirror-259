from abc import ABC, abstractmethod
from typing import Dict, List

import httpx

def use_authenticate(method):
    def wrapper(*args, **kwargs):
        if args[0].is_auth is False:
            args[0].authenticate()
        return method(*args, **kwargs)
    return wrapper



class Delivery(ABC):
    def __init__(self, client_id: str, client_secret: str, base_url: str) -> None:
        self.client_id: str = client_id
        self.client_secret: str = client_secret
        self.base_url: str = base_url
        self.access_token: str = ""
        self.client = httpx.Client()

    @abstractmethod
    def authenticate(self) -> None:
        pass

    @abstractmethod
    def post_order(self, data: Dict) -> Dict:
        pass

    @abstractmethod
    def get_order_info(self, order_d: str) -> Dict:
        pass

    @abstractmethod
    def get_delivery_points(self, city_code: str) -> List[Dict]:
        pass

    @abstractmethod
    def get_regions(self) -> List[Dict]:
        pass

    @abstractmethod
    def get_cities(self, region_code: str) -> List[Dict]:
        pass

    @abstractmethod
    def check_delivery_point(self, point_id: str) -> bool:
        pass
