from django.shortcuts import render
from django.http import HttpResponse


def tasksList(request):
    return render(request, "tasks/list.html")
