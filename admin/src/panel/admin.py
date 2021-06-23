from django.contrib import admin

from panel import models


@admin.register(models.Template)
class TemplatesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Task)
class TasksAdmin(admin.ModelAdmin):
    pass
