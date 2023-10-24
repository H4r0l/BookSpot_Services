from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', #TODO change to mysql
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
