from django import forms
from .models import Menu
import request


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'method', 'price', 'num_people', 'photo', 'Restaurant_id')
    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['Restaurant_id'].initial = 2
        self.fields['Restaurant_id'].widget = forms.HiddenInput()



# class MenuIngredientForm(forms.ModelForm):
#     class Meta:
#         model = Menu_Ingredient
#         fields = ('menu', 'ingredient')
#     def __init__(self, *args, **kwargs):
#         menu = kwargs.pop('menu_id', None)
#         super(MenuIngredientForm, self).__init__(*args, **kwargs)
#         self.fields['menu'].initial = menu
#         self.fields['menu'].widget = forms.HiddenInput()