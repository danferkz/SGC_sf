from django.db import models
from datetime import date

class Pedido(models.Model):
    numero_pedido = models.AutoField(primary_key=True)
    fecha_pactada = models.DateField()
    empleado = models.ForeignKey('employees.Empleado', on_delete=models.SET_NULL, null=True, related_name='pedidos_como_empleado')
    cliente = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, limit_choices_to={'is_cliente': True}, related_name='pedidos_como_cliente')
    entrega_domicilio = models.BooleanField(default=False)
    estado = models.CharField(max_length=20, default='pendiente')

    def precio_total(self, terminado_antes=False):
        from products.models import ProductoPedido  # Importación dentro del método
        productos = self.productos_pedido.all()
        precio_productos = sum([producto.precio_unitario() * producto.cantidad for producto in productos])
        recargo_entrega = 25 if self.entrega_domicilio else 0
        descuento_retraso = 0
        recargo_terminacion = 0
        if terminado_antes:
            recargo_terminacion = 15 * len(productos)  # $15 por producto
        if date.today() > self.fecha_pactada:
            dias_retraso = (date.today() - self.fecha_pactada).days
            descuento_retraso = dias_retraso * 10
        return precio_productos + recargo_entrega + recargo_terminacion - descuento_retraso

    def __str__(self):
        return f'Pedido {self.numero_pedido} - {self.cliente.username}'
