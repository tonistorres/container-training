from django.urls import path
from .views import viewUser

urlpatterns = [path("", viewUser, name="viewUser")]
