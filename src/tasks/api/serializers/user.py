from django.contrib.auth import get_user_model

from rest_framework import serializers

from tasks.api.serializers import TaskSerializer


class UserSerializer(serializers.ModelSerializer):
    """Task serializer."""

    tasks = TaskSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'tasks',
        ]
