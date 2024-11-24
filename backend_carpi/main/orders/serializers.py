# orders/serializers.py
from rest_framework import serializers
from .models import Order
from deliveries.models import Delivery
from users.models import CustomUser  
from employees.models import Employee

class OrderSerializer(serializers.ModelSerializer):
    client_detail = serializers.SerializerMethodField()  # Cambiado de user_detail a client_detail
    employee_detail = serializers.SerializerMethodField()
    delivery_detail = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'orders_id',
            'client',               # Campo de cliente en lugar de user
            'client_detail',        # Detalles del cliente
            'delivery',
            'delivery_detail',      # Detalles de la entrega
            'employee',
            'employee_detail',      # Detalles del empleado
            'status',
            'promised_date',
            'total_price'
        ]
        read_only_fields = ['orders_id', 'total_price']

    def get_client_detail(self, obj):
        """
        Obtiene los detalles del cliente (CustomUser) que realiza la orden.
        """
        client = obj.client  # Aquí usamos client, no user
        return {
            "id": client.id,
            "username": client.username,
            "email": client.email,
        }

    def get_employee_detail(self, obj):
        """
        Obtiene los detalles del empleado asignado a la orden.
        """
        employee = obj.employee
        if employee is not None:
            return {
                "employee_id": employee.employee_id,
                "specialty": employee.specialty,
            }
        return None

    def get_delivery_detail(self, obj):
        """
        Obtiene los detalles de la entrega asociada a la orden.
        """
        delivery = obj.delivery
        return {
            "delivery_id": delivery.delivery_id,
            "delivery_option": delivery.delivery_option,
            "delivery_date": delivery.delivery_date,
            "additional_cost": delivery.additional_cost,
            # Incluye otros campos de Delivery según sea necesario
        }
        
class OrderSerializerclient(serializers.ModelSerializer):
    client_detail = serializers.SerializerMethodField()  # Cambiado de user_detail a client_detail
    employee_detail = serializers.SerializerMethodField()
    delivery_detail = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'orders_id',
            'client',               # Campo de cliente en lugar de user
            'client_detail',        # Detalles del cliente
            'delivery',
            'delivery_detail',      # Detalles de la entrega
            'employee',
            'employee_detail',      # Detalles del empleado
            'status',
            'promised_date',
            'total_price'
        ]
        read_only_fields = ['orders_id', 'total_price']

    def get_client_detail(self, obj):
        """
        Obtiene los detalles del cliente (CustomUser) que realiza la orden.
        """
        client = obj.client  # Aquí usamos client, no user
        return {
            "id": client.id,
            "username": client.username,
            "email": client.email,
        }

    def get_employee_detail(self, obj):
        """
        Obtiene los detalles del empleado asignado a la orden.
        """
        employee = obj.employee
        if employee is not None:
            return {
                "employee_id": employee.employee_id,
                "specialty": employee.specialty,
            }
        return None

    def get_delivery_detail(self, obj):
        """
        Obtiene los detalles de la entrega asociada a la orden.
        """
        delivery = obj.delivery
        return {
            "delivery_id": delivery.delivery_id,
            "delivery_option": delivery.delivery_option,
            "delivery_date": delivery.delivery_date,
            "additional_cost": delivery.additional_cost,
            # Incluye otros campos de Delivery según sea necesario
        }
        

class OrderupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'orders_id',# Detalles del empleado
            'status',
        ]
        read_only_fields = ['orders_id', 'total_price']