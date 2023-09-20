from django.db import models
# CRUD - Create, Read, Update, Delete
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length= 20)
    age = models.IntegerField()
