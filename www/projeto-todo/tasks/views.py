from django.shortcuts import render
from django.http import HttpResponse


def tasks_initial(request):
    return HttpResponse("Hello World Task Install")
