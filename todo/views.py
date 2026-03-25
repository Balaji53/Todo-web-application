from django.http import HttpResponse
from django.shortcuts import redirect, render

from todo.models import Task

# Create your views here.
def addtask(request):
    t = request.POST.get('task')
    Task.objects.create(task=t)
    return redirect('homepg')
