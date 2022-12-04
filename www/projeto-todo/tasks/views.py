from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from .filters import TaskFilter
from django.contrib import messages


def tasksList(request):
    tasks_list = Task.objects.all()
    paginator = Paginator(tasks_list, 8)
    page = request.GET.get("page")
    tasks = paginator.get_page(page)
    return render(request, "tasks/list.html", {"tasks": tasks})


# https://www.youtube.com/watch?v=rzyoT2ZDy1c
def newTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = "doing"
            task.save()
            return redirect("/")
    else:
        form = TaskForm()
        return render(request, "tasks/addtask.html")


def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, "tasks/task.html", {"task": task})


# https://www.youtube.com/watch?v=npaSyVGE93g&list=PLnDvRpP8BnewqnMzRnBT5LeTpld5bMvsj&index=11
def editTask(request, id):

    tasks = Task.objects.all()
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect("/")
        else:
            return render(request, "tasks/edittask.html", context)
    else:
        print("Esout no GET DEU BOM !!")
        context = {
            "task": task,
            "tasks": tasks,
            "form": form,
        }
        return render(request, "tasks/edittask.html", context)


def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, "Task deleted success.")
    return redirect("/")


def tasks_list_filtered(request):
    tasks = Task.objects.all()
    f = TaskFilter(request.GET, queryset=tasks)
    paginator = Paginator(tasks, 8)
    page = request.GET.get("page")
    tasks = paginator.get_page(page)

    return render(request, "tasks/list.html", {"filter": f, "tasks": tasks})
