from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="tasks"),
    path("<id>",views.view_task, name="view_task")
]