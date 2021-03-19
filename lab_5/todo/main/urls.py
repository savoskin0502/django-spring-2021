from django.urls import path, include
from rest_framework import routers

from .views import TodoListViewSet, TodoListDetailedViewSet

router = routers.SimpleRouter()
router.register(r'', TodoListViewSet, basename='main')
# router.register(r'', TodoViewSet, basename='main')

urlpatterns = [
    path('todos/<int:pk>/completed/', TodoListDetailedViewSet.as_view({
        'get': 'get_completed'
    }))
]
urlpatterns += router.urls
print('routes', router.urls, urlpatterns)
