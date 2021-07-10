from typing import Type
from src.domain.usecases import CreateUser, CreateUserParams
from src.presentation.helpers import HttpRequest, HttpResponse, validate
from src.presentation.errors import HttpErrors
from src.presentation.contracts import ControllerContract

class CreateUserController(ControllerContract):
    def __init__(self, use_case: Type[CreateUser]):
        self.use_case = use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:

        error = validate(("username", "name", "email"), http_request.body)

        if(error):
            return error

        body_data = http_request.body

        params = CreateUserParams(
            body_data["username"],
            body_data["name"],
            body_data["email"],
            body_data["last_name"] if "last_name" in body_data else None,
            body_data["profile_image_url"] if "profile_image_url" in body_data else None,
            body_data["bio"] if "bio" in body_data else None,
            body_data["gender"] if "gender" in body_data else None,
        )
        
        response = self.use_case.execute(params)

        if response["success"] is False:
            http_error =  HttpErrors.error_422(response["message"])
            return HttpResponse(http_error["status_code"], http_error["body"])

        created_user_data = response["data"]
        response_data = {
            "user": {
                "username": created_user_data.username,
                "name": created_user_data.name,
                "last_name": created_user_data.last_name,
                "bio": created_user_data.bio,
                "email": created_user_data.email,
                "profile_image_url": created_user_data.profile_image_url,
                "gender": created_user_data.gender
            },
            "message": response["message"],
            "status_code": 200
        }

        return HttpResponse(200, response_data)
