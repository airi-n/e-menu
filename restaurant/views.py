from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Menu
from .forms import MenuForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy



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
    template_name = 'restaurant/add.html'
    form_class = MenuForm
    # restaurant = request.user
    # model = Menu
    success_url = reverse_lazy('restaurant:home')

