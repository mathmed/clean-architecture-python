from abc import ABC, abstractmethod
from typing import Dict

class HttpRequestContract(ABC):
    
    @abstractmethod
    def get(self, url: str) -> Dict:
        raise Exception("Method not implemented")
    