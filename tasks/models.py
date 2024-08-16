from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Task(models.Model):
    TASK_STATUS = [
        ("PENDING", "Pending"),
        ("COMPLETE", "Complete")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=15, choices=TASK_STATUS, default="PENDING")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task-detail",args=[str(self.id)])

# Create your models here.
