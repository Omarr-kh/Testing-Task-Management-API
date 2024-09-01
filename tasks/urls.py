from django.urls import path
from .views import ViewCreateTasks

urlpatterns = [
    path("tasks/", ViewCreateTasks.as_view(), name="view-create-tasks"),
]
