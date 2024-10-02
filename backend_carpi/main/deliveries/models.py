from django.db import models
from orders.models import Pedido

class Entrega(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    fecha_efectiva = models.DateField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Entrega {self.pedido.numero_pedido}'
