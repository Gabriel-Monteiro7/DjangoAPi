from django.shortcuts import render
from rest_framework import viewsets, permissions, status, mixins
from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response


class TaskViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request):
        queryset = Task.objects.all().filter(user=request.user.id)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        print(request.data)
        request.data['user'] = request.user.id
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = Task.objects.all().filter(user=request.user.id)
        task = get_object_or_404(queryset, pk=pk)
        request.data['user'] = request.user.id
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Task.objects.all().filter(user=request.user.id)
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def destroy(self, request, pk, format=None):
        queryset = Task.objects.all().filter(user=request.user.id)
        task = get_object_or_404(queryset, pk=pk)
        if(task.user.id == request.user.id):
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
