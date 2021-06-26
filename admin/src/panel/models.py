from enum import Enum

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone


class TemplateCodes(models.TextChoices):
    welcome_letter = "welcome_letter", "Приветственное письмо"
    selection_movies = "selection_movies", "Подборка фильмов"
    personal_newsletter = "personal_newsletter", "Персональная рассылка фильмов"


class Template(models.Model):
    title = models.CharField("Наименование", max_length=250)
    code = models.CharField(choices=TemplateCodes.choices, max_length=50)
    html = models.TextField()
    subject = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'email_templates'


class Task(models.Model):
    class NotificationStatuses(str, Enum):
        to_send = "to_send"
        in_process = "in_process"
        done = "done"
        cancelled = "cancelled"
        failed = "failed"

    NOTIFICATION_STATUSES = (
        (NotificationStatuses.to_send, "to_send"),
        (NotificationStatuses.in_process, "in_process"),
        (NotificationStatuses.done, "done"),
        (NotificationStatuses.cancelled, "cancelled"),
        (NotificationStatuses.failed, "failed")
    )

    # IN_PROCESS = 1
    # DONE = 2
    # CANCELLED = 3
    #
    # STATUSES = (
    #     (IN_PROCESS, "В процессе исполнения"),
    #     (DONE, "Выполнена"),
    #     (CANCELLED, "Отмененен"),
    # )
    status = models.CharField(max_length=250, choices=NOTIFICATION_STATUSES, default=NotificationStatuses.to_send)
    email = models.CharField(max_length=250)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)
    template_data = JSONField(default={})
    scheduled_datetime = models.DateTimeField(blank=True, null=True)
    execution_datetime = models.DateTimeField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)

    hash_sum = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        db_table = 'email_tasks'
