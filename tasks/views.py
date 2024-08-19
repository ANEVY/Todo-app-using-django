from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import CreateUserForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "tasks/index.html", {"tasks": tasks})


def view_task(request):
    return render(request, "tasks/view.html")


def home_page(request):
    return render(request, "home.html")


def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + username)
            return redirect("login")
    return render(request, "registration/register.html", {"form": form})


def login_page(request):

    return render(request, "registration/login.html")

# Create your views here.
