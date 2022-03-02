# type: ignore

import pytest
from mixer.backend.django import mixer as _mixer

from app.test.api_client import DRFClient


@pytest.fixture
def mixer():
    return _mixer


@pytest.fixture
def api_client(mixer):
    """DRF API client."""
    return DRFClient(mixer)


@pytest.fixture
def anon_api_client(mixer):
    """Anonymous DRF API client."""
    return DRFClient(mixer, anon=True)
