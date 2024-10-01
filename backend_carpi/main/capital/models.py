from django.db import models

class Capital(models.Model):
    monto_disponible = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Monto disponible')

    def __str__(self):
        return f'Capital disponible: {self.monto_disponible}'

    def tiene_suficiente_capital(self, costo_total):
        return self.monto_disponible >= costo_total

    def descontar_capital(self, costo_total):
        if self.tiene_suficiente_capital(costo_total):
            self.monto_disponible -= costo_total
            self.save()
            return True
        return False