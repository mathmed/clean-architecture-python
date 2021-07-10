from typing import Type, Dict
from src.domain.usecases import CreateUserParams, CreateUserContract
from src.data.contracts import UserRepositoryContract, CreateUserParams as CreateUserDBParams

class CreateUser(CreateUserContract):

    def __init__(self, user_repository: Type[UserRepositoryContract]):
        self.user_repository = user_repository

    def execute(self, params: CreateUserParams ) -> Dict:
        
        user_exists = self.user_repository.select_user(field_filter="username", value=params.username)
        email_exists = self.user_repository.select_user(field_filter="email", value=params.email)

        if(user_exists or email_exists):
            return {"success": False, "message": "User {} already exists".format(user_exists.username if user_exists else email_exists.email), "data": {}}

        response = self.user_repository.insert_user(
            CreateUserDBParams(
                params.username, params.name, params.email, params.last_name, params.profile_image_url, params.bio, params.gender
                )
            )
        return {"success": True, "message": "ok", "data": response}