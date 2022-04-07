#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys
import environ
from debugger import initialize_django_debugger

env = environ.Env()


def main():
    """Run administrative tasks."""

    if not env("VUE_APP_PRODUCTION", default=False):
        environ.Env.read_env("../.env.development")
        environ.Env.read_env("../.env.local", overwrite=True)
        if sys.argv[1] == "runserver":
            initialize_django_debugger()

    settings_module = (
        "saasboilerplate.production"
        if env("VUE_APP_PRODUCTION", default=False)
        else "saasboilerplate.settings"
    )
    env.ENVIRON.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
