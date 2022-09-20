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

