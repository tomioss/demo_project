from rest_framework import serializers

from app.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'user', 'is_done', 'created_at', 'updated_at']

