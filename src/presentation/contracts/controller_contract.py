from typing import Type, Dict
from abc import ABC, abstractmethod
class HttpRequest:

    def __init__(self, header: Dict = None, body: Dict = None, query: Dict = None):
        self.header = header
        self.body = body
        self.query = query

    def __repr__(self):
        return (
            f"HttpRequest (header={self.header}, body={self.body}, query={self.query})"
        )
class HttpResponse:

    def __init__(self, status_code: int, body: any):
        self.status_code = status_code
        self.body = body

    def __repr__(self):
        return f"HttpResponse (status_code={self.status_code}, body={self.body})"
        
class ControllerContract(ABC):
    
    @abstractmethod
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        raise Exception("Should implement method: route")