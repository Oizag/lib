from .base import *

# SECURITY WARNING: don't run with debug turned on in production!

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "django-insecure-fhzr*ucvvx+4*w_d_bgf7opow4tpwijhm$&fn4e+og7g2p(x94"
)

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
