# orders/models.py
import uuid
from django.db import models
from products.models import DoorWindow, Furniture
from employees.models import Employee
from users.models import CustomUser    

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('in_progress', 'En Progreso'),
        ('completed', 'Completado'),
        ('delivered', 'Entregado'),
        ('cancelled', 'Cancelado')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    client = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        limit_choices_to={'is_client': True},
        verbose_name='Cliente'
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        verbose_name='Empleado'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Estado'
    )
    promised_date = models.DateField(verbose_name='Fecha Prometida')
    home_delivery = models.BooleanField(default=False, verbose_name='Entrega a Domicilio')

    class Meta:
        db_table = 'orders'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_items',
        verbose_name='Pedido'
    )
    product = models.ForeignKey(
        DoorWindow,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='order_items_door_window',
        verbose_name='Producto (Puerta/Ventana)'
    )
    product_furniture = models.ForeignKey(
        Furniture,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='order_items_furniture',
        verbose_name='Producto (Mueble)'
    )
    quantity = models.IntegerField(default=1, verbose_name='Cantidad')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio por Unidad')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Total', editable=False)

    class Meta:
        db_table = 'order_items'
        verbose_name = 'Ítem de Pedido'
        verbose_name_plural = 'Ítems de Pedido'
