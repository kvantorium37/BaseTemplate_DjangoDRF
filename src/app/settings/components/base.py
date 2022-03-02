import sys
from pathlib import Path

from app.settings import env

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

IS_PYTEST_RUNNING = (
    'pytest' in sys.argv[0]
    or 'py.test' in sys.argv[0]
    or 'py/test' in sys.argv[0]
)
RUNNING_TESTS = IS_PYTEST_RUNNING
