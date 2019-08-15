import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

from actions_on_google.config.config import ENVIRONMENT, PORT, SSL_CONTEXT_CERT, SSL_CONTEXT_KEY, SENTRY_DSN
from actions_on_google.controllers.ilifev7s import ilifev7s_api

if SENTRY_DSN:
    sentry_sdk.init(dsn=SENTRY_DSN, integrations=[FlaskIntegration()])

app = Flask(__name__)
app.register_blueprint(ilifev7s_api)


@app.route('/')
def hello():
    return 'Welcome to the actions on Google server!'


if __name__ == '__main__':
    ssl_context = None
    if ENVIRONMENT != 'development':
        ssl_context = (SSL_CONTEXT_CERT, SSL_CONTEXT_KEY)

    app.run(
        port=PORT,
        host='0.0.0.0',
        ssl_context=ssl_context
    )
