import logging
import os
import uuid

from django.conf import settings
from django.db import models
from rest_framework.exceptions import ValidationError

from api import utils

logger = logging.getLogger(__name__)


class Task(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]
    STATUS_PENDING = "pending"
    STATUS_FAILED = "failed"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=100, default=STATUS_PENDING, choices=STATUS_CHOICES)
    file = models.FileField(upload_to="docs/")
    stats = models.JSONField(default=dict, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.status} [{self.created_at}]"

    class Meta:
        ordering = ["-created_at"]

    @property
    def file_url(self):
        if not self.file:
            return None
        return self.file.url

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        if self.file and is_new:
            extension = os.path.splitext(self.file.name)[1]
            self.file.name = f'{self.id}{extension}'
            if extension not in settings.ALLOWED_FILE_TYPES:
                logger.error(f"File type not allowed: {extension}")
                raise ValidationError(f"File type not allowed: {extension}")
        super().save(*args, **kwargs)
        try:
            if is_new:
                utils.send_task_created_message(self.id, self.file_url)
        except Exception as e:
            logger.error(f"Error while sending task created message: {e}")
            self.status = Task.STATUS_FAILED
            self.save()

# class Chunk(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     text = models.TextField(default="")
#     stats = models.JSONField(default=dict)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.id} - {self.task.id} [{self.created_at}]"
#
#     class Meta:
#         ordering = ["-created_at"]
