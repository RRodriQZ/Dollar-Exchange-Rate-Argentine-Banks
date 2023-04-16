from .error_handling import register_error_handlers
from .api.index import index
from .api.v1 import dollar_scraping_v1
from flask import Flask


def create_app() -> Flask:
    """
    This function creates and returns a Flask app with registered blueprints and custom error handlers.
    :return: The function `create_app()` is returning an instance of the Flask application with
    registered blueprints and custom error handlers.
    """
    # Initialize Api
    app = Flask(__name__)

    # Blueprints registration
    app.register_blueprint(blueprint=index)
    app.register_blueprint(blueprint=dollar_scraping_v1, url_prefix="/api/v1")

    # Custom error handlers
    register_error_handlers(app)

    return app
