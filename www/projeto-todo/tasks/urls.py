from django.urls import path
from .views import tasks_initial

urlpatterns = [path("", tasks_initial, name="tasks_initial")]
