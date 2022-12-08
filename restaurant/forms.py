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

    name = forms.CharField(label="メニュー名")
    method = forms.CharField(label="調理方法")
    price = forms.IntegerField(label="価格")
    num_people = forms.IntegerField(label="人数")
    photo = forms.ImageField(label="料理の画像")



class IngredientsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field in self.fields.values():
        #     field.widget.attrs['class'] = 'from-control'
    class Meta:
        model = Menu
        fields = ('id','ingredient',)

        # widgets = {
        #     'preference': forms.CheckboxSelectMultiple(),
        # }
TagInlineFormSet = forms.inlineformset_factory(
    Menu, Menu.ingredient.through, fields='__all__', can_delete=False
)
# class MenuIngredientForm(forms.ModelForm):
#     class Meta:
#         model = Menu_Ingredient
#         fields = ('menu', 'ingredient')
#     def __init__(self, *args, **kwargs):
#         menu = kwargs.pop('menu_id', None)
#         super(MenuIngredientForm, self).__init__(*args, **kwargs)
#         self.fields['menu'].initial = menu
#         self.fields['menu'].widget = forms.HiddenInput()