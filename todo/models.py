from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):

    class Priority(models.IntegerChoices):
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    class Status(models.IntegerChoices):
        ACTIVE = 1
        DONE = 2

    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.MEDIUM)
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['important', '-priority', '-created', 'status']
