from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from accounts.models import Restaurant
from .models import Menu, Ingredient
from .forms import MenuForm, IngredientsForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy, reverse
from itertools import chain




# Create your views here.
def home(request):
    # return HttpResponse('restaurant')
    restaurant = request.user
    print(restaurant )
    menus = Menu.objects.filter(Restaurant_id=restaurant.id)
    restaurant_name = Restaurant.objects.get(user_id=restaurant.id)
    ingredient_list = Ingredient.objects.all()
    ingredients_category = Ingredient.objects.values('category').distinct()
    # print(menus)
    context = {
        'restaurant': restaurant_name.name,
        'menus': menus,
        'ingredient_list': ingredient_list,
        'ingredients_category': ingredients_category,
    }
    return render(request, 'restaurant/home.html', context)
#
class  AddMenuView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'restaurant/add.html'

    def get_context_data(self, **kwargs):
        context =super(AddMenuView, self).get_context_data(**kwargs)
        context['display_type'] = "none"
        return context

    def get_success_url(self):
        id = Menu.objects.last().id
        return reverse('restaurant:edit', kwargs={'pk':id,})


class EditMenuView(UpdateView):

    model = Menu
    form_class = MenuForm
    template_name = 'restaurant/edit.html'
    def get_context_data(self, **kwargs):
        context =super(EditMenuView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['display_type'] = "block"
        context['ingredients_id'] = list(chain.from_iterable(Menu.objects.filter(id=self.kwargs['pk']).values_list('ingredient')))
        # print(list(chain.from_iterable(context['ingredients_id'])))
        context['ingredient_list'] = Ingredient.objects.all()
        context['ingredients_category'] = Ingredient.objects.values('category').distinct()
        return context


    def createIngredientsForm(request,  *args, **kwargs):
        pk = kwargs['pk']

        if request.method == "POST":
            ingredient_form = IngredientsForm()
            # print(request.POST.getlist('ingredient_id'))
            if 'ingredient_id' in request.POST:
                ingredient_form = IngredientsForm(request.POST)
                # if ingredient_form.is_valid():
                #     print("3")
                    # form = MenuForm(request.POST)
                    # form.save()
                for p in request.POST.getlist('ingredient_id'):
                    menu = Menu.objects.get(id=pk)
                    menu.ingredient.add(p)

                    menu.save()

                    # return reverse('restaurant:edit', kwargs={'pk':pk})




        # context = {
        #     # 'ingredient_form': ingredient_form,
        #     'pk': int(pk),
        # }
        return redirect('restaurant:edit', pk=int(pk))

    def deleteIngredient(request,  *args, **kwargs):
        print("delete1")
        if request.method =="POST":
            if 'delete_ingredient' in request.POST:
                print("delete2")
                menu_id=kwargs['pk']
                menu=Menu.objects.get(id=menu_id)
                ingredient_id = request.POST['delete']
                print(ingredient_id)
                menu.ingredient.remove(ingredient_id)
                menu.save()

        return redirect('restaurant:edit', pk=int(menu_id))

    def get_success_url(self):
        # id = self.kwargs['pk']
        print("here")
        return reverse('restaurant:home')

class DeleteMenuView(DeleteView):
    model = Menu
    template_name = 'restaurant/confirm_delete.html'
    success_url = reverse_lazy('restaurant:home')





#
# def category(request):
#     restaurant = request.user
#     menus = Menu.objects.filter(Restaurant_id=restaurant.id)
#     ingredients = Ingredient.objects.all()
#     ingredients_category = Ingredient.objects.values('preference').distinct()
#     context = {
#         'restaurant': restaurant.first_name,
#         'menus': menus,
#         'ingredients':ingredients,
#         'ingredients_category':ingredients_category,
#     }
#     return render(request, 'restaurant/category.html', context)


