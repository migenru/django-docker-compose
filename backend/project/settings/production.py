from .base import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


DEBUG = False
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS').split(',')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
sentry_sdk.init(
    dsn=os.environ.get("SENTRY_URL"),
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)