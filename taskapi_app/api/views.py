from rest_framework.permissions import IsAuthenticated
from taskapi_app.api.serializers import TaskSerializer
from rest_framework import generics
from taskapi_app.models import Task
from django.conf import settings
from django.db import models
User = settings.AUTH_USER_MODEL

# from rest_framework.permissions import IsAdminUser



class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        """
        This view should return a list of all the Tasks
        for the currently authenticated user.
        """
        owner = self.request.user
        return Task.objects.filter(owner=owner)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """
        This view should return a list of all the Tasks
        for the currently authenticated user.
        """
        owner = self.request.user
        return Task.objects.filter(owner=owner)