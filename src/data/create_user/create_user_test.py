from src.infra.test.user_repository_mock import UserRepositoryMock
from src.domain.test import user_mock
from .create_user import CreateUser, CreateUserParams

repo_mock = UserRepositoryMock()
sut = CreateUser(repo_mock)

def test_create_user_return():
    """Should return correct data on success"""
    user = user_mock()
    result = sut.execute(CreateUserParams(
        user.username,
        user.name,
        user.email,
        user.last_name,
        user.profile_image_url,
        user.bio,
        user.gender
    ))

    assert result["message"] == "ok"
    assert result["success"] == True

    user_data = result["data"]

    assert user_data.username == user.username
    assert user_data.name == user.name
    assert user_data.last_name == user.last_name
    assert user_data.profile_image_url == user.profile_image_url
    assert user_data.bio == user.bio
    assert user_data.email == user.email
    assert user_data.gender == user.gender


def test_create_user_call_repository():
    """Should call repository with correct params"""
    user = user_mock()
    sut.execute(CreateUserParams(
        user.username,
        user.name,
        user.email,
        user.last_name,
        user.profile_image_url,
        user.bio,
        user.gender
    ))

    assert repo_mock.insert_user_params["username"] == user.username
    assert repo_mock.insert_user_params["name"] == user.name
    assert repo_mock.insert_user_params["last_name"] == user.last_name
    assert repo_mock.insert_user_params["profile_image_url"] == user.profile_image_url
    assert repo_mock.insert_user_params["bio"] == user.bio
    assert repo_mock.insert_user_params["email"] == user.email
    assert repo_mock.insert_user_params["gender"] == user.gender