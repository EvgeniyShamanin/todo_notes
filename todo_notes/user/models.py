from django.db import models
from uuid import uuid4


# Create your models here.


class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(blank=True, null=True, default=False)
    is_staff = models.BooleanField(blank=True, null=True, default=True)

    def __str__(self):
        return f"{self.username} {self.email}"

    class Meta:
        ordering = ['lastname']
