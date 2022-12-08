from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home.preferenceList, name='home'),
    path('register/', views.Home.createPreferenceForm, name='register'),
    path('search/<int:pk>',  views.searchResultShow, name='search'),
    path('delete/',  views.Home.deletePreference, name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)