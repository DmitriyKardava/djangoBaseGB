import os
from .settings import *
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'braniac',
        'USER': 'braniac',
        'PASSWORD': 'masterkey',
	'HOST': 'postgres',
	'PORT': 5432,
    }
}
del STATICFILES_DIRS
STATIC_ROOT = BASE_DIR / "static"