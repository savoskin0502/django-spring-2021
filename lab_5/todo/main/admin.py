from django.contrib import admin
from .models import TodoList, Todo


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    ordering = ['title']
    search_fields = ['title__contains']
    list_filter = ['title']


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'due_on', 'get_owner', 'mark',
                    'get_parent_name']
    ordering = ['mark', '-created', 'due_on']
    search_fields = ['title', 'mark']
    list_filter = ['title', 'due_on', 'mark', 'task_list']

    def get_parent_name(self, obj):
        return obj.task_list.title
    get_parent_name.short_description = 'Parent'
    get_parent_name.admin_order_field = 'task_list__title'

    def get_owner(self, obj):
        return obj.task_list.user.username
    get_owner.short_description = 'Owner'
    get_owner.admin_order_field = 'get_owner'
