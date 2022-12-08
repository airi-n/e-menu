from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.AddMenuView.as_view(), name='add'),
    # path('add/category', views.category, name='category'),
    # path('add/category/<str:category>/', views.ingredient, name='ingredient'),
    path('edit/<slug:pk>/ingredient', views.EditMenuView.createIngredientsForm, name='ingredient'),
    path('edit/<slug:pk>/', views.EditMenuView.as_view(), name='edit'),
    path('delete/<slug:pk>/', views.DeleteMenuView.as_view(), name='delete')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)