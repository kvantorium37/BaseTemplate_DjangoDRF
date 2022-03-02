from pathlib import PurePath

import environ
from split_settings.tools import include

ENVFILE_PATH = PurePath.joinpath(PurePath(__file__).parent, '.env')

env = environ.Env(
    DEBUG=(bool, False),
    DJANGO_ENV=(str, 'development'),
)
environ.Env.read_env(str(ENVFILE_PATH))

ENV = env.str('DJANGO_ENV')

include(
    'components/base.py',
    'components/auth.py',
    'components/cors.py',
    'components/db.py',
    'components/i18n.py',
    'components/installed_apps.py',
    'components/logging.py',
    'components/middleware.py',
    'components/rest_framework.py',
    'components/templates.py',
    'components/simple_jwt.py',
    'components/static.py',
    'components/storage.py',

    f'environments/{ENV}.py',
)
