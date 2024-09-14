# orders/serializers.py
from rest_framework import serializers
from .models import Pedido
from products.serializers import ProductoPedidoSerializer

class PedidoSerializer(serializers.ModelSerializer):
    empleado = serializers.PrimaryKeyRelatedField(read_only=True)
    cliente = serializers.PrimaryKeyRelatedField(read_only=True)  # Usamos un campo de solo lectura si no necesitamos el serializador completo
    productos_pedido = ProductoPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = '__all__'

    def get_precio_total(self, obj):
        return obj.precio_total()
