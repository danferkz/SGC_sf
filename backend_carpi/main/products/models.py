from django.db import models


class Producto(models.Model):
    numero_producto = models.AutoField(primary_key=True)
    tipo_madera = models.CharField(max_length=50)
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2)
    barnizado = models.BooleanField(default=False)
    productor = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Puerta(Producto):
    largo = models.DecimalField(max_digits=5, decimal_places=2)
    ancho = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad_hojas = models.IntegerField()
    exterior = models.BooleanField(default=False)


class Ventana(Producto):
    largo = models.DecimalField(max_digits=5, decimal_places=2)
    ancho = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad_hojas = models.IntegerField()
    exterior = models.BooleanField(default=False)


class Mueble(Producto):
    peso = models.DecimalField(max_digits=7, decimal_places=2)
    nombre_pieza = models.CharField(max_length=100)
    parte_juego = models.BooleanField(default=False)


class ProductoPedido(models.Model):
    pedido = models.ForeignKey('orders.Pedido', on_delete=models.CASCADE, related_name='productos_pedido')
    puerta = models.ForeignKey(Puerta, on_delete=models.CASCADE, null=True, blank=True)
    ventana = models.ForeignKey(Ventana, on_delete=models.CASCADE, null=True, blank=True)
    mueble = models.ForeignKey(Mueble, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.PositiveIntegerField()

    def precio_unitario(self):
        if self.puerta or self.ventana or self.mueble:
            producto = self.puerta or self.ventana or self.mueble
            precio_base = producto.precio_costo
            precio_base += 50 if producto.barnizado else 0

            # Aplicar el incremento según tipo de producto
            if self.puerta:
                precio_venta = precio_base * 1.07
                if self.puerta.exterior:
                    precio_venta *= 1.02
            elif self.ventana:
                precio_venta = precio_base * 1.05
                if self.ventana.exterior:
                    precio_venta *= 1.02
            elif self.mueble:
                precio_venta = precio_base * 1.10
                peso_kg = self.mueble.peso
                descuento_peso = max(0, (peso_kg // 1000) * 0.01)
                precio_venta *= (1 - descuento_peso)

            return precio_venta
        return 0

    def __str__(self):
        if self.puerta:
            return f'Puerta: {self.puerta} (Cantidad: {self.cantidad})'
        elif self.ventana:
            return f'Ventana: {self.ventana} (Cantidad: {self.cantidad})'
        elif self.mueble:
            return f'Mueble: {self.mueble} (Cantidad: {self.cantidad})'
        return 'Producto no especificado'
