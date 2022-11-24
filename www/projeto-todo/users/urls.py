from django.urls import path
from .views import view_users

urlpatterns = [path("", view_users, name="view_users")]
