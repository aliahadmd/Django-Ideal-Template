from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tasks.models import Task
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    fields = ['name', 'description']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')
    success_message = "Task '%(name)s' was created successfully"

class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    fields = ['name', 'description']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')
    success_message = "Task '%(name)s' was updated successfully"

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

    def get_success_url(self):
        messages.success(self.request, f"Task '{self.object.name}' was deleted successfully!")
        return super().get_success_url()


