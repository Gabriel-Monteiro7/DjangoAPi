from django.shortcuts import render

from rest_framework import viewsets, permissions

from .models import Task
from .serializers import TaskSerializer

from rest_framework.response import Response


class TaskViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def list(self, request):
        queryset = Task.objects.all().filter(user=request.user.id)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
