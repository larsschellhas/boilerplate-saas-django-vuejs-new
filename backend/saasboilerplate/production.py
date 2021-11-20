from .settings import *
import environ

env = environ.Env()

# Sets django and dj-stripe to run in live mode
DEBUG = False
STRIPE_LIVE_MODE = True

# WhiteNoise configuration
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# DBHOST is only the server name, not the full URL
dbhostname = env("DBHOST")

# Configure Postgres database; the full username is username@servername,
# which we construct using the DBHOST value.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DBNAME"),
        "HOST": dbhostname + ".postgres.database.azure.com",
        "USER": env("DBUSER") + "@" + dbhostname,
        "PASSWORD": env("DBPASS"),
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
