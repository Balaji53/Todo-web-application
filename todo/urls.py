from  django.urls import path
from . import views

urlpatterns = [
    # Add Task button
    path('addtask', views.addtask, name='addtask'),

    #mark as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done')
    
]