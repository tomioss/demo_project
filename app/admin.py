from django.contrib import admin
from app.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_done', 'created_at', 'updated_at')

admin.site.register(Task, TaskAdmin)
