from src.infra.test import UserRepositoryMock, RequestsMock
from src.domain.test import user_mock
from .create_user_from_github import CreateUserFromGithub, CreateUserFromGitHubParams
from faker import Faker

faker = Faker()

repo_mock = UserRepositoryMock()
requests_mock = RequestsMock()
sut = CreateUserFromGithub(requests_mock, repo_mock)
user = user_mock()
user_params = CreateUserFromGitHubParams(
    user.username,
    user.gender
)

def test_should_return_correct_data_on_success():
    repo_mock.return_select = None
    return_http = {
        "name": faker.name(),
        "login": faker.name(),
        "email": faker.email(),
        "avatar_url": faker.url(),
        "bio": faker.words()
    }
    requests_mock.return_get = return_http
    result = sut.execute(user_params)

    assert result["message"] == "ok"
    assert result["success"] == True

    user_data = result["data"]

    assert user_data.username == user.username
    assert user_data.name == return_http["name"].split(" ")[0]
    assert user_data.last_name == return_http["name"].split(" ")[-1]
    assert user_data.profile_image_url == return_http["avatar_url"]
    assert user_data.bio == return_http["bio"]
    assert user_data.email == return_http["email"]
    assert user_data.gender == user.gender



def test_should_call_repository_with_correct_params():

    return_http = {
        "name": faker.name(),
        "login": faker.name(),
        "email": faker.email(),
        "avatar_url": faker.url(),
        "bio": faker.words()
    }
    requests_mock.return_get = return_http

    sut.execute(user_params)

    assert repo_mock.insert_user_params["username"] == user.username
    assert repo_mock.insert_user_params["gender"] == user.gender
    assert repo_mock.insert_user_params["name"] == return_http["name"].split(" ")[0]
    assert repo_mock.insert_user_params["last_name"] == return_http["name"].split(" ")[-1]
    assert repo_mock.insert_user_params["profile_image_url"] == return_http["avatar_url"]
    assert repo_mock.insert_user_params["bio"] == return_http["bio"]
    assert repo_mock.insert_user_params["email"] == return_http["email"]


def test_should_requet_with_correct_params():

    sut.execute(user_params)
    url = "https://api.github.com/users/{}".format(user_params.username)
    assert requests_mock.get_params["url"] == url



def test_should_return_error_if_user_exists():

    requests_mock.return_get = None

    result = sut.execute(user_params)

    assert result["success"] == False
    assert result["message"] == "User {} not found on Github".format(user_params.username)
    assert result["data"] == {}



def test_should_return_error_if_user_doesnot_have_email():

    return_http = {
        "name": faker.name(),
        "login": faker.name(),
        "email": None,
        "avatar_url": faker.url(),
        "bio": faker.words()
    }
    requests_mock.return_get = return_http

    result = sut.execute(user_params)

    assert result["success"] == False
    assert result["message"] == "User email not found on Github"
    assert result["data"] == {}

