from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.contrib import messages


def viewUser(request):
    users = User.objects.all()
    return render(request, "users/list.html", {"users": users})


# https://www.youtube.com/watch?v=rzyoT2ZDy1c
def newUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("/user")
    else:
        form = UserForm()
        return render(request, "users/adduser.html")


def searchId(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, "users/searchid.html", {"user": user})


# https://www.youtube.com/watch?v=npaSyVGE93g&list=PLnDvRpP8BnewqnMzRnBT5LeTpld5bMvsj&index=11
def editUser(request, id):

    users = User.objects.all()
    user = get_object_or_404(User, pk=id)
    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user.save()
            return redirect("/user")
        else:
            return render(request, "users/edituser.html", context)
    else:
        context = {
            "task": user,
            "tasks": users,
            "form": form,
        }
        return render(request, "users/edituser.html", context)


def deleteUser(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    messages.info(request, "User deleted success.")
    return redirect("/user")
