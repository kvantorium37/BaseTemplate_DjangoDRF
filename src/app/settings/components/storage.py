from pathlib import Path

from app.settings import env
from app.settings.components.base import BASE_DIR, RUNNING_TESTS

MEDIA_ROOT = Path.joinpath(Path(BASE_DIR).parent, 'media')
MEDIA_URL = '/media/'

USE_CLOUD_STORAGE = env.bool('USE_CLOUD_STORAGE', default=False)

if USE_CLOUD_STORAGE:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

if RUNNING_TESTS:
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'
