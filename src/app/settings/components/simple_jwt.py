from datetime import timedelta

from app.settings import env

# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html

ACCESS_TOKEN_LIFETIME_MINUTES = timedelta(
    minutes=env('ACCESS_TOKEN_LIFETIME_MINUTES', default=0),
)

ACCESS_TOKEN_LIFETIME_DAYS = timedelta(
    days=env('ACCESS_TOKEN_LIFETIME_DAYS', default=1),
)

ACCESS_TOKEN_LIFETIME = (
    ACCESS_TOKEN_LIFETIME_MINUTES
    or ACCESS_TOKEN_LIFETIME_DAYS
)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': ACCESS_TOKEN_LIFETIME,
    'REFRESH_TOKEN_LIFETIME': timedelta(
        days=env('REFRESH_TOKEN_LIFETIME_DAYS', default=7 * 2),  # two weeks
    ),
    'ROTATE_REFRESH_TOKENS': True,
    'UPDATE_LAST_LOGIN': True,
}
