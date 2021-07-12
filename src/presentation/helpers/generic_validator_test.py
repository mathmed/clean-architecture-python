from .generic_validator import validate
from faker import Faker

faker = Faker()

def test_should_return_none_on_success():
    field = faker.word()
    validate_result = validate([field], {field: faker.word()})
    assert validate_result == None

def test_should_return_response_error():
    field = faker.word()
    validate_result = validate([field], {faker.word(): faker.word()})
    assert validate_result.body["error"] == "Missing required field (s): {}".format(field)
    assert validate_result.status_code == 400


