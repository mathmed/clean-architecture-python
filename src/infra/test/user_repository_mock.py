
from src.domain.models import User
from src.data.contracts import UserRepositoryContract
from src.data.contracts import CreateUserParams

class UserRepositoryMock(UserRepositoryContract):

    def __init__(self):
        self.insert_user_params = {}
        self.select_user_params = {}
        self.return_select = {}

    def insert_user(self, params: CreateUserParams) -> User:
        self.insert_user_params["username"] = params.username
        self.insert_user_params["name"] = params.name
        self.insert_user_params["last_name"] = params.last_name
        self.insert_user_params["profile_image_url"] = params.profile_image_url
        self.insert_user_params["bio"] = params.bio
        self.insert_user_params["email"] = params.email
        self.insert_user_params["gender"] = params.gender
        return User(params.username, params.name, params.last_name, params.profile_image_url, params.bio, params.email, params.gender)

    def select_user(self, field_filter: str = None, value: str = None) -> User:
        self.select_user_params["field"] = field_filter
        self.select_user_params["value"] = value
        if(self.return_select == {}):
            self.return_select = self.insert_user_params
        return self.return_select