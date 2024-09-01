from django.shortcuts import render

from rest_framework import generics, permissions

from .models import Task
from .serializers import TaskSerializer


class ListCreateTasks(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]


class UpdateDeleteTasks(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]
