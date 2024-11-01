# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    dni = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name='DNI')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True, verbose_name='Sexo')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Dirección')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Teléfono')
    is_client = models.BooleanField(default=False, verbose_name='Es Cliente')

    class Meta:
        db_table = 'users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username
