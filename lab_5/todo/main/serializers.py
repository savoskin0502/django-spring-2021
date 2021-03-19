from rest_framework import serializers
from .models import TodoList, Todo
from auth_.models import MainUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('username', )


class TodoListSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = TodoList
        fields = ('title', 'user')
        depth = 3


class TodoListDetailedSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = TodoList
        fields = '__all__'
        depth = 2


class TodoSerializer(serializers.ModelSerializer):
    task_list = TodoListSerializer(many=False)

    class Meta:
        model = Todo
        fields = ('title', 'created', 'due_on', 'task_list', 'mark')
        depth = 2

#
# class TodoListCompletedSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = TodoList
#         fields = ('title', )
#         depth = 2
