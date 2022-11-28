from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def viewUser(request):
    users = User.objects.all()
    return render(request, "users/list.html", {"users": users})
