from ...config import API_VERSION
from flask import (
    redirect,
    jsonify,
)
from . import index


@index.route("/", methods=["GET"])
def get_index():
    return redirect("/status")


@index.route("/status", methods=["GET"])
def get_status():
    response: dict = {
        "message": "'Dollar-exchange-rate-argentine-banks' API works!",
        "status_code": 200,
        "version": API_VERSION,
    }
    return jsonify(response), 200
