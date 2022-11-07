from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from restaurant.models import Ingredient
from accounts.models import User
from django.urls import reverse_lazy
from django import forms
from.form import PreferenceForm
from django.views import View
from .form import TagInlineFormSet
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

    def showMenu(request):
        print("worked")
        user_id = request.user.id
        ingredient_id_taple = User.objects.filter(id=user_id).values_list('preference')
        ingredient_id = list(chain.from_iterable(ingredient_id_taple))
        print(ingredient_id)
        preference_registered = Ingredient.objects.filter(id__in =  ingredient_id ).values_list('Jp_name')
        ingredient_list = Ingredient.objects.all()
        ingredients_category = Ingredient.objects.values('category').distinct()
        print(user_id, preference_registered)
        context = {
            'user_id': user_id,
            'preference': list(chain.from_iterable((preference_registered))),
            'ingredient_list': ingredient_list,
            'ingredients_category': ingredients_category,
        }
        return render(request, 'visitor/home.html', context)

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})

    def createPreferenceForm(request,  *args, **kwargs):
        print("worked")
        if request.method =="POST":
            form = PreferenceForm(request.POST)
            print(request.POST.getlist('ingredient_id'))

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
        # form = PreferenceForm(request.POST or None)
        #
        # context = {
        #     'form': form,
        # }
        # if request.method == 'POST' and form.is_valid():
        #     post = form.save(commit=False)
        #     formset = TagInlineFormSet(request.POST, instance=post)
        #     if formset.is_valid():
        #         post.save()
        #         formset.save()
        #         return redirect('visitor:home')
        #     else:
        #         context['formset'] = formset
        #
        # else:
        #     context['formset'] = TagInlineFormSet()

        # context ={
        #     'preference': preference,
        #     'form': form_class,
        # }
        # print(preference)
        # print(user_id)
        # if request.method == 'POST':
        #     update_preference = User.objects.filter(id=user_id)
        #     update_preference.preference = request.POST['preference']
        #     update_preference.save()
        #     print("saved!")
        return render(request, 'visitor/home.html', context)


# class PreferenceRegisterView(forms.Form):
#     class Meta:
#         model = User
#         fields = ['preference',]
#         widgets = {
#             'preference': forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all(), widget=forms.CheckboxSelectMultiple()),
#         }
#         print("pass")

# class PreferenceRegisterView(CreateView):
#     model = User
#     fields = ('preference',)
#     template_name = "preference_register.html"
#     success_url = reverse_lazy("visitor:home")