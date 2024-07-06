from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.http import require_http_methods
from .models import Task
from .forms import TaskForm

@require_http_methods(["GET"])
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@require_http_methods(["GET"])
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

@require_http_methods(["GET", "POST"])
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f"Task '{task.name}' was created successfully!")
            return redirect(reverse('task-list'))
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@require_http_methods(["GET", "POST"])
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            messages.success(request, f"Task '{task.name}' was updated successfully!")
            return redirect(reverse('task-list'))
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@require_http_methods(["GET", "POST"])
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task_name = task.name
        task.delete()
        messages.success(request, f"Task '{task_name}' was deleted successfully!")
        return redirect(reverse('task-list'))
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
