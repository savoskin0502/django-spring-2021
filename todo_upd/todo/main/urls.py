from django.urls import path
from .views import get_todo_list, get_completed_tasks


urlpatterns = [
    path('', get_todo_list),
    path('<int:pk>/completed/', get_completed_tasks)
]
