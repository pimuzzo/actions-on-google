import sentry_sdk
from flask import Flask, send_from_directory
from flask_basicauth import BasicAuth
from sentry_sdk.integrations.flask import FlaskIntegration

from actions_on_google.config.config import ENVIRONMENT, PORT, SSL_CONTEXT_CERT, SSL_CONTEXT_KEY, SENTRY_DSN, \
    BASIC_AUTH_USERNAME, BASIC_AUTH_PASSWORD, BASIC_AUTH_FORCE
from actions_on_google.controllers.ilifev7s import ilifev7s_api

if SENTRY_DSN:
    sentry_sdk.init(dsn=SENTRY_DSN, integrations=[FlaskIntegration()])

app = Flask(__name__)

if BASIC_AUTH_USERNAME and BASIC_AUTH_PASSWORD:
    app.config['BASIC_AUTH_USERNAME'] = BASIC_AUTH_USERNAME
    app.config['BASIC_AUTH_PASSWORD'] = BASIC_AUTH_PASSWORD
    app.config['BASIC_AUTH_FORCE'] = BASIC_AUTH_FORCE
    basic_auth = BasicAuth(app)

app.register_blueprint(ilifev7s_api)


@app.route('/')
def hello():
    return 'Welcome to the actions on Google server!'


@app.route('/.well-known/acme-challenge/<path:filename>')
def well_known_route(filename):
    return send_from_directory(app.root_path + '/static/.well-known/acme-challenge/', filename, conditional=True)


if __name__ == '__main__':
    ssl_context = None
    if ENVIRONMENT != 'development':
        ssl_context = (SSL_CONTEXT_CERT, SSL_CONTEXT_KEY)

    app.run(
        port=PORT,
        host='0.0.0.0',
        ssl_context=ssl_context
    )
