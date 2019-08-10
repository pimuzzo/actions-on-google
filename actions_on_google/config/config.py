import os

# Global
ENVIRONMENT = os.environ.get('FLASK_ENV')  # development or production (default)
PORT = 4043
SSL_CONTEXT_CERT = '/etc/letsencrypt/live/my.awesome.domain/fullchain.pem'
SSL_CONTEXT_KEY = '/etc/letsencrypt/live/my.awesome.domain/privkey.pem'
SENTRY_DSN = ''

# Ilife v7s zone
ILIFEV7S_ALLOWED_ACTIONS = ['wake_up', 'clean', 'stop', 'up', 'down', 'left', 'right', 'spot', 'home', 'edge']
ILIFEV7S_ENDPOINT = 'http://ilifev7s-rest-remote.local/ilifev7s'
