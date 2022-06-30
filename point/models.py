from django.db import models

from user.models import User


class Point(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)