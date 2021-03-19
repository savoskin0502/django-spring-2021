from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import TodoList, Todo
from .serializers import TodoListSerializer, TodoListDetailedSerializer, TodoSerializer


class TodoListViewSet(viewsets.ViewSet):
    # serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return TodoList.objects.all()

    @action(methods=['GET'], detail=False, url_path='todos')
    def get_todos(self, request):
        print(self.get_queryset())
        serializer = TodoListDetailedSerializer(self.get_queryset(), many=True)
        print(serializer.data)
        return Response(serializer.data)


class TodoListDetailedViewSet(viewsets.ViewSet):
    # serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk):
        return Todo.objects.filter(task_list__id=pk).filter(mark=False)

    @action(methods=['GET'], detail=True, url_path='completed')
    def get_completed(self, request, pk):
        serializer = TodoSerializer(self.get_queryset(pk), many=True)
        return Response(serializer.data)
