from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    cover_image = models.ImageField()
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

