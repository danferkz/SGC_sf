# deliveries/models.py
from django.db import models
from orders.models import Order

class Delivery(models.Model):
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='delivery',
        verbose_name='Pedido'
    )
    delivery_date = models.DateField(verbose_name='Fecha de Entrega')
    delivered_by = models.ForeignKey(
        'employees.Employee',
        on_delete=models.PROTECT,
        verbose_name='Entregado Por'
    )
    delivery_notes = models.TextField(blank=True, verbose_name='Notas de Entrega')
    signature_received = models.BooleanField(default=False, verbose_name='Firma Recibida')

    class Meta:
        db_table = 'deliveries'
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'