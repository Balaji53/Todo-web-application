from django.http import HttpResponse
from django.shortcuts import redirect, render

from todo.models import Task

# Create your views here.
def addtask(request):
    t = request.POST.get('data')
    Task.objects.create(task=t)
    return redirect('homepg')

def mark_as_done(request, task_id):
    task_obj = Task.objects.get(pk=task_id)
    task_obj.is_completed = True
    task_obj.save()
    return redirect('homepg')

def mark_as_undone(request, task_id):
    task_obj = Task.objects.get(pk=task_id)
    task_obj.is_completed = False
    task_obj.save()
    return redirect('homepg')

def edit_task(request, task_id):
    task_obj = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        new_task = request.POST.get('task')
        task_obj.task = new_task
        task_obj.save()
        return redirect('homepg')
    context = {
        'task': task_obj
    }
    return render(request, 'edit_task.html', context)

def delete_task(request, task_id):
    task_obj = Task.objects.get(pk=task_id)
    task_obj.delete()   
    return redirect('homepg')