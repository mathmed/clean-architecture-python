from typing import Type
from abc import ABC, abstractmethod
from src.presentation.helpers import HttpRequest, HttpResponse

class ControllerContract(ABC):
    
    @abstractmethod
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        raise Exception("Should implement method: route")