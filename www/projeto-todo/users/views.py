from django.shortcuts import render
from django.http import HttpResponse


def view_users(request):
    return HttpResponse("Hello World View Users")
