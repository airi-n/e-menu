from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.AddMenuView.as_view(), name='add'),
    path('edit/<slug:pk>/', views.EditMenuView.as_view(), name='edit'),
]