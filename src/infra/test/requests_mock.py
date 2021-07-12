from typing import Dict
from src.data.contracts import HttpRequestContract

class RequestsMock(HttpRequestContract):
    def __init__(self):
        self.get_params = {}
        self.return_get = {}

    def get(self, url: str) -> Dict:
        self.get_params["url"] = url
        if(self.return_get == {}):
            self.return_get = self.return_get
        return self.return_get