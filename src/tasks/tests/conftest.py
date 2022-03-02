
from django.contrib.auth import get_user_model

import pytest


@pytest.fixture
def user(mixer):
    return mixer.blend(get_user_model())


@pytest.fixture
def task(mixer, user):
    return mixer.blend(
        'tasks.Task',
        owner=user,
    )
