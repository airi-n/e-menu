from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from accounts.models import User
from .models import Menu, Ingredient
from .forms import MenuForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy, reverse



# Create your views here.
def home(request):
    # return HttpResponse('restaurant')
    restaurant = request.user
    print(restaurant )
    menus = Menu.objects.filter(Restaurant_id=restaurant.id)
    print(menus)
    context = {
        'restaurant': restaurant.first_name,
        'menus': menus,
    }
    return render(request, 'restaurant/home.html', context)
#
class  AddMenuView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'restaurant/add.html'
    success_url = reverse_lazy('restaurant:home')

class EditMenuView(UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = 'restaurant/add.html'
    success_url = reverse_lazy('restaurant:home')

class DeleteMenuView(DeleteView):
    model = Menu
    template_name = 'restaurant/confirm_delete.html'
    success_url = reverse_lazy('restaurant:home')

def ingredient(request,category):
    ingredients = Ingredient.objects.filter(category=category)

    context = {
        'ingredients':ingredients,
    }
    return render(request, 'restaurant/ingredient.html', context)



def category(request):
    restaurant = request.user
    menus = Menu.objects.filter(Restaurant_id=restaurant.id)
    ingredients = Ingredient.objects.all()
    ingredients_category = Ingredient.objects.values('preference').distinct()
    context = {
        'restaurant': restaurant.first_name,
        'menus': menus,
        'ingredients':ingredients,
        'ingredients_category':ingredients_category,
    }
    return render(request, 'restaurant/category.html', context)