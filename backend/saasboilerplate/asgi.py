"""
ASGI config for saasboilerplate project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import environ

env = environ.Env()

from django.core.asgi import get_asgi_application

settings_module = (
    "saasboilerplate.production"
    if env("VUE_APP_PRODUCTION", default=False)
    else "saasboilerplate.settings"
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_asgi_application()
