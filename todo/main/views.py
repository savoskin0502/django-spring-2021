from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import json
import random
# Create your views here.

tasks_filename = 'tasks.json'
dataset = None


def load_tasks(filename):
    with open(filename) as f:
        return json.loads(f.read())


def check_dataset():
    global dataset
    if dataset is None:
        dataset = load_tasks(tasks_filename)


def get_todo_list(request):
    check_dataset()
    tasks_list = random.choice(list(dataset.keys()))
    context = get_context(header_name='Tasks',
                          tasks_list_name=tasks_list,
                          tasks=dataset.get(tasks_list))
    return render(request, 'todo_list.html', context=context)


def get_completed_tasks(request, **kwargs):
    check_dataset()
    context = get_context(header_name='Completed Tasks',
                          tasks_list_name=kwargs.get('pk'),
                          tasks=list(filter(lambda x: x.get('mark') is True,
                                  dataset.get(kwargs.get('pk')))))
    return render(request, 'todo_list.html', context=context)


def get_context(header_name, tasks_list_name, tasks):
    return {
        'header_name': header_name,
        'tasks_list_name': tasks_list_name,
        'tasks': tasks
    }
