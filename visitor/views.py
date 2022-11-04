from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from restaurant.models import Ingredient

# Create your views here.
def home(request):
    # return HttpResponse('visitor')
#     return render(request, 'visitor/home.html')

# def get_list(request):
    ingredient_list = Ingredient.objects.all()
    ingredients_category = Ingredient.objects.values('category').distinct()
    context = {
        'ingredient_list': ingredient_list,
        'ingredients_category': ingredients_category,
    }
    return render(request, 'visitor/home.html', context)