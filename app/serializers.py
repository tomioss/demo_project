from rest_framework import serializers

from app.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'is_done', 'created_at', 'updated_at']
