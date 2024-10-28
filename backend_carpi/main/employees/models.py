# employees/models.py
from django.db import models
from users.models import CustomUser 
from django.utils import timezone

class Employee(models.Model):
    user = models.OneToOneField(
        CustomUser , 
        on_delete=models.CASCADE, 
        related_name='employee_profile',
        verbose_name='Usuario'
    )
    hire_date = models.DateField(verbose_name='Fecha de Contratación')
    specialty = models.CharField(max_length=100, verbose_name='Especialidad')
    is_active = models.BooleanField(default=True, verbose_name='Está Activo')

    class Meta:
        db_table = 'employees'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['hire_date']

    def __str__(self):
        return f'{self.user.username} - {self.specialty}'