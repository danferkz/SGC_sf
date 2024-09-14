from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    numero_empleado = models.IntegerField(unique=True)

    def __str__(self):
        return self.nombre
