# deliveries/serializers.py
from rest_framework import serializers
from .models import Delivery
from serializers import OrderSerializer
from serializers import EmployeeSerializer

class DeliverySerializer(serializers.ModelSerializer):
    order_details = OrderSerializer(source='order', read_only=True)
    delivered_by_details = EmployeeSerializer(source='delivered_by', read_only=True)
    
    class Meta:
        model = Delivery
        fields = [
            'id',
            'order',
            'order_details',
            'delivery_date',
            'delivered_by',
            'delivered_by_details',
            'delivery_notes',
            'signature_received'
        ]