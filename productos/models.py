from django.db import models
from clientes.models import Client

class Product(models.Model):    
    """
    Modelo de datos para la tabla Producto
    un producto del Banco Los Alpes es un producto
    financiero que el banco ofrece a sus clientes.
    Los productos pueden ser cuentas de ahorro, cuentas
    corrientes, tarjetas de credito, etc.
    """
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    account_type = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.client}'s {self.account_type} account"