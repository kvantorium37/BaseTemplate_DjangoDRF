from django.urls import reverse


def test_homepage(anon_api_client):
    """Test ensures that homepage is accessible."""
    anon_api_client.get(reverse('homepage'))


def test_swagger_is_accessible(anon_api_client):
    """Test swagger homepage is accessible."""
    anon_api_client.get('/api/v1/swagger/?format=openapi')
