# employees/serializers.py
from rest_framework import serializers
from .models import Employee
from users.models import CustomUser  # Asegúrate de que se importe el modelo de usuario
from django.core.exceptions import ValidationError

class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Muestra el usuario como una cadena
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Employee
        fields = [
            'id',
            'user',
            'user_id',
            'hire_date',
            'specialty',
            'is_active'
        ]

    def validate_user_id(self, value):
        try:
            user = CustomUser.objects.get(id=value)
            if not user.is_staff:
                raise serializers.ValidationError("El usuario debe ser un empleado con is_staff=True.")
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("El usuario no existe.")
        return value

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = CustomUser.objects.get(id=user_id)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee