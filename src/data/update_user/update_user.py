from typing import Type, Dict
from src.domain.usecases import UpdateUserParams, UpdateUserContract
from src.data.contracts import UserRepositoryContract, UpdateUserParams as UpdateUserDBParams

class UpdateUser(UpdateUserContract):

    def __init__(self, user_repository: Type[UserRepositoryContract]):
        self.user_repository = user_repository

    def execute(self, username: str, params: UpdateUserParams ) -> Dict:
        
        user = self.user_repository.select_user(field_filter="username", value=username)

        if(not user):
            return {"success": False, "message": "User {} not found".format(username), "data": {}}

        user = self.user_repository.select_user(field_filter="email", value=params.email)
        
        if(user and user.username != username ):
            return {"success": False, "message": "User {} already exists".format(user.username), "data": {}}

        response = self.user_repository.update_user(
            username,
            UpdateUserDBParams(params.name, params.email, params.last_name, params.profile_image_url, params.bio, params.gender)
        )
               
        return {"success": True, "message": "ok", "data": response}