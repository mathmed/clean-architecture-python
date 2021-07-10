from src.presentation.controllers import CreateUserController
from src.data.create_user import CreateUser
from src.infra.database.repositories import UserRepository

def create_user_factory() -> CreateUserController:
    repository = UserRepository()
    use_case = CreateUser(repository)
    create_user_controller = CreateUserController(use_case)
    return create_user_controller