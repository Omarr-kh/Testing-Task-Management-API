from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Task
from rest_framework.test import APITestCase


class TaskAPICreate(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="omar", password="12345")
        self.client.login(username="omar", password="12345")
        self.task = Task.objects.create(
            user=self.user, title="Title #1 test", description="Description #1 test"
        )

    def test_create_view(self) -> None:
        url = reverse("list-create-tasks")
        task_data = {
            "title": "Title #2 test",
            "description": "Description #2 test",
        }
        response = self.client.post(url, task_data, format="json")
        task = Task.objects.last()
        self.assertEqual(task.user, self.user)
        self.assertEqual(task.title, "Title #2 test")
        self.assertEqual(task.description, "Description #2 test")
        self.assertFalse(task.status)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 2)

    def test_create_view_no_fields(self):
        url = reverse("list-create-tasks")
        task_data = {}
        response = self.client.post(url, task_data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Task.objects.count(), 1)

    def test_create_view_missing_title(self):
        url = reverse("list-create-tasks")
        task_data = {"title": "Title #2 test"}
        response = self.client.post(url, task_data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Task.objects.count(), 1)

    def test_create_view_missing_description(self):
        url = reverse("list-create-tasks")
        task_data = {"description": "Description #2 test"}
        response = self.client.post(url, task_data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Task.objects.count(), 1)


class TaskAPIList(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="omar", password="12345")
        self.client.login(username="omar", password="12345")
        self.task = Task.objects.create(
            user=self.user, title="Title #1 test", description="Description #1 test"
        )

    def test_list_view(self) -> None:
        url = reverse("list-create-tasks")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_list_view_after_create(self) -> None:
        Task.objects.create(
            user=self.user, title="Title #2", description="Description #2"
        )
        url = reverse("list-create-tasks")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_list_view_after_delete(self) -> None:
        Task.objects.last().delete()
        url = reverse("list-create-tasks")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
