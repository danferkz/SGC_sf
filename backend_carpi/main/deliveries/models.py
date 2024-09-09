from django.db import models
from orders.models import Pedido

class Entrega(models.Model):
    ESTADOS_ENTREGA = [
        ('pendiente', 'Pendiente'),
        ('realizada', 'Realizada'),
    ]
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='entrega')
    fecha_efectiva = models.DateField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS_ENTREGA, default='pendiente')

    def __str__(self):
        return f'Entrega {self.pedido.numero_pedido}'