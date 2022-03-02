from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

import tasks.api.serializers as tasks_serializers
from tasks.models import Task


class TasksViewSet(viewsets.ModelViewSet):
    """Tasks viewset."""

    queryset = Task.objects.all()

    serializer_class = tasks_serializers.TaskSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'options']

    @action(
        detail=False,
        methods=['get'],
        serializer_class=tasks_serializers.TaskSerializer,
    )  # type: ignore
    def user(self, request: Request):
        """Action to get current user's tasks."""
        tasks = Task.objects.filter(owner=request.user)

        serializer = self.get_serializer(tasks, many=True)

        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """Users viewset."""

    queryset = get_user_model().objects.all().order_by('id')

    serializer_class = tasks_serializers.UserSerializer
    http_method_names = ['get', 'options']
