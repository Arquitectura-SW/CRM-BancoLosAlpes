from django.db import models
from productos.models import Product


class Transaccion(models.Model):
    """
    Modelo de datos para la tabla Transaccion
    una transaccion es un registro de un movimiento
    de dinero entre distintos productos del Banco Los Alpes.
    """
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    origin = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='origin')
    destination = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='destination')

    def __str__(self):
        return f"{self.fecha} {self.monto} {self.cuenta_origen} {self.cuenta_destino}"