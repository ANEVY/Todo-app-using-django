from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    TASK_STATUS = [
        ("PENDING", "Pending"),
        ("COMPLETE", "Complete")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(choices=TASK_STATUS, default="PENDING")

    def __str__(self):
        return self.title

# Create your models here.
