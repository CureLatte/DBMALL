from django.db import models
from user.models import User


class Card(models.Model):
    number = models.CharField(max_length=100)
    expire_year = models.CharField(max_length=100)
    expire_month = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


class Account(models.Model):
    number = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class PaymentStatus(models.Model):
    status = models.CharField(max_length=100)


class MethodPayment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    card = models.OneToOneField(Card, on_delete=models.SET_NULL, blank=True)
    account = models.OneToOneField(Card, on_delete=models.SET_NULL, blank=True)
    cash = models.OneToOneField(Card, on_delete=models.SET_NULL, blank=True)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.ForeignKey()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)