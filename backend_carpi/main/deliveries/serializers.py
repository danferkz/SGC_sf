# deliveries/serializers.py
from rest_framework import serializers
from .models import Entrega
from orders.serializers import PedidoSerializer

class EntregaSerializer(serializers.ModelSerializer):
    pedido = serializers.PrimaryKeyRelatedField(read_only=True)  # Solo muestra el ID del pedido

    class Meta:
        model = Entrega
        fields = '__all__'
