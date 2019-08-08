from flask import Flask

from actions_on_google.config.config import ENVIRONMENT, PORT
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
        ssl_context = (
            '/etc/letsencrypt/live/my.awesome.domain/fullchain.pem',
            '/etc/letsencrypt/live/my.awesome.domain/privkey.pem'
        )

    app.run(
        debug=debug,
        port=PORT,
        host='0.0.0.0',
        ssl_context=ssl_context
    )
