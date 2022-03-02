import pytest
from rest_framework import status

pytestmark = [pytest.mark.django_db]


def test_users_list_anon(anon_api_client):
    anon_api_client.get(
        '/api/v1/tasks/users/',
        expected_status_code=status.HTTP_401_UNAUTHORIZED,
    )


def test_users_list(api_client):
    response = api_client.get('/api/v1/tasks/users/')['results'][0]

    assert response['id'] == api_client.user.id
    assert response['tasks'] == []
