from .requests import Requests

sut = Requests()

def test_should_make_get_request_successfully():
   
    request_result = sut.get("https://httpbin.org/get?any_arg=any_value")   
    assert request_result["args"]["any_arg"] == "any_value"

