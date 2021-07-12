import requests
from typing import Dict
from src.data.contracts import HttpRequestContract

class Requests(HttpRequestContract):
    def get(self, url: str) -> Dict:
        try:
            result = requests.get(url)
            return result.json()
        except:
            return None