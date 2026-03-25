from django.http import HttpResponse
from django.shortcuts import redirect, render

from todo.models import Task

# Create your views here.
def addtask(request):
    t = request.POST.get('task')
    Task.objects.create(task=t)
    return redirect('homepg')

def mark_as_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('homepg')

def mark_as_undone(request,pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = False
    task.save()
    return redirect('homepg')

def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        new_task = request.POST.get('task')
        task.task = new_task
        task.save()
        return redirect('homepg')
    context = {
        'task': task
    }
    return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()   
    return redirect('homepg')