"""
WSGI config for saasboilerplate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import environ

env = environ.Env()

from django.core.wsgi import get_wsgi_application

settings_module = (
    "saasboilerplate.production"
    if env("PRODUCTION", default=False)
    else "saasboilerplate.settings"
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
