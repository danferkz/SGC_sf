# orders/serializers.py
from rest_framework import serializers
from .models import Order
from deliveries.models import Delivery
from users.models import CustomUser  
from employees.models import Employee

class OrderSerializer(serializers.ModelSerializer):
    client_detail = serializers.SerializerMethodField()
    employee_detail = serializers.SerializerMethodField()
    delivery_detail = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'orders_id',
            'client',               
            'client_detail',        
            'delivery',
            'delivery_detail',     
            'employee',
            'employee_detail',     
            'status',
            'promised_date',
            'total_price',
            'created_at',  # Añadido el campo created_at
        ]
        read_only_fields = ['orders_id', 'total_price', 'created_at']  # Este campo es solo lectura

    def get_client_detail(self, obj):
        client = obj.client
        return {
            "id": client.id,
            "username": client.username,
            "email": client.email,
        }

    def get_employee_detail(self, obj):
        employee = obj.employee
        if employee is not None:
            return {
                "employee_id": employee.employee_id,
                "specialty": employee.specialty,
            }
        return None

    def get_delivery_detail(self, obj):
        delivery = obj.delivery
        return {
            "delivery_id": delivery.delivery_id,
            "delivery_option": delivery.delivery_option,
            "delivery_date": delivery.delivery_date,
            "additional_cost": delivery.additional_cost,
        }

class OrderupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'orders_id',# Detalles del empleado
            'status',
        ]
        read_only_fields = ['orders_id', 'total_price']