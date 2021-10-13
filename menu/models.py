from typing import Callable
from django.db import models

# Create your models here.


class MenuItem(models.Model):
    PIZZAS = "Pizzas"
    SALADS = "Salads"
    DESSERTS = "Desserts"
    BEVERAGES = "Beverages"

    CATEGORY_CHOICES = [
        (PIZZAS, 'Pizzas'),
        (SALADS, 'Salads'),
        (DESSERTS, 'Desserts'),
        (BEVERAGES, 'Beverages'),
    ]

    category = models.CharField(
        null=True,
        choices=CATEGORY_CHOICES,
        default=PIZZAS,
        max_length=25,
    )
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.title
