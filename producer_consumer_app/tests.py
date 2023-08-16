from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Order
from django.contrib.auth import get_user_model

User = get_user_model()


class OrderViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")
        self.order = Order.objects.create(
            task_id=1,
            name="Test Order",
            description="Test Description",
            employee=self.user,
        )

    def test_order_list_view(self):
        response = self.client.get(reverse("order_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Order")

    def test_delete_order_view(self):
        response = self.client.post(
            reverse("delete_order", args=[self.order.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("order_list"))
