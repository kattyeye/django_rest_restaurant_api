from django.db import models
# Create your models here.


class Order(models.Model):
    order = models.JSONField(null=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)


    def __str__(self):
        return self.order
