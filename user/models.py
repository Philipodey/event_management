from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class EventUser(AbstractUser):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField()

