from flask import (
    jsonify,
    request,
)


def register_error_handlers(app) -> dict:
    """
    This function registers an error handler for HTTP 404 errors in a Flask app and returns a JSON
    response with a message and status code.
    :param app: The "app" parameter is an instance of a Flask application. It is used to register the
    error handler function as a route in the application
    :return: The function `not_found` is returning a dictionary `response` containing a message and a
    status code, both related to a 404 error. The dictionary is then converted to a JSON response using
    the `jsonify` function and returned along with a 404 status code.
    """
    @app.errorhandler(404)
    def not_found(error=None) -> dict:
        response: dict = {
            "message": f"Resource not found: {request.url}",
            "status_code": 404,
        }
        return jsonify(response), 404
