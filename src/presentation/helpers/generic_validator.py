from typing import Dict
from src.presentation.errors import HttpErrors
from src.presentation.helpers import HttpResponse

def validate(required_fields: [], body: Dict) -> HttpResponse:
    missing_fields = []
    for field in required_fields:
        if field not in body:
            missing_fields.append(field)
    if(len(missing_fields) > 0):
            http_error =  HttpErrors.error_400("Missing required field (s): {}".format(', '.join(missing_fields)))
            return HttpResponse(http_error["status_code"], http_error["body"])
    return None