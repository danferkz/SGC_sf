# deliveries/serializers.py
from rest_framework import serializers
from .models import Delivery
from products.models import DoorWindow, Furniture

class DeliverySerializer(serializers.ModelSerializer):
    product_id = serializers.UUIDField(write_only=True)
    delivery_option = serializers.BooleanField(write_only=True)

    class Meta:
        model = Delivery
        fields = [
            'product_id',
            'delivery_date',
            'delivered_by',
            'delivery_notes',
            'signature_received',
            'delivery_option'
        ]

    def validate_product_id(self, value):
        # Intentar encontrar el producto en ambos modelos
        try:
            product = DoorWindow.objects.get(id=value)
        except DoorWindow.DoesNotExist:
            try:
                product = Furniture.objects.get(id=value)
            except Furniture.DoesNotExist:
                raise serializers.ValidationError("Producto no encontrado.")
        
        return product
