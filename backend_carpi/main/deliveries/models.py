# deliveries/models.py
from django.db import models
from products.models import DoorWindow, Furniture  # Importa los modelos
import uuid

class Delivery(models.Model):
    delivery_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    door_window = models.OneToOneField(DoorWindow, null=True, blank=True, on_delete=models.CASCADE, related_name='delivery')
    furniture = models.OneToOneField(Furniture, null=True, blank=True, on_delete=models.CASCADE, related_name='delivery')
    
    delivery_date = models.DateField(verbose_name='Fecha de Entrega')
    delivery_notes = models.TextField(blank=True, verbose_name='Notas de Entrega')
    signature_received = models.BooleanField(default=False, verbose_name='Firma Recibida')
    delivery_option = models.BooleanField(default=False, verbose_name='Opción de Entrega')
    additional_cost = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='Costo Adicional',
        default=0
    )

    class Meta:
        db_table = 'deliveries'
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'