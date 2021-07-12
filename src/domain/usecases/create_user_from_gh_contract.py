from abc import ABC, abstractmethod
from typing import Dict

class CreateUserFromGitHubParams:
    def __init__(self, username: str, gender: str):
        self.username = username
        self.gender = gender

class CreateUserFromGitHubContract(ABC):
    
    @abstractmethod
    def execute(self, params: CreateUserFromGitHubParams ) -> Dict:
        raise Exception("Method not implemented")
