from django.shortcuts import render
from django.http import HttpResponse


def view_about(request):
    return render(request, "about/index.html")
