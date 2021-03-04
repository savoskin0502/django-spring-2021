from django.contrib import admin
from .models import TaskList, Task
# Register your models here.


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']
    search_fields = ['title__contains']
    list_filter = ['title']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'due_on', 'owner', 'mark', 'task_list']
    ordering = ['mark', '-created', 'due_on']
    search_fields = ['title', 'mark']
    list_filter = ['title', 'due_on', 'mark', 'task_list']
