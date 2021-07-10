from abc import ABC, abstractmethod
from src.domain.models import User

class CreateUserParams:
    def __init__(self, username: str, name: str, email: str, last_name: str, profile_image_url: str, bio: str, gender: str):
        self.username = username
        self.name = name
        self.last_name = last_name
        self.profile_image_url = profile_image_url
        self.bio = bio
        self.email = email
        self.gender = gender

class UserRepositoryContract(ABC):
    
    @abstractmethod
    def insert_user(self, params: CreateUserParams) -> User:
        raise Exception("Method not implemented")
    
    @abstractmethod
    def select_user(self, field_filter: str = None, value: str = None) -> User:
        raise Exception("Method not implemented")
    