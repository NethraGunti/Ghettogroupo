from django.shortcuts import render, redirect
from django.http import HttpResponse

from users.models import User
from django.contrib.auth.decorators import login_required

from ToDo.models import Todo
from ToDo.forms import TaskForm

# Create your views here.
@login_required(login_url='login')
def index(request):
    tasks = Todo.objects.filter(user=request.user).order_by('-id')

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(form)
        if form.is_valid():
            print('her')
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
        else:
            print('ajsdbnwijndwjsndjnjxndaqwndoiw0-0000000000000000000000000000')
        return redirect('list')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'ToDo/list_todo.html', context)

@login_required(login_url='login')
def updateTodo(request, pk):
    task = Todo.objects.get(id=pk, user=request.user)

    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')  

    context = {'form':form}

    return render(request, 'ToDo/update_todo.html', context)

@login_required
def deleteTodo(request, pk):
    item = Todo.objects.get(id=pk, user=request.user)

    if request.method == 'POST':
        item.delete()
        return redirect('list') 

    context = {'item':item}
    return render(request, 'ToDo/delete_todo.html',context)