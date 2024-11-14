import uuid
from django.db import models
from users.models import CustomUser  # Importa el modelo de usuario directamente

class BaseProduct(models.Model):
    PRODUCT_TYPES = [
        ('door', 'Puerta'),
        ('window', 'Ventana'),
        ('furniture', 'Mueble')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    product_type = models.CharField(max_length=9, choices=PRODUCT_TYPES, verbose_name='Tipo de Producto', null=True)
    wood_type = models.CharField(max_length=100, verbose_name='Tipo de Madera', null=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio de Costo', null=True)
    is_varnished = models.BooleanField(default=False, verbose_name='Es Barnizado', null=True)
    producer = models.ForeignKey(
        'employees.Employee',
        on_delete=models.PROTECT,
        related_name='produced_%(class)s',
        verbose_name='Productor',
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización', null=True)
    client = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='door_window_products',
        verbose_name='Cliente',
        null=True
    )
    
    class Meta:
        abstract = True

class DoorWindow(BaseProduct):
    length = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Longitud', null=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ancho', null=True)
    is_exterior = models.BooleanField(default=False, verbose_name='Es Exterior', null=True)
    number_of_sheets = models.IntegerField(verbose_name='Número de Hojas', null=True)

    class Meta:
        db_table = 'doors_windows'
        verbose_name = 'Puerta/Ventana'
        verbose_name_plural = 'Puertas/Ventanas'

class Furniture(BaseProduct):
    piece_name = models.CharField(max_length=100, verbose_name='Nombre de la Pieza', null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Peso', null=True)
    is_part_of_set = models.BooleanField(default=False, verbose_name='Es Parte de un Conjunto', null=True)
    set_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nombre del Conjunto')
    client = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='furniture_products',
        verbose_name='Cliente',
        null=True
    )

    class Meta:
        db_table = 'furniture'
        verbose_name = 'Mueble'
        verbose_name_plural = 'Muebles'
