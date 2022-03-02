import pytest

pytestmark = [pytest.mark.django_db]


def test_user_tasks_list(api_client, user_task, another_task):
    response = api_client.get('/api/v1/tasks/user/')

    assert len(response) == 1
    assert response[0]['id'] == user_task.id
    assert response[0]['summary'] == user_task.summary
    assert response[0]['body'] == user_task.body
