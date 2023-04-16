from os import environ


API_VERSION: str = environ.get("API_VERSION", "1.0.1")
APP_PORT: int = int(environ.get("APP_PORT", 5000))
ENVIRONMENT: str = environ.get("ENVIRONMENT", "local")
