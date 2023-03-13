from django.shortcuts import render

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
