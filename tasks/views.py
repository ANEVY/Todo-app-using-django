from django.shortcuts import render


def index(request):
    return render(request, "tasks/index.html")


def view_task(request):
    return render(request, "tasks/view.html")


def home_page(request):
    return render(request, "home.html")

# Create your views here.
