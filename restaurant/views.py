from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurant.models import DishType, Cook, Dish


def index(request):
    num_dish_types = DishType.objects.count()
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()

    context = {
        "num_dish_types": num_dish_types,
        "num_cooks": num_cooks,
        "num_dishes": num_dishes
    }

    return render(request, "restaurant/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "restaurant/dish_type_list.html"
    paginate_by = 10


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    context_object_name = "dish_type_detail"
    template_name = "restaurant/dish_type_detail.html"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    template_name = "restaurant/dish_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    template_name = "restaurant/dish_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "restaurant/dish_type_delete.html"
    success_url = reverse_lazy("restaurant:dish-type-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 10


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    queryset = Dish.objects.all().select_related("dish_type")
    paginate_by = 10


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
