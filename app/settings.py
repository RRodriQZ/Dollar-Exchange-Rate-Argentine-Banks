from os import environ


APP_PORT: int = int(environ.get("APP_PORT", 5000))
