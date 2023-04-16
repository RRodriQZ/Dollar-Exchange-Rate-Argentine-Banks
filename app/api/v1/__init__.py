from flask import Blueprint


# Register "model v1" module
dollar_scraping_v1 = Blueprint("dollar_scraping_v1", __name__)


from . import routes
