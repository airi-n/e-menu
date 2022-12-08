from django import forms
from django.db import models
from accounts.models import User
from restaurant.models import Ingredient


class PreferenceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'from-control'
    class Meta:
        model = User
        fields = ('id','preference',)

        # widgets = {
        #     'preference': forms.CheckboxSelectMultiple(),
        # }
TagInlineFormSet = forms.inlineformset_factory(
    User, User.preference.through, fields='__all__', can_delete=False
)