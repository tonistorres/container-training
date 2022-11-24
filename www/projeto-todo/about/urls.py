from django.urls import path
from .views import view_about

urlpatterns = [path("", view_about, name="view_about")]
