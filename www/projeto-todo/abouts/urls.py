from django.urls import path
from .views import aboutTemplate

urlpatterns = [
    path("", aboutTemplate, name="aboutTemplate"),
]
