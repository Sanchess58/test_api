from django.db import models


class Task(models.Model):
    """Класс модели Task"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)