from django.urls import path
from .views import ListCreateTasks, UpdateDeleteTasks

urlpatterns = [
    path("tasks/", ListCreateTasks.as_view(), name="list-create-tasks"),
    path("tasks/<int:pk>", UpdateDeleteTasks.as_view(), name="update-delete-tasks"),
]
