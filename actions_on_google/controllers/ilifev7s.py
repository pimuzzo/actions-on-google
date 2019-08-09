import requests
from flask import Blueprint, jsonify, request, current_app

from actions_on_google.config.config import ILIFEV7S_ALLOWED_ACTIONS, ENVIRONMENT, ILIFEV7S_ENDPOINT

ilifev7s_api = Blueprint('ilifev7s_api', __name__)


@ilifev7s_api.route('/ilifev7s', methods=['POST'])
def send_response():
    try:
        req = request.get_json(force=True)
    except:
        return jsonify({'error': 'failed to decode JSON object'}), 400
    current_app.logger.info(f'received object: {req}')

    try:
        # queryResult:='{"parameters": {"action": "clean"}}'
        action = req['queryResult']['parameters']['action']
    except:
        return jsonify({'error': 'missing queryResult.parameters.action parameter'}), 400

    if action not in ILIFEV7S_ALLOWED_ACTIONS:
        return jsonify({'error': f'action {action} not permitted'}), 400

    if ENVIRONMENT is 'prod':
        payload = {'action': action}
        requests.post(ILIFEV7S_ENDPOINT, data=payload)

    return jsonify(), 204
