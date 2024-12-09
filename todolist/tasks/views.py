from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        Task.objects.create(description=description)
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')


def delete_task(request, task_id):
    # Get task by ID or 404 if not found
    task = get_object_or_404(Task, id=task_id)
    # Delete the task
    task.delete()
    # Redirect back to task list
    return redirect('task_list')
