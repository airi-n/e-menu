from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from . import forms
from .models import User
from django.urls import reverse_lazy

class Login(LoginView):
    form_class = forms.LoginForm
    template_name = "accounts/login.html"

    def get_success_url(self):
        user = User.objects.filter(username=self.request.POST['username'])
        if user[0].is_restaurant:
            return reverse_lazy('restaurant:home')
        else:
            return reverse_lazy('visitor:home')