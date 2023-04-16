from flask import Blueprint


# Register "index" module
index = Blueprint("index", __name__)


from . import routes
