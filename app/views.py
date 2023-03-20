from app.services import DatetimeService, ArgentineBanksServices
from flask import jsonify, redirect, url_for, request
from app.constants import VERSION_API
from app import app


@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("get_status"))


@app.route("/status", methods=["GET"])
def get_status():
    response: dict = {
        "message": "'Dollar-exchange-rate-argentine-banks' API works!",
        "status_code": 200,
        "version": VERSION_API,
    }
    return jsonify(response), 200


@app.route("/banks", methods=["GET"])
def get_dollar_data_from_pages():
    try:
        datetime = DatetimeService.get_time()
        argentine_banks = ArgentineBanksServices().get_dollar_values_of_banks()

        response: dict = {
            "datetime": datetime,
            "banks": argentine_banks,
        }
        return jsonify(response), 200

    except Exception as err:
        response: dict = {"message": f"Banks error: {str(err)}"}
        return jsonify(response), 400


@app.errorhandler(404)
def not_found(error=None):
    response: dict = {
        "message": f"Resource not found: '{request.url}'",
        "status_code": 404,
    }
    return jsonify(response), 404
