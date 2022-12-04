from django.urls import path
from .views import tasksList
from .views import taskView
from .views import newTask
from .views import editTask
from .views import deleteTask
from .views import tasks_list_filtered


urlpatterns = [
    path("", tasks_list_filtered, name="tasks_list_filtered"),
    path("task/<int:id>", taskView, name="taskView"),
    path("edit/<int:id>", editTask, name="editTask"),
    path("delete/<int:id>", deleteTask, name="deleteTask"),
    path("newtask/", newTask, name="newTask"),
    # path("", tasksList, name="tasksList"),
]
