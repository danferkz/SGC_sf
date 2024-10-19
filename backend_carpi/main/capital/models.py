from django.db import models

class Capital(models.Model):
    monto_disponible = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Capital disponible: {self.monto_disponible}'
