from django.db import models
from datetime import date

class Pedido(models.Model):
    numero_pedido = models.AutoField(primary_key=True)
    fecha_pactada = models.DateField()
    empleado = models.ForeignKey('employees.Empleado', on_delete=models.SET_NULL, null=True, related_name='pedidos', verbose_name='Empleado')
    cliente = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, limit_choices_to={'is_cliente': True}, related_name='pedidos', verbose_name='Cliente')
    entrega_domicilio = models.BooleanField(default=False, verbose_name='Entrega a domicilio')

    # ManyToMany relationships for different product types (Puerta, Ventana, Mueble)
    puertas = models.ManyToManyField('products.Puerta', through='ProductoPedido', related_name='pedidos_puertas')
    ventanas = models.ManyToManyField('products.Ventana', through='ProductoPedido', related_name='pedidos_ventanas')
    muebles = models.ManyToManyField('products.Mueble', through='ProductoPedido', related_name='pedidos_muebles')

    def get_productos(self):
        return ProductoPedido.objects.filter(pedido=self)

    def precio_total(self, terminado_antes=False):
        productos = self.get_productos()
        precio_productos = sum([producto.get_precio_total() for producto in productos])

        recargo_entrega = 25 if self.entrega_domicilio else 0
        descuento_retraso = 0
        recargo_terminacion = 0

        if terminado_antes:
            recargo_terminacion = 15 * len(productos)  # $15 por producto si se termina antes
        if date.today() > self.fecha_pactada:
            dias_retraso = (date.today() - self.fecha_pactada).days
            descuento_retraso = dias_retraso * 10  # $10 por día de retraso

        return precio_productos + recargo_entrega + recargo_terminacion - descuento_retraso

    def __str__(self):
        return f'Pedido {self.numero_pedido} - {self.cliente.username}'

class ProductoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='productos_pedido')
    puerta = models.ForeignKey('products.Puerta', on_delete=models.CASCADE, null=True, blank=True)
    ventana = models.ForeignKey('products.Ventana', on_delete=models.CASCADE, null=True, blank=True)
    mueble = models.ForeignKey('products.Mueble', on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.PositiveIntegerField()

    def calcular_precio_unitario(self):
        producto = self.puerta or self.ventana or self.mueble
        return producto.precio_venta()

    def get_precio_total(self):
        return self.calcular_precio_unitario() * self.cantidad

    def save(self, *args, **kwargs):
        self.precio_total = self.get_precio_total()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.puerta:
            return f'Puerta: {self.puerta} (Cantidad: {self.cantidad})'
        elif self.ventana:
            return f'Ventana: {self.ventana} (Cantidad: {self.cantidad})'
        elif self.mueble:
            return f'Mueble: {self.mueble} (Cantidad: {self.cantidad})'
        return 'Producto no especificado'
