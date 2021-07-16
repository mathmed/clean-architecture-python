from src.infra.test.user_repository_mock import UserRepositoryMock
from src.domain.test import user_mock
from .update_user import UpdateUser, UpdateUserParams
from faker import Faker

faker = Faker()

repo_mock = UserRepositoryMock()
sut = UpdateUser(repo_mock)
user = user_mock()
user_params = UpdateUserParams(
    user.name,
    user.email,
    user.last_name,
    user.profile_image_url,
    user.bio,
    user.gender
)

def test_should_return_correct_data_on_success():
    user_params.username = user.username
    repo_mock.return_select = user_params
    result = sut.execute(user.username, user_params)

    assert result["message"] == "ok"
    assert result["success"] == True

    user_data = result["data"]

    assert user_data.username == user_params.username
    assert user_data.name == user_params.name
    assert user_data.last_name == user_params.last_name
    assert user_data.profile_image_url == user_params.profile_image_url
    assert user_data.bio == user_params.bio
    assert user_data.email == user_params.email
    assert user_data.gender == user_params.gender


def test_should_return_error_if_user_not_exists():
    repo_mock.return_select = None
    result = sut.execute(user.username, user_params)

    assert result["message"] == "User {} not found".format(user.username)
    assert result["success"] == False
    assert result["data"] == {}

    
def test_should_return_error_if_email_already_exists():
    username = faker.name()
    user_params.username = username
    user_params.email = user.email
    repo_mock.return_select = user_params
    result = sut.execute(user.username, user_params)

    assert result["message"] == "User {} already exists".format(username)
    assert result["success"] == False
    assert result["data"] == {}

def test_should_call_update_user_repository_with_correct_params():

    user_params.username = user.username
    repo_mock.return_select = user_params
    result = sut.execute(user.username, user_params)

    assert repo_mock.update_user_params["username"] == user.username
    assert repo_mock.update_user_params["user"].name == user.name
    assert repo_mock.update_user_params["user"].last_name == user.last_name
    assert repo_mock.update_user_params["user"].profile_image_url == user.profile_image_url
    assert repo_mock.update_user_params["user"].bio == user.bio
    assert repo_mock.update_user_params["user"].email == user.email
    assert repo_mock.update_user_params["user"].gender == user.gender