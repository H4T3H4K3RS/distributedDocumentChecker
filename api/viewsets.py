from rest_batteries.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from api.models import Task
from api.paginators import StandardResultsSetPagination
from api.serializers import TaskSerializer, TaskCreateSerializer, TaskUpdateSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = StandardResultsSetPagination

    action_permission_classes = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'create': [AllowAny],
        'update': [AllowAny],
        'partial_update': [AllowAny],
        'destroy': [AllowAny],
    }

    request_action_serializer_classes = {
        'create': TaskCreateSerializer,
        'update': TaskUpdateSerializer,
        'partial_update': TaskUpdateSerializer,
    }

    response_action_serializer_classes = {
        'list': TaskSerializer,
        'retrieve': TaskSerializer,
        'create': TaskSerializer,
        'update': TaskSerializer,
        'partial_update': TaskSerializer,
        'destroy': TaskSerializer,
    }

