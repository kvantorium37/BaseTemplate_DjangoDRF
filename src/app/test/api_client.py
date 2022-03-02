# flake8: noqa
# type: ignore
# Based on DRFClient from https://github.com/f213/django

import json
import random
import string

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class DRFClient(APIClient):
    """DRF Api client to use in tests."""

    def __init__(
        self, mixer, anon=False, *args, **kwargs,
    ):
        """Initialize of API client."""
        super().__init__(*args, **kwargs)
        self.mixer = mixer
        if not anon:
            self.auth()

    def auth(self) -> None:
        """Authenticate test user."""
        self.user = self._create_user()

        refresh = RefreshToken.for_user(self.user)

        self.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def _create_user(self):
        """Create test user."""
        user = self.mixer.blend(
            'users.User', is_active=True, phone='+79012345678',
        )
        random_chars = [random.choice(string.hexdigits) for _ in range(0, 6)]  # noqa: S311
        self.password = ''.join(random_chars)
        user.set_password(self.password)
        user.save()

        return user

    def get(self, *args, **kwargs):
        return self._api_call('get', kwargs.get('expected_status_code', status.HTTP_200_OK), *args, **kwargs)

    def post(self, *args, **kwargs):
        return self._api_call('post', kwargs.get('expected_status_code', status.HTTP_201_CREATED), *args, **kwargs)

    def put(self, *args, **kwargs):
        return self._api_call('put', kwargs.get('expected_status_code', status.HTTP_200_OK), *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self._api_call('delete', kwargs.get('expected_status_code', status.HTTP_204_NO_CONTENT), *args, **kwargs)

    def _api_call(self, method, expected, *args, **kwargs):
        kwargs['format'] = kwargs.get('format', 'json')  # by default submit all data in JSON
        as_response = kwargs.pop('as_response', False)

        method = getattr(super(), method)
        response = method(*args, **kwargs)

        if as_response:
            return response

        content = self._decode(response)

        assert response.status_code == expected, content

        return content

    def _decode(self, response):
        if not len(response.content):
            return

        content = response.content.decode('utf-8', errors='ignore')
        if response.headers['content-type'] == 'application/json':
            return json.loads(content)
        else:
            return content
