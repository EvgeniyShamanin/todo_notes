from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=60)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
