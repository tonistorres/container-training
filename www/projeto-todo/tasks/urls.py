from django.urls import path
from .views import tasksList

urlpatterns = [path("", tasksList, name="tasksList")]
