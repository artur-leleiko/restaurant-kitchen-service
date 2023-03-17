from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant.models import DishType, Cook, Dish


class SearchTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test12345"
        )

        self.client.force_login(self.user)

    def test_search_dish_type_by_name(self):
        response = self.client.get(
            reverse("restaurant:dish-type-list") + "?name=Test"
        )

        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(DishType.objects.filter(name__icontains="Test"))
        )

    def test_search_cook_by_username(self):
        response = self.client.get(
            reverse("restaurant:cook-list") + "?name=Test"
        )

        self.assertEqual(
            list(response.context["cook_list"]),
            list(Cook.objects.filter(username__icontains="Test"))
        )

    def test_search_dish_by_name(self):
        response = self.client.get(
            reverse("restaurant:dish-list") + "?name=Test"
        )

        self.assertEqual(
            list(response.context["dish_list"]),
            list(Dish.objects.filter(name__icontains="Test"))
        )
