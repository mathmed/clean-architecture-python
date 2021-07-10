from typing import Type, Dict
from src.domain.usecases import CreateUserParams, CreateUser as CreateUserContract
from src.data.contracts import UserRepositoryContract, CreateUserParams as CreateUserDBParams

class CreateUser(CreateUserContract):

    def __init__(self, user_repository: Type[UserRepositoryContract]):
        self.user_repository = user_repository

    def execute(self, params: CreateUserParams ) -> Dict:
        
        response = self.user_repository.insert_user(
            CreateUserDBParams(
                params.username, params.name, params.email, params.last_name, params.profile_image_url, params.bio, params.gender
                )
            )
        return {"success": True, "message": "ok", "data": response}