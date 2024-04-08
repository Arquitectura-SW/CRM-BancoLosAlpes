from django.db import models
from apps.client.models import Client

class Product(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.client}'s {self.product_type} product"