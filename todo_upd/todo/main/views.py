from django.shortcuts import render
from .models import TaskList


def get_todo_list(request):
    todo = get_todo(pk=1)
    context = form_context(
        header_name='Tasks',
        tasks_list_name=todo.title,
        tasks=todo.tasks.all()
    )
    return render(request, 'todo_list.html', context=context)


def get_completed_tasks(request, pk):
    todo = get_todo(pk=pk)
    context = form_context(
        header_name='Completed tasks',
        tasks_list_name=todo.title,
        tasks=todo.tasks.filter(mark__exact=True)
    )
    return render(request, 'todo_list.html', context=context)


def get_todo(pk):
    return TaskList.objects.get(pk=pk)


def form_context(header_name, tasks_list_name, tasks):
    return dict({
        'header_name': header_name,
        'tasks_list_name': tasks_list_name,
        'tasks': tasks
    })
