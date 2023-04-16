from .services import (
    DatetimeService,
    ArgentineBanksServices,
)
from . import dollar_scraping_v1
from flask import jsonify


@dollar_scraping_v1.route("/banks", methods=["GET"])
def get_dollar_data_from_pages():
    try:
        datetime: str = DatetimeService.get_time()
        argentine_banks: list = ArgentineBanksServices().get_dollar_values_of_banks()

        response: dict = {
            "datetime": datetime,
            "banks": argentine_banks,
        }
        return jsonify(response), 200

    except Exception as err:
        response: dict = {"message": f"Banks error: {str(err)}"}
        return jsonify(response), 400
