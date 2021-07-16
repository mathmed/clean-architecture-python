from faker import Faker
from .update_user_controller import UpdateUserController
from src.data.test import UpdateUserMock
from src.presentation.contracts import HttpRequest
from src.domain.test import user_mock

mock_update_user = UpdateUserMock()
sut = UpdateUserController(mock_update_user)
faker = Faker()
user = user_mock()
request_data = {
    "name": user.name,
    "last_name": user.last_name,
    "bio": user.bio,
    "email": user.email,
    "profile_image_url": user.profile_image_url,
    "gender": user.gender
}

def test_should_return_200_on_success():

    username = faker.name()
    request = HttpRequest(body = request_data, url_param=username)
    result = sut.handle(request)
    result_user = result.body["user"]
    result_message = result.body["message"]
    result_status_code = result.body["status_code"]

    assert result.status_code == 200
    assert result_user["username"] == username
    assert result_user["name"] == request_data["name"]
    assert result_user["last_name"] == request_data["last_name"]
    assert result_user["bio"] == request_data["bio"]
    assert result_user["email"] == request_data["email"]
    assert result_user["profile_image_url"] == request_data["profile_image_url"]
    assert result_user["gender"] == request_data["gender"]
    assert result_message == "ok"
    assert result_status_code == 200

def test_should_call_create_user_with_correct_params():

    username = faker.name()
    request = HttpRequest(body = request_data, url_param=username)
    sut.handle(request)
    
    assert mock_update_user.execute_params.username == username
    assert mock_update_user.execute_params.name == request_data["name"]
    assert mock_update_user.execute_params.last_name == request_data["last_name"]
    assert mock_update_user.execute_params.bio == request_data["bio"]
    assert mock_update_user.execute_params.email == request_data["email"]
    assert mock_update_user.execute_params.profile_image_url == request_data["profile_image_url"]
    assert mock_update_user.execute_params.gender == request_data["gender"]

def test_should_return_422_on_error():

    return_value = {"success": False, "message": faker.word(), "data": faker.word()}
    mock_update_user.return_value = return_value
    request = HttpRequest(body = request_data)
    result = sut.handle(request)
    assert result.status_code == 422
    assert result.body["error"] == return_value["message"]
    

