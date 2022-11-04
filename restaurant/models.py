from django.db import models
# Create your models here.

class Ingredient(models.Model):
    Jp_name = models.TextField()
    category = models.TextField()

    def __str__(self):
        return self.Jp_name


class Menu(models.Model):
    Restaurant_id = models.ForeignKey('accounts.Restaurant', on_delete=models.CASCADE)
    name = models.TextField()
    method = models.CharField(max_length=5)
    price = models.IntegerField()
    num_people = models.IntegerField()
    photo = models.ImageField(upload_to='')
    cuisine_num = models.IntegerField(blank=True, null=True)
    ingredient = models.ManyToManyField(Ingredient)


    def __str__(self):
        return self.name








