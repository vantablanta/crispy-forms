from django.db import models

# Create your models here.
class RandomModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()