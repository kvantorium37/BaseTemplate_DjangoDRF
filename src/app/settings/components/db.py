# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

from app.settings import env

DATABASES = {
    'default': env.db(),
}
