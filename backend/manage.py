#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ

env = environ.Env()

def main():
    """Run administrative tasks."""
    
    if "WEBSITE_HOSTNAME" not in env.ENVIRON:
        environ.Env.read_env('.env.development')
        environ.Env.read_env('.env.local', overwrite=True)

    settings_module = (
        "saasboilerplate.production"
        if "WEBSITE_HOSTNAME" in env.ENVIRON
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
