from django.db import models
from apps.products.models import Product

class Transaction(models.Model):
    """
    This class represents a transaction object.
    The trasaction object is created when a client
    make any operation in any of his products.
    """
    date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    balance_after = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=255)
    