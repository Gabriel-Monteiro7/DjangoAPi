from django.contrib import admin

from .models import Task

@admin.register
class TaskAdmin(Task):
    list_display = {'name', 'deadline', 'priority',
                    'description', 'completed', 'created_at', 'updated_at'}
