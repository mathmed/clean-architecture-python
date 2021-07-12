from src.presentation.controllers import CreateUserFromGitHubController
from src.data.create_user_from_github import CreateUserFromGithub
from src.infra.database.repositories import UserRepository
from src.infra.http import Requests

def create_user_from_github_factory() -> CreateUserFromGitHubController:
    http_requests = Requests()
    repository = UserRepository()
    use_case = CreateUserFromGithub(http_requests, repository)
    create_user_controller = CreateUserFromGitHubController(use_case)
    return create_user_controller