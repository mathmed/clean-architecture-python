
from src.domain.usecases import UpdateUserContract, UpdateUserParams
from typing import Dict

class UpdateUserMock(UpdateUserContract):

    def __init__(self):
        self.execute_params = {}
        self.return_value = {}

    def execute(self, username: str, params: UpdateUserParams ) -> Dict:
        self.execute_params = params
        self.execute_params.username = username
        if(not self.return_value):
            self.return_value = {"success": True, "message": "ok", "data": params}
        return self.return_value