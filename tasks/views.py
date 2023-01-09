from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.


def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)


def add(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Todo.objects.create(task=task)

        return redirect('index')
    else:
        return render(request, 'tasks/add.html')


def delete(request, id):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect('index')


def search(request):
    search_term = request.GET.get('search-term') or ''
    tasks = Todo.objects.filter(task__icontains=search_term) #
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)


def update(request, id):
    task = Todo.objects.get(id=id)

    form = TodoForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()

        return redirect('index')

    return render(request, 'tasks/update.html', {'form': form, 'task': task})
