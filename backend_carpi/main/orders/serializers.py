# orders/serializers.py
from rest_framework import serializers
from .models import Order, OrderItem
from users.models import CustomUser
from employees.models import Employee
from django.utils import timezone

class OrderSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(is_client=True))
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    order_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'client', 'employee', 'status', 'promised_date', 'home_delivery', 'order_items']
    
    def validate_status(self, value):
        if value not in dict(Order.STATUS_CHOICES):
            raise serializers.ValidationError("Estado inválido.")
        return value

    def validate_promised_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("La fecha prometida no puede ser en el pasado.")
        return value

class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'product_furniture', 'quantity', 'price']
    
    def validate(self, data):
        if not data.get('product') and not data.get('product_furniture'):
            raise serializers.ValidationError("Debes seleccionar un producto o un mueble.")
        if data.get('product') and data.get('product_furniture'):
            raise serializers.ValidationError("Solo puedes seleccionar un producto o un mueble, no ambos.")
        return data
