from django.db import models

class Client(models.Model):
    """
    Modelo de datos para la tabla Cliente
    un cliente del CRM es un cliente que ya
    ha utilizado productos del Banco Los Alpes.
    Los clientes del CRM se pueden registrar
    cada vez que se vinculen a un nuevo producto.
    """
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    phone = models.CharField(max_length=9)
    profession = models.CharField(max_length=50)
    economy_activity = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    income_monthly = models.DecimalField(max_digits=10, decimal_places=2)
    credit_card = models.BooleanField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
