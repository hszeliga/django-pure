from django.db import models

class Form(models.Model):
    login = models.CharField(max_length=16)
    password = models.CharField(max_length=16)

class Car(models.Model):
    brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    manufacturing_date = models.DateField()
    power_output = models.IntegerField()