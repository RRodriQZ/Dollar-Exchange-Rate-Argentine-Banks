from app.service import ArgentineBanksService
from app.settings import VERSION_ID
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/status", methods=["GET"])
def status() -> None:
    """ Return 'Dollar exchange rate argentine banks' API status """
    response = {
        "message": "'Dollar-exchange-rate-argentine-banks' API works!",
        "status_code": 200,
        "version": VERSION_ID,
    }
    return jsonify(response)


@app.route("/banks", methods=["GET"])
def get_dollar_data_from_pages():
    """ Return Dollar exchange rate all argentine banks """
    argentine_banks = ArgentineBanksService().get_dollar_values_of_banks()
    return jsonify(argentine_banks)


@app.errorhandler(404)
def not_found(error=None):
    """ Error handler for resources that are not covered """
    response = {
        "message": f"Resource not found: '{request.url}'",
        "status_code": 404,
    }
    return jsonify(response), 404
