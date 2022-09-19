from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  is_restaurant = models.BooleanField(default=False)

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField()
    prefecture = models.CharField(max_length=6)



