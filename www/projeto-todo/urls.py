from django.urls import path
from .views import here_name_view

urlpatterns = [path("", here_name_view, name="here_name_view")]

