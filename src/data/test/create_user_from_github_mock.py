

from faker import Faker
from src.domain.usecases import CreateUserFromGitHubContract, CreateUserFromGitHubParams, CreateUserParams
from typing import Dict

faker = Faker()

class CreateUserFromGithubMock(CreateUserFromGitHubContract):

    def __init__(self):
        self.execute_params = {}
        self.return_value = {}

    def execute(self, params: CreateUserFromGitHubParams ) -> Dict:
        self.execute_params = params
        if(not self.return_value):
            self.return_value = {"success": True, "message": "ok", "data": CreateUserParams(
                params.username,
                faker.name(),
                faker.name(),
                faker.word(),
                faker.word(),
                faker.email(),
                params.gender
            )}
        return self.return_value