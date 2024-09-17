# products/serializers.py
from rest_framework import serializers
from .models import Puerta, Ventana, Mueble, ProductoPedido

class PuertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puerta
        fields = '__all__'

class VentanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventana
        fields = '__all__'

class MuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mueble
        fields = '__all__'

class ProductoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoPedido
        fields = '__all__'
