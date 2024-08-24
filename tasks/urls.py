from django.urls import path

from . import views
urlpatterns = [
    path("/", views.index, name="tasks"),
    path("/add-task", views.create_task, name="add_task"),
    path("/<id>",views.view_task, name="view_task"),

]