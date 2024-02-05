from django.shortcuts import render, redirect, get_object_or_404

from app.models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks},)


def add_task(request):
    if request.method == 'POST':
        Task.objects.create(name=request.POST.get('task'))
        return redirect('index')

    return render(request, 'error.html')


def edit_task(request, id):
    task = get_object_or_404(Task, pk = id)

    if request.method == 'POST':
        task.name = request.POST.get('task')
        task.save()
        return redirect('index')

    return render(request, 'edit.html', context={'task': task},)


def delete_task(request, id):
    task = get_object_or_404(Task, pk = id)
    task.delete()

    return redirect('index')


def toggle_task(request, id):
    task = get_object_or_404(Task, pk = id)

    if not task.is_done:
        task.is_done = True
    else:
        task.is_done = False
    task.save()

    return redirect('index')
