from django.contrib import admin

# Register your models here.
from .models import Restaurant, User


admin.site.register(Restaurant)
admin.site.register(User)