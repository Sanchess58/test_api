from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Task
from .serializer import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Класс обеспечивающий весь CRUD."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('completed',)