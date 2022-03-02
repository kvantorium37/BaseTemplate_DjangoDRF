"""Module for production settings."""

from app.settings.components.rest_framework import REST_FRAMEWORK

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
)
