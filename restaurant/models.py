from django.db import models
import accounts
# Create your models here.

class Menu(models.Model):
    Restaurant_id = models.ForeignKey(accounts.models.Restaurant, on_delete=models.CASCADE)
    name = models.TextField()
    method = models.CharField(max_length=5)
    price = models.IntegerField()
    num_people = models.IntegerField()
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    Jp_name = models.TextField()
    en_name = models.TextField()
    category = models.TextField()
    # cross-reference table
    menu = models.ManyToManyField(Menu)


    def __str__(self):
        return self.Jp_name
