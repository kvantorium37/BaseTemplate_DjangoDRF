# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
from django.utils.translation import gettext_lazy as _

LANGUAGES = [
    ('en-EN', _('English')),
    ('ru-RU', _('Russian')),
]

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
