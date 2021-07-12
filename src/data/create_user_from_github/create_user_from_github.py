from src.domain.usecases import CreateUserFromGitHubContract, CreateUserFromGitHubParams
from src.data.contracts import HttpRequestContract, UserRepositoryContract, CreateUserParams as CreateUserDBParams
from typing import Type, Dict


class CreateUserFromGithub(CreateUserFromGitHubContract):

    def __init__(self, http_request: Type[HttpRequestContract], user_repository: Type[UserRepositoryContract]):
        self.http_request = http_request
        self.user_repository = user_repository

    def execute(self, params: CreateUserFromGitHubParams ) -> Dict:

        url = "https://api.github.com/users/{}".format(params.username)
        user_github = self.http_request.get(url)

        if(not user_github or not "login" in user_github):
            return {"success": False, "message": "User {} not found on Github".format(params.username), "data": {}}

        if(not user_github["email"]):
            return {"success": False, "message": "User email not found on Github", "data": {}}
        
        create_user_data = CreateUserDBParams(
            params.username,
            user_github["name"].split(" ")[0],
            user_github["email"],
            user_github["name"].split(" ")[-1],
            user_github["avatar_url"],
            user_github["bio"],
            params.gender
        )

        created_user = self.user_repository.insert_user(create_user_data)
            
        return {"success": True, "message": "ok", "data": created_user}