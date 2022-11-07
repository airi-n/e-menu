from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.showMenu, name='home'),
    path('register/', views.Home.createPreferenceForm, name='register'),
    # path('',  views.PreferenceRegisterView, name='register'),
]