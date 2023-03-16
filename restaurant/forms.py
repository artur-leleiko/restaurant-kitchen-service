from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from restaurant.models import Cook, Dish


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "username",
            "first_name",
            "last_name",
            "years_of_experience"
        )

    def clean_years_of_experience(self):
        return validate_years_of_experience(
            self.cleaned_data["years_of_experience"]
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "username",
            "first_name",
            "last_name",
            "years_of_experience"
        )

    def clean_years_of_experience(self):
        return validate_years_of_experience(
            self.cleaned_data["years_of_experience"]
        )


class DishForm(forms.ModelForm):
    cooks = forms.MultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"


def validate_years_of_experience(years_of_experience) -> int:
    if type(years_of_experience) != int:
        raise ValidationError("Years of experience must be integer")

    return years_of_experience
