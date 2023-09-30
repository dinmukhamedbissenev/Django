from distutils.text_file import TextFile
from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.TextField()
    cost = models.IntegerField()
