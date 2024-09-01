from django.urls import path
from .views import ListCreateTasks, UpdateDeleteRetrieveTasks

urlpatterns = [
    path("tasks/", ListCreateTasks.as_view(), name="list-create-tasks"),
    path(
        "tasks/<int:pk>",
        UpdateDeleteRetrieveTasks.as_view(),
        name="update-delete-retrieve-tasks",
    ),
]
