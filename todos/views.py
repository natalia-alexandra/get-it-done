from django.shortcuts import redirect, render
from .models import Todos
from .forms import TodoForm


# def index(request):
#     return render(request, 'index.html')


def todo_list(request):
    tasks = Todos.objects.all()

    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()

    # return render(request, 'todo-list.html', {'tasks': tasks, 'form': form})
    return render(request, 'index.html', {'tasks': tasks, 'form': form})


def delete_item(req, pk):
    task = Todos.objects.get(id=pk)
    task.delete()
    return redirect('/')


def update_item(request, pk):
    todo = Todos.objects.get(id=pk)
    updateForm = TodoForm(instance=todo)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance=todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('/')
    return render(request, 'edit.html', {'todo': todo, 'updateForm': updateForm})
