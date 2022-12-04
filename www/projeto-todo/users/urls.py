from django.urls import path
from .views import viewUser
from .views import searchId
from .views import newUser
from .views import editUser
from .views import deleteUser

urlpatterns = [
    path("searchid/<int:id>", searchId, name="searchId"),
    path("edituser/<int:id>", editUser, name="editUser"),
    path("deleteuserid/<int:id>", deleteUser, name="deleteUser"),
    path("newuser/", newUser, name="newUser"),
    path("", viewUser, name="viewUser"),
]
