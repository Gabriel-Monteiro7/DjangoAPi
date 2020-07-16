from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
class Base (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class Task(Base):
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=True)
    description = models.CharField(blank=True, default='', max_length=255)
    priority = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    user = models.ForeignKey(
        User, related_name='tasks', on_delete=models.CASCADE)

    class Meta:
        verbose_name: "Task"
        verbose_name_plural: "Tasks"
        unique_together = ['name']
        ordering = ['id']

    def __str__(self):
        return self.name
