
from django.db import models

class Route(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.source} to {self.destination}'
