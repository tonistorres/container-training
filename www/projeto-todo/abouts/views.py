from django.shortcuts import render
from django.http import HttpResponse


def aboutTemplate(request):
    return render(request, "abouts/index.html")
