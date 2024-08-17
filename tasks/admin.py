from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "status", "due_date", "user")
    list_filter = ["status"]


admin.site.register(Task, TaskAdmin)
