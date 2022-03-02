# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    'corsheaders',  # https://github.com/adamchainz/django-cors-headers
    'drf_yasg',  # https://github.com/axnsan12/drf-yasg
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',

    # apps
]
