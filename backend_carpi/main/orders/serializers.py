# orders/serializers.py
from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import DoorWindowSerializer, FurnitureSerializer
from users.serializers import CustomUserSerializer  # Asegúrate de tener este serializador en `users`

class OrderItemSerializer(serializers.ModelSerializer):
    product = DoorWindowSerializer(required=False)
    product_furniture = FurnitureSerializer(required=False)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'product_furniture', 'quantity', 'price', 'total_price']

class OrderSerializer(serializers.ModelSerializer):
    client = CustomUserSerializer(read_only=True)
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'client', 'employee', 'status', 'promised_date', 'home_delivery', 'order_items']

    def create(self, validated_data):
        # Extrae los datos de los ítems de pedido y crea la orden.
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for item_data in order_items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order