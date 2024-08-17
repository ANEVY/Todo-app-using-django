from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "tasks/index.html", {"tasks": tasks})


def view_task(request):
    return render(request, "tasks/view.html")


def home_page(request):
    return render(request, "home.html")

# Create your views here.
