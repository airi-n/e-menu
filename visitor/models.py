from django.db import models
import restaurant

# Create your models here.
class Preference(models.Model):
    types = models.TextField()
    ingredient = models.ManyToManyField(restaurant.models.Ingredient)

    def __str__(self):
        return self.types