from  django.urls import path
from . import views

urlpatterns = [
    # Add Task button
    path('addtask', views.addtask, name='addtask'),

    #mark as done
    path('mark_as_done/<int:task_id>/', views.mark_as_done, name ='mark_as_done'),
    #mark as undone
    path('mark_as_undone/<int:task_id>/', views.mark_as_undone, name='mark_as_undone'),

    #edit task
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),

    #delete task
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),]