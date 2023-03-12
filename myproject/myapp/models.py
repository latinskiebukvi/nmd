from django.utils import timezone
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    start_date = models.DateField(default=timezone.now())
    end_date = models.DateField(null=True, blank=True)


class Storage(models.Model):
    addres = models.CharField(max_length=30)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Developer(models.Model):
    dev_name = models.CharField(max_length=30)


class Model(models.Model):
    model_name = models.CharField(max_length=30)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)


class Country(models.Model):
    country_name = models.CharField(max_length=30)


class Device(models.Model):
    start_date = models.DateField(default=timezone.now())
    end_date = models.DateField(null=True, blank=True)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
