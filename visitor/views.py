from django.shortcuts import render
from django.shortcuts import redirect
from restaurant.models import Ingredient, Menu
from accounts.models import User
from.form import PreferenceForm
from django.views import View
from itertools import chain


# from .form import PreferenceForm
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)

# Create your views here.
# def home(request):
    # return HttpResponse('visitor')
#     return render(request, 'visitor/home.html')
    # form
    # form = PreferenceForm()
# def get_list(request):
#     ingredient_list = Ingredient.objects.all()
#     ingredients_category = Ingredient.objects.values('category').distinct()
#     context = {
#         'form': form,
#         'ingredient_list': ingredient_list,
#         'ingredients_category': ingredients_category,
#     }
#     return render(request, 'visitor/home.html', context)



class Home(View):
    form_class = PreferenceForm
    template_name = 'visitor/home.html'

    def preferenceList(request):
        print("worked")
        user_id = request.user.id
        ingredient_id_taple = User.objects.filter(id=user_id).values_list('preference')
        ingredient_id = list(chain.from_iterable(ingredient_id_taple))
        # print(ingredient_id)
        preference_registered = Ingredient.objects.filter(id__in =  ingredient_id ).values_list('Jp_name')
        ingredient_list = Ingredient.objects.all()
        ingredients_category = Ingredient.objects.values('category').distinct()
        # print(user_id, preference_registered)
        context = {
            'user_id': user_id,
            'preference': list(chain.from_iterable((preference_registered))),
            'ingredient_list': ingredient_list,
            'ingredients_category': ingredients_category,
        }
        return render(request, 'visitor/home.html', context)



    def createPreferenceForm(request,  *args, **kwargs):
        print("worked")
        if request.method =="POST":
            form = PreferenceForm(request.POST)
            # print(request.POST.getlist('ingredient_id'))

            if form.is_valid():
                for p in request.POST.getlist('ingredient_id'):
                  user = User.objects.get(id=request.user.id)
                  user.preference.add(p)
                  user.save()
                return redirect('visitor:home')
        else:
            form = PreferenceForm()
            print("fail")

        context = {
            'form': form
        }

        return render(request, 'visitor/home.html', context)

    def deletePreference(request):
        if request.method =="POST":
            if 'delete_preference' in request.POST:

                user = User.objects.get(id=request.user.id)
                preference = request.POST['delete']
                preference_id = Ingredient.objects.filter(Jp_name=preference).values('id')
                user.preference.remove(list(preference_id)[0]["id"])
                user.save()

        return redirect('visitor:home')



def searchResultShow(request, pk):
    menus = Menu.objects.filter(cuisine_num = pk)
    user_id = request.user.id
    ingredient_id_taple = User.objects.filter(id=user_id).values_list('preference')
    ingredient_id = list(chain.from_iterable(ingredient_id_taple))
    preference_registered = Ingredient.objects.filter(id__in=ingredient_id).values_list('Jp_name')
    # ingredient_id = list(chain.from_iterable(menus.values_list('preference')))
    # ingredients = Ingredient.objects.filter(id__in=ingredient_id)

    context = {
        'menus': menus,
        'preference': list(chain.from_iterable((preference_registered))),
        # 'ingredients': ingredients,

    }

    return  render(request, 'visitor/search_result.html', context)


