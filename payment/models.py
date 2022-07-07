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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.OneToOneField(Card, null=True, blank=True, on_delete=models.CASCADE)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, blank=True)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.ForeignKey(MethodPayment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)