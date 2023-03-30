from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def index (request):
    todo = Todo.objects.all()
    context = {
        'todo':todo
    }
    return render (request, 'index.html', context)

def detail (request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todos':todo
    }
    return render (request, 'detail.html', context)

def new (request):
    return render (request, 'new.html')

def create (request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    todo = Todo(title=title, content=content)
    todo.save()
    return redirect('todo:index')

def delete (request, pk):
    todos = Todo.objects.get(pk=pk)
    todos.delete()
    return redirect('todo:index')

def edit (request, pk):
    todos = Todo.objects.get(pk=pk)
    context = {
        'todos':todos
    }
    return render(request, 'edit.html', context)

def update (request, pk):
    todos = Todo.objects.get(pk=pk)
    todos.title = request.POST.get('title')
    todos.content = request.POST.get('content')
    todos.save()

    return redirect('todo:detail', todos.pk)