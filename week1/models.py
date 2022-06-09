from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, default='name')

    def __str__(self):
        return f'{self.name}'


class GameProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    desc = models.CharField(max_length=1000, default='')

    def __str__(self):
        return f'{self.user}의 자기 소개'


class Car(models.Model):
    user = models.ManyToManyField(User)
    car_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.car_name}'

