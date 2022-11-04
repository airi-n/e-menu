from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.AddMenuView.as_view(), name='add'),
    path('add/category', views.category, name='category'),
    path('add/category/<str:category>/', views.ingredient, name='ingredient'),
    # path('add/category/<str:category>/', views.add_ingredient, name='add_ingredient'),
    path('edit/<slug:pk>/', views.EditMenuView.as_view(), name='edit'),
    path('delete/<slug:pk>/', views.DeleteMenuView.as_view(), name='delete')
]