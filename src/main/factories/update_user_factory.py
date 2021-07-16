from src.presentation.controllers import UpdateUserController
from src.data.update_user import UpdateUser
from src.infra.database.repositories import UserRepository

def update_user_factory() -> UpdateUserController:
    repository = UserRepository()
    use_case = UpdateUser(repository)
    update_user_controller = UpdateUserController(use_case)
    return update_user_controller