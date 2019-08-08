from flask import Blueprint, make_response, jsonify

ilifev7s_api = Blueprint('ilifev7s_api', __name__)


@ilifev7s_api.route('/ilifev7s', methods=['POST'])
def send_response():
    res = {
        "testKey": "testValue"
    }
    return jsonify(res)
