# orders/serializers.py
from rest_framework import serializers
from .models import Order
from deliveries.models import Delivery
from users.models import CustomUser  
from employees.models import Employee

class OrderSerializer(serializers.ModelSerializer):
    user_detail = serializers.SerializerMethodField()
    employee_detail = serializers.SerializerMethodField()
    delivery_detail = serializers.SerializerMethodField()  # Nuevo campo para detalles de la entrega

    class Meta:
        model = Order
        fields = [
            'orders_id',
            'user',
            'user_detail',        # Detalles del usuario
            'delivery',
            'delivery_detail',    # Detalles de la entrega
            'employee',
            'employee_detail',    # Detalles del empleado
            'status',
            'promised_date',
            'total_price'
        ]
        read_only_fields = ['id', 'total_price']

    def get_user_detail(self, obj):
        """
        Obtiene los detalles del usuario (CustomUser) que realiza la orden.
        """
        user = obj.user
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }

    def get_employee_detail(self, obj):
        """
        Obtiene los detalles del empleado asignado a la orden.
        """
        employee = obj.employee
        return {
            "employee_id": employee.employee_id,
            "specialty": employee.specialty,
        }

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

    def validate_user(self, value):
        """
        Valida que el usuario sea un cliente.
        """
        if not value.is_client:
            raise serializers.ValidationError("El usuario debe ser un cliente.")
        return value
