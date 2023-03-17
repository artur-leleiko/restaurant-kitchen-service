from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant.models import DishType, Dish

DISH_TYPES_URL = reverse("restaurant:dish-type-list")
COOKS_URL = reverse("restaurant:cook-list")
DISHES_URL = reverse("restaurant:dish-list")


class PublicDishTypeTests(TestCase):
    def test_login_required(self):
        response = self.client.get(DISH_TYPES_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test12345"
        )

        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="Test1")
        DishType.objects.create(name="Test2")

        response = self.client.get(DISH_TYPES_URL)
        dish_types = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(response, "restaurant/dish_type_list.html")


class PublicCookTests(TestCase):
    def test_login_required(self):
        response = self.client.get(COOKS_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test12345"
        )

        self.client.force_login(self.user)

    def test_retrieve_cooks(self):
        get_user_model().objects.create_user(
            username="test_user_1",
            password="test12345",
            years_of_experience=3
        )
        get_user_model().objects.create_user(
            username="test_user_2",
            password="test67890",
            years_of_experience=5
        )

        response = self.client.get(COOKS_URL)
        cooks = get_user_model().objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks)
        )
        self.assertTemplateUsed(response, "restaurant/cook_list.html")

    def test_create_cook(self):
        form_data = {
            "username": "username_test",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "Test first name",
            "last_name": "Test last name",
            "years_of_experience": 1
        }

        self.client.post(reverse("restaurant:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.username, form_data["username"])
        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.years_of_experience, form_data["years_of_experience"])


class PublicDishTests(TestCase):
    def test_login_required(self):
        response = self.client.get(DISHES_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateDishTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test12345"
        )

        self.client.force_login(self.user)

    def test_retrieve_dishes(self):
        dish_type = DishType.objects.create(name="Test1")
        Dish.objects.create(
            name="Test1",
            description="Test description",
            price=10,
            dish_type=dish_type
        )
        Dish.objects.create(
            name="Test2",
            description="Test description",
            price=15.1,
            dish_type=dish_type
        )

        response = self.client.get(DISHES_URL)
        dishes = Dish.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
        self.assertTemplateUsed(response, "restaurant/dish_list.html")
