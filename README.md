# actions-on-google
The aim of this project is an hub for multiple [Actions on Google](https://developers.google.com/actions/)<br><br>


## Integrations
- [ilifev7s-rest-remote](https://github.com/pimuzzo/ilifev7s-rest-remote) Rest remote for Chuwi iLife v7s<br><br>


## Install ALL dependencies
`PIPENV_VENV_IN_PROJECT=1 pipenv install --dev`<br><br>


## Configuration
Take a look to `config.py`
- `ENVIRONMENT` takes the value from [FLASK_ENV](https://flask.palletsprojects.com/en/1.0.x/cli/#environments)
- `SSL_CONTEXT_CERT` and `SSL_CONTEXT_KEY` are used only if `ENVIRONMENT` is not 'development' (you can use [letsencrypt](https://letsencrypt.org/) to generate them)
- `BASIC_AUTH_USERNAME` and `BASIC_AUTH_PASSWORD` are optional but recommended to enable basic auth
- `SENTRY_DSN` is optional and it is the [Sentry](https://sentry.io/) API key<br><br>


## Usage
Run the app (`FLASK_ENV` is optional and it defaults to 'production'):
- `PYTHONPATH=".:actions_on_google" FLASK_ENV=development pipenv run python actions_on_google/app.py`<br><br>


# Certificate
To renew a certificate the project must be served on port 80 and with basic-auth disabled.
Use the command:
- `certbot renew --webroot -w $PROJECT_PATH/actions-on-google/actions_on_google/static/`

I will improve it when I have more time<br><br>

## Thanks to
- [Actions on Google example](https://github.com/gdgpisa/actions-on-google-diy) The code from [GDG Pisa](https://gdgpisa.it/) that I used to start my project
