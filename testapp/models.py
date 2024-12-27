from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=34)
    address = models.CharField(max_length=55)
    salary = models.FloatField()
    age = models.IntegerField()