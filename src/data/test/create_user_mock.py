
from src.domain.usecases import CreateUser, CreateUserParams
from typing import Dict

class CreateUserMock(CreateUser):

    def __init__(self):
        self.execute_params = {}
        self.return_value = {}

    def execute(self, params: CreateUserParams ) -> Dict:
        self.execute_params = params
        if(not self.return_value):
            self.return_value = {"success": True, "message": "ok", "data": params}
        return self.return_value