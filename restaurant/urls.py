from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.AddMenuView.as_view(), name='add'),
]