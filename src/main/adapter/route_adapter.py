import traceback
from typing import Type
from sqlalchemy.exc import IntegrityError
from src.presentation.errors import HttpErrors
from src.presentation.contracts import ControllerContract, HttpRequest, HttpResponse

def flask_adapter(request: any, api_route: Type[ControllerContract], url_param: str = None) -> any:

    try:
        query_string_params = request.args.to_dict()
    except:
        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )

    http_request = HttpRequest(
        header=request.headers, body=request.json, query=query_string_params, url_param=url_param
    )

    try:
        response = api_route.handle(http_request)

    except IntegrityError:
        https_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
    except Exception:
        traceback.print_exc()
        https_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
    return response