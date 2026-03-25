from django.contrib import admin

# Register your models here.
from .models import Task


class Taskadmin(admin.ModelAdmin):
    
    list_display =('task','is_completed','updated_at')
    


admin.site.register(Task, Taskadmin)
