from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
 