from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Task serializer."""

    class Meta:
        model = Task
        fields = [
            'id',
            'owner',
            'summary',
            'body',
        ]
