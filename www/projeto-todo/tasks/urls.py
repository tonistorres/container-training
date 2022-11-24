from django.urls import path
from .views import tasksList
from .views import yourName


urlpatterns = [
    path("", tasksList, name="tasksList"),
    path("yourname/<str:name>", yourName, name="yourName"),
]
