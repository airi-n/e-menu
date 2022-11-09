from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.preferenceList, name='home'),
    path('register/', views.Home.createPreferenceForm, name='register'),
    path('search/<int:pk>',  views.searchResultShow, name='search'),
]