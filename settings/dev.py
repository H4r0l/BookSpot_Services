from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', #TODO change to mysql
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',  # Ejemplo: Puedes reemplazar con tu frontend
    # Agrega más orígenes si es necesario
]

