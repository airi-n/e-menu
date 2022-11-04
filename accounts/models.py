from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  is_restaurant = models.BooleanField(default=False)
  preference = models.ManyToManyField('restaurant.Ingredient', blank=True)

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.TextField()
    address = models.TextField()
    prefecture = models.CharField(max_length=6)



