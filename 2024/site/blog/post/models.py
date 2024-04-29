from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='image/%Y')