from flask import Flask

from actions_on_google.config.config import ENVIRONMENT, PORT, SSL_CONTEXT_CERT, SSL_CONTEXT_KEY
from actions_on_google.controllers.ilifev7s import ilifev7s_api

app = Flask(__name__)

app.register_blueprint(ilifev7s_api)


@app.route("/")
def hello():
    return "Welcome to the actions on Google server!"


if __name__ == '__main__':
    debug = True
    ssl_context = None
    if ENVIRONMENT is 'prod':
        debug = False
        ssl_context = (SSL_CONTEXT_CERT, SSL_CONTEXT_KEY)

    app.run(
        debug=debug,
        port=PORT,
        host='0.0.0.0',
        ssl_context=ssl_context
    )
