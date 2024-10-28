# products/models.py
import uuid
from django.db import models

class BaseProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    wood_type = models.CharField(max_length=100, verbose_name='Tipo de Madera')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio de Costo')
    is_varnished = models.BooleanField(default=False, verbose_name='Es Barnizado')
    producer = models.ForeignKey(
        'employees.Employee',
        on_delete=models.PROTECT,
        related_name='produced_%(class)s',
        verbose_name='Productor'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        abstract = True

class DoorWindow(BaseProduct):
    PRODUCT_TYPES = [
        ('door', 'Puerta'),
        ('window', 'Ventana')
    ]
    
    product_type = models.CharField(max_length=6, choices=PRODUCT_TYPES, verbose_name='Tipo de Producto')
    length = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Longitud')
    width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ancho')
    is_exterior = models.BooleanField(default=False, verbose_name='Es Exterior')
    number_of_sheets = models.IntegerField(verbose_name='Número de Hojas')

    class Meta:
        db_table = 'doors_windows'
        verbose_name = 'Puerta/Ventana'
        verbose_name_plural = 'Puertas/Ventanas'

class Furniture(BaseProduct):
    piece_name = models.CharField(max_length=100, verbose_name='Nombre de la Pieza')
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Peso')
    is_part_of_set = models.BooleanField(default=False, verbose_name='Es Parte de un Conjunto')
    set_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nombre del Conjunto')

    class Meta:
        db_table = 'furniture'
        verbose_name = 'Mueble'
        verbose_name_plural = 'Muebles'