
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


@pytest.fixture
def user_task(mixer, api_client):
    return mixer.blend(
        'tasks.Task',
        owner_id=api_client.user.id,
    )


@pytest.fixture
def another_user(mixer):
    return mixer.blend(get_user_model())


@pytest.fixture
def another_task(mixer, another_user):
    return mixer.blend(
        'tasks.Task',
        owner=another_user,
    )
