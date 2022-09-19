from django.contrib import admin

# Register your models here.
from .models import Menu, Ingredient

admin.site.register(Menu)
admin.site.register(Ingredient)
