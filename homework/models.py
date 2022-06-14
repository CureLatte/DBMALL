from django.db import models


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)


class Store(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ManyToManyField(Food, blank=True)


class StoreIndex(models.Model):
    number = models.OneToOneField(Store, on_delete=models.CASCADE)
