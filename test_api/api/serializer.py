from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор Task"""
    class Meta:
        fields = ('id', 'title', 'description', 'completed', 'created_at')
        model = Task
