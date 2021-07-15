from abc import ABC, abstractmethod
from typing import Dict

class UpdateUserParams:
    def __init__(self, name: str, email: str, last_name: str, profile_image_url: str, bio: str, gender: str):
        self.name = name
        self.last_name = last_name
        self.profile_image_url = profile_image_url
        self.bio = bio
        self.email = email
        self.gender = gender

class UpdateUserContract(ABC):
    
    @abstractmethod
    def execute(self, params: UpdateUserParams ) -> Dict:
        raise Exception("Method not implemented")
