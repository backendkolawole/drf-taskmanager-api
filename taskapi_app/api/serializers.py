from rest_framework import serializers
from taskapi_app.models import Task



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ['name', 'completed']
        exclude = ['owner']
