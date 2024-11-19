# employees/models.py
from django.db import models
from users.models import CustomUser
from django.utils import timezone
import uuid

class Employee(models.Model):
    employee_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name='ID de Empleado'
    )
    user = models.OneToOneField(
        CustomUser,  # Ahora sí hacemos referencia directa a CustomUser
        on_delete=models.CASCADE,
        related_name='employee_profile',
        verbose_name='Usuario',
    )
    hire_date = models.DateField(
        verbose_name='Fecha de Contratación',
        default=timezone.now
    )
    specialty = models.CharField(
        max_length=100,
        verbose_name='Especialidad',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Está Activo'
    )

    class Meta:
        db_table = 'employees'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['-hire_date']

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.specialty}'

    def clean(self):
        if not self.user.is_staff:
            raise models.ValidationError({
                'user': 'Solo los usuarios con privilegios de staff pueden ser empleados.'
            })