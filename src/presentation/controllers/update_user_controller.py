from typing import Type
from src.domain.usecases import UpdateUserContract, UpdateUserParams
from src.presentation.helpers import validate
from src.presentation.errors import HttpErrors
from src.presentation.contracts import ControllerContract, HttpRequest, HttpResponse

class UpdateUserController(ControllerContract):
    def __init__(self, use_case: Type[UpdateUserContract]):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        body_data = http_request.body
        username = http_request.url_param

        params = UpdateUserParams(
            body_data["name"] if "name" in body_data else None,
            body_data["email"] if "email" in body_data else None,
            body_data["last_name"] if "last_name" in body_data else None,
            body_data["profile_image_url"] if "profile_image_url" in body_data else None,
            body_data["bio"] if "bio" in body_data else None,
            body_data["gender"] if "gender" in body_data else None,
        )
        
        response = self.use_case.execute(username, params)

        if response["success"] is False:
            http_error =  HttpErrors.error_422(response["message"])
            return HttpResponse(http_error["status_code"], http_error["body"])

        updated_user_data = response["data"]
        response_data = {
            "user": {
                "username": updated_user_data.username,
                "name": updated_user_data.name,
                "last_name": updated_user_data.last_name,
                "bio": updated_user_data.bio,
                "email": updated_user_data.email,
                "profile_image_url": updated_user_data.profile_image_url,
                "gender": updated_user_data.gender
            },
            "message": response["message"],
            "status_code": 200
        }

        return HttpResponse(200, response_data)
