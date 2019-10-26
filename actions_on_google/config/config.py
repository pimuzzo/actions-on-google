import os

# Global
ENVIRONMENT = os.environ.get('FLASK_ENV')  # development or production (default)
PORT = 4043
BASIC_AUTH_USERNAME = ''
BASIC_AUTH_PASSWORD = ''
BASIC_AUTH_FORCE = True
SSL_CONTEXT_CERT = '/etc/letsencrypt/live/my.awesome.domain/fullchain.pem'
SSL_CONTEXT_KEY = '/etc/letsencrypt/live/my.awesome.domain/privkey.pem'
SENTRY_DSN = ''

# Ilife v7s zone
ILIFEV7S_ALLOWED_ACTIONS = ['wake_up', 'clean', 'stop', 'spot', 'home', 'edge']
ILIFEV7S_ENDPOINT = 'http://192.168.XXX.XXX/ilifev7s'
