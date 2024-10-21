from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    DNI = models.CharField(max_length=11, unique=True, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    is_cliente = models.BooleanField(default=False)  # Distinguimos clientes de administradores

    def __str__(self):
        return self.username