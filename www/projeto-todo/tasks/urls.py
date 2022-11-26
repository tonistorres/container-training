from django.urls import path
from .views import tasksList
from .views import yourName
from .views import taskView
from .views import newTask

# Neste arquivo fica todas as assinaturas dos métodos
# bem como todos os caminhos de acesso a view
urlpatterns = [
    path("", tasksList, name="tasksList"),
    path("yourname/<str:name>", yourName, name="yourName"),
    path("task/<int:id>", taskView, name="taskView"),
    path("newtask/", newTask, name="newTask"),
]
