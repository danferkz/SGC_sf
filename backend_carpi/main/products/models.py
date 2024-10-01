from django.db import models

class Producto(models.Model):
    numero_producto = models.AutoField(primary_key=True)
    tipo_madera = models.CharField(max_length=50)
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2)
    barnizado = models.BooleanField(default=False)
    productor = models.CharField(max_length=100)

    def precio_venta(self):
        precio_base = self.precio_costo
        if self.barnizado:
            precio_base += 50
        return precio_base

    def __str__(self):
        return f'{self.productor} ({self.tipo_madera})'


class Puerta(Producto):
    largo = models.DecimalField(max_digits=5, decimal_places=2)
    ancho = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad_hojas = models.IntegerField()
    exterior = models.BooleanField(default=False)

    def precio_venta(self):
        precio_base = super().precio_venta()
        precio_venta = precio_base * 1.07
        if self.exterior:
            precio_venta *= 1.02
        return precio_venta


class Ventana(Producto):
    largo = models.DecimalField(max_digits=5, decimal_places=2)
    ancho = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad_hojas = models.IntegerField()
    exterior = models.BooleanField(default=False)

    def precio_venta(self):
        precio_base = super().precio_venta()
        precio_venta = precio_base * 1.05
        if self.exterior:
            precio_venta *= 1.02
        return precio_venta


class Mueble(Producto):
    peso = models.DecimalField(max_digits=7, decimal_places=2)
    nombre_pieza = models.CharField(max_length=100)
    parte_juego = models.BooleanField(default=False)

    def precio_venta(self):
        precio_base = super().precio_venta()
        precio_venta = precio_base * 1.10
        peso_kg = self.peso
        descuento_peso = max(0, (peso_kg // 1000) * 0.01)
        precio_venta *= (1 - descuento_peso)
        return precio_venta
