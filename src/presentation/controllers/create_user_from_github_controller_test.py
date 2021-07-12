from faker import Faker
from .create_user_from_github_controller import CreateUserFromGitHubController
from src.data.test import CreateUserFromGithubMock
from src.presentation.helpers import HttpRequest
from src.domain.test import user_mock

mock_create_user = CreateUserFromGithubMock()
sut = CreateUserFromGitHubController(mock_create_user)
faker = Faker()
user = user_mock()
request_data = {
    "username": user.username,
    "gender": user.gender
}


def test_should_return_200_on_success():

    request = HttpRequest(body = request_data)
    result = sut.handle(request)
    result_user = result.body["user"]
    result_message = result.body["message"]
    result_status_code = result.body["status_code"]

    assert result.status_code == 200
    assert result_user["username"] == request_data["username"]
    assert result_user["gender"] == request_data["gender"]
    assert result_message == "ok"
    assert result_status_code == 200


def test_should_return_error_if_required_field_is_not_set():

    request = HttpRequest(body = {"field": faker.words()})
    result = sut.handle(request)
    assert result.status_code == 400
    assert result.body["error"] == 'Missing required field (s): username'


def test_should_call_create_user_with_correct_params():

    request = HttpRequest(body = request_data)
    sut.handle(request)
    
    assert mock_create_user.execute_params.username == request_data["username"]
    assert mock_create_user.execute_params.gender == request_data["gender"]


def test_should_return_422_on_error():

    return_value = {"success": False, "message": faker.word(), "data": faker.word()}
    mock_create_user.return_value = return_value
    request = HttpRequest(body = request_data)
    result = sut.handle(request)
    assert result.status_code == 422
    assert result.body["error"] == return_value["message"]
    