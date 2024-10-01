from django.contrib.auth.models import AbstractUser
from django.db import models

# modelo de custom user
class CustomUser(AbstractUser):
    DNI = models.CharField(max_length=11, unique=True, null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')], null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    is_cliente = models.BooleanField(default=False)  # Distinguimos clientes de administradores

    def __str__(self):
        return self.username
