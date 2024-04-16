from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class EventUser(AbstractUser):
    email = models.EmailField(unique=True)

