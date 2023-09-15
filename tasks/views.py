from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from .models import Tasks
from .forms import TasksForm


# Create your views here.
@login_required
def tasks(request):
    search_query = request.GET.get('search', '')
    important_choice = request.GET.get('important_choice', '')
    completed_choice = request.GET.get('completed_choice', '')
    tasks_list = Tasks.objects.all()

    if search_query:
        tasks_list = tasks_list.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    if important_choice == '1':
        tasks_list = tasks_list.filter(important=True)
    elif important_choice == '0':
        tasks_list = tasks_list.filter(important=False)

    if completed_choice == '1':
        tasks_list = tasks_list.filter(completed=True)
    elif completed_choice == '0':
        tasks_list = tasks_list.filter(completed=False)

    context = {
        'tasks_list': tasks_list,
        'search_query': search_query
    }

    return render(request, 'tasks/tasks.html', context)


@login_required
def add_tasks(request):
    if request.method == 'POST':
        tasks_form = TasksForm(request.POST)
        if tasks_form.is_valid():
            tasks = tasks_form.save(commit=False)
            tasks.user = request.user
            tasks.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('tasks')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        tasks_form = TasksForm()

    return render(request, 'tasks/add_tasks.html', {
        'tasks_form': tasks_form
    })


@login_required
def delete_task(request, id):
    task = get_object_or_404(Tasks, pk=id)
    print(task)

    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            task.delete()
            messages.success(
                request, '¡Los datos se han borrado exitosamente!'
            )
            return redirect('tasks')
        else:
            messages.error(
                request, 'La acción de eliminación no se ha confirmado.'
            )
            return redirect('tasks')

    context = {'task': task}
    return render(request, 'tasks/tasks_delete_conf.html', context)


@login_required
def update_task(request, id):
    task = get_object_or_404(Tasks, pk=id)
    task_form = TasksForm(instance=task)

    if request.method == 'POST':
        task_form = TasksForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('tasks')
        else:
            for field, errors in task_form.errors.items():
                for error in errors:
                    messages.error(
                        request, f'Error en el campo {field}: {error}'
                    )
    else:
        task_form = TasksForm(instance=task)

    context = {'task_form': task_form, 'task': task}

    return render(request, 'tasks/tasks.html', context)


@login_required
def complete_task(request, id):
    task = get_object_or_404(Tasks, pk=id)
    if request.method == 'POST':
        task.completed = timezone.now()
        task.save()
        return redirect('tasks')
