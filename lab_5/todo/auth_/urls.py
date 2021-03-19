from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path(r'', obtain_jwt_token),
]
