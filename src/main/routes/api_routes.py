from flask import jsonify, Blueprint, request
from src.main.adapter import flask_adapter
from src.main.factories import create_user_factory

api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/api/user", methods=["POST"])
def create_user():

    response = flask_adapter(request=request, api_route=create_user_factory())
    
    if response.status_code < 300:
        return jsonify({"data": response.body}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )
