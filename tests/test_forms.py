from django.test import TestCase

from restaurant.forms import CookCreationForm


class FormTests(TestCase):
    def test_cook_creation_form_is_valid(self):
        form_data = {
            "username": "test_cook",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "Test first name",
            "last_name": "Test last name",
            "years_of_experience": 5
        }

        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
