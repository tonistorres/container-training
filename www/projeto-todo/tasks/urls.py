from django.urls import path
from .views import tasksList
from .views import taskView
from .views import newTask


urlpatterns = [
    path("", tasksList, name="tasksList"),
    path("task/<int:id>", taskView, name="taskView"),
    path("newtask/", newTask, name="newTask"),
]
