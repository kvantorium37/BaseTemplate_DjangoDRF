import pytest
from rest_framework import status

from tasks.models import Task

pytestmark = [pytest.mark.django_db]


def test_tasks_list_anon(anon_api_client):
    anon_api_client.get(
        '/api/v1/tasks/',
        expected_status_code=status.HTTP_401_UNAUTHORIZED,
    )


def test_tasks_list(api_client, task):
    response = api_client.get('/api/v1/tasks/')['results'][0]

    assert response['id'] == task.id
    assert response['summary'] == task.summary
    assert response['body'] == task.body


def test_task_create(api_client, user):
    response = api_client.post(
        '/api/v1/tasks/',
        data={
            'owner': user.id,
            'summary': 'Hello, world.',
            'body': 'Test task.',
        },
    )

    assert response['owner'] == user.id
    assert response['summary'] == 'Hello, world.'
    assert response['body'] == 'Test task.'


def test_task_update(api_client, user, task):
    response = api_client.put(
        f'/api/v1/tasks/{task.id}/',
        data={
            'owner': user.id,
            'summary': 'Hello, world.',
            'body': 'Test task.',
        },
    )

    assert response['id'] == task.id
    assert response['owner'] == user.id
    assert response['summary'] == 'Hello, world.'
    assert response['body'] == 'Test task.'


def test_task_delete(api_client, task):
    api_client.delete(f'/api/v1/tasks/{task.id}/')

    assert not Task.objects.exists()
