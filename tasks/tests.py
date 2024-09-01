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


class TaskAPIUpdate(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="omar", password="12345")
        self.client.login(username="omar", password="12345")
        self.task = Task.objects.create(
            user=self.user, title="Title #1 test", description="Description #1 test"
        )
        self.url = reverse("update-delete-tasks", args=[self.task.id])

    def test_update_view(self) -> None:
        updated_data = {
            "title": "updated title",
            "description": "updated description",
            "status": True,
        }
        response = self.client.put(self.url, updated_data, format="json")
        updated_task = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_task["title"], "updated title")
        self.assertEqual(updated_task["description"], "updated description")
        self.assertTrue(updated_task["status"])

    def test_update_view_invalid_title_type(self) -> None:
        updated_data = {
            "title": True,
            "description": "updated description",
            "status": True,
        }
        response = self.client.put(self.url, updated_data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_update_view_invalid_description_type(self) -> None:
        updated_data = {
            "title": "updated title",
            "description": False,
            "status": True,
        }
        response = self.client.put(self.url, updated_data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_update_view_invalid_status_type(self) -> None:
        updated_data = {
            "title": "new title",
            "description": "updated description",
            "status": "new status",
        }
        response = self.client.put(self.url, updated_data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_update_view_nonexistent_object(self) -> None:
        url = reverse("update-delete-tasks", args=[15])
        response = self.client.put(url, {}, format="json")
        self.assertEqual(response.status_code, 404)
