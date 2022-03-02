from app.settings import env
from app.settings.components.base import DEBUG
from app.settings.components.installed_apps import INSTALLED_APPS
from app.settings.components.middleware import MIDDLEWARE

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INSTALLED_APPS += ['debug_toolbar']
DISABLE_DEBUG_TOOLBAR = env.bool('DISABLE_DEBUG_TOOLBAR', default=False)


def custom_show_toolbar(request):
    """Only show the debug toolbar to users with the superuser flag."""
    return DEBUG and request.user.is_superuser and not DISABLE_DEBUG_TOOLBAR


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': (
        'app.settings.environments.development.custom_show_toolbar'
    ),
}
