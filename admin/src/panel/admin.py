"""Настройки интерфеса администратора."""
from django.contrib import admin

from panel import models


@admin.register(models.Template)
class TemplatesAdmin(admin.ModelAdmin):
    """Интерфейс администратора для модели Template."""

    pass


@admin.register(models.Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    """Интерфейс администратора для модели Task."""

    pass
