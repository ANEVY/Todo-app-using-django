from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "tasks/index.html", {"tasks": tasks})


def view_task(request):
    return render(request, "tasks/view.html")


def home_page(request):
    return render(request, "home.html")


def register_page(request):
    return render(request, "register/register.html")


def login_page(request):
    return render(request, "register/login.html")

# Create your views here.
