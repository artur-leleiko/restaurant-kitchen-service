from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import DishType, Dish


class ModelsTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="DishType test")

        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="test_cook",
            password="test12345",
            first_name="First name test",
            last_name="Last name test",
            years_of_experience=5
        )

        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_create_cook(self):
        username = "test_cook"
        password = "test12345"
        first_name = "First name test"
        last_name = "Last name test"
        years_of_experience = 5

        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            years_of_experience=years_of_experience
        )

        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="DishType test")
        dish = Dish.objects.create(
            name="Dish test",
            description="Description test",
            price=15.5,
            dish_type=dish_type
        )

        self.assertEqual(str(dish), f"{dish.name} ({dish.price})")
