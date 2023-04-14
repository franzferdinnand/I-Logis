from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.utils.samples import sample_cargo, sample_transport


class TestAPI(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(email="test_api@admin.com")
        self.user.set_password("12345678")
        self.user.save()
        self.client = APIClient()
        self.cargo = sample_cargo(
            self.user,
        )
        self.transport = sample_transport(
            self.user,
        )

    def test_get_cargo_list(self):
        response = self.client.get(reverse("api:cargos"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_cargo(self):
        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse("api:create_cargo"),
            {
                "cargo_type": "bullets",
                "weight_kg": 3000,
                "destination_from": "Warsaw",
                "destination_to": "Kyiv",
                "owner": 1,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_cargo_details(self):
        response = self.client.get(reverse("api:cargo-detail", args=[self.cargo.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_cargo(self):
        response = self.client.patch(reverse("api:update_cargo", args=[self.cargo.id]), {"cargo_type": "new test name"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["cargo_type"], "new test name")

    def test_delete_cargo(self):
        response = self.client.delete(reverse("api:delete_cargo", args=[self.cargo.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
