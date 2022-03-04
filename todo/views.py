from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TodoForm, CreateUser
from .models import Todo
from django.contrib import messages

from django.contrib.auth import login, logout, authenticate


def todo_list(request):
    if not request.user.is_authenticated:

        return redirect('/login')
    print(request.user)
    todos = Todo.objects.all()

    print(todos)
    context = {
        'todo_list':todos
    }
    return render(request, 'todo/todo_list.html', context)


def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo':todo
    }
    return render(request, 'todo/todo_detail.html', context)

# Create your views here.


def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Todo created')
        return redirect('/')

    context = {
        "form":form
    }

    return render(request, 'todo/todo_create.html', context)


def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        "form":form,
        'id':id
    }

    return render(request, 'todo/todo_update.html', context)


def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')


def register(request):
    form = CreateUser()

    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = { 'form': form}
    return render(request, 'todo/register.html', context)


def loginup(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        messages.error(request, 'Enter correct user name and password')

    return render(request, 'todo/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('/login')