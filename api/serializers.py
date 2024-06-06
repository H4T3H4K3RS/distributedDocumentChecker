from rest_framework import serializers

from api.models import Task


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('file',)


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('status', 'stats',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
