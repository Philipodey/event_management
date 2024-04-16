from django.db import models


# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=255)
    price = models.ForeignKey('Price', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.price} {self.name}"


class Price(models.Model):
    amount = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.amount}"


class EventType(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name} \n {self.description}"

