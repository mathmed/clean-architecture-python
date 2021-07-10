
class HttpErrors:

    @staticmethod
    def error_400(custom_msg: str = None):
        return {"status_code": 400, "body": {"error": custom_msg or "Bad Request"}}

    @staticmethod
    def error_404(custom_msg: str = None):
        return {"status_code": 404, "body": {"error": custom_msg or "Not Found"}}

    @staticmethod
    def error_409(custom_msg: str = None):
        return {"status_code": 409, "body": {"error": custom_msg or "Conflict"}}

    @staticmethod
    def error_422(custom_msg: str = None):
        return {"status_code": 422, "body": {"error": custom_msg or "Unprocessable Entity"}}

    @staticmethod
    def error_500(custom_msg: str = None):
        return {"status_code": 500, "body": {"error": custom_msg or "Internal Server Error"}}