# orders/models.py
import uuid
from django.db import models
from deliveries.models import Delivery
from users.models import CustomUser  
from employees.models import Employee

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('in_progress', 'En Progreso'),
        ('completed', 'Completado'),
        ('delivered', 'Entregado'),
        ('cancelled ', 'Cancelado')
    ]

    orders_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    client = models.ForeignKey(CustomUser ,on_delete=models.PROTECT,limit_choices_to={'is_client': True},verbose_name='Cliente')
    delivery = models.OneToOneField(Delivery,on_delete=models.CASCADE,related_name='order',verbose_name='Entrega')
    employee = models.ForeignKey(Employee,on_delete=models.PROTECT,verbose_name='Empleado')
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending',verbose_name='Estado')
    promised_date = models.DateField(verbose_name='Fecha Prometida')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Total', editable=False)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
