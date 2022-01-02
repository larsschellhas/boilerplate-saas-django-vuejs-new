from .settings import *
import environ

env = environ.Env()

### Activate live mode & disable debug
DEBUG = False
STRIPE_LIVE_MODE = True


### Security related settings for production
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

### WhiteNoise configuration for serving static files
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


### Database settings
# Set database connection lifetime to one day to reduce reconnects
CONN_MAX_AGE = 86400
