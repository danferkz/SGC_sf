# employees/serializers.py
from rest_framework import serializers
from users.models import CustomUser
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    user_data = serializers.SerializerMethodField()
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Employee
        fields = [
            'id',
            'user_id',
            'user_data',  # Mostrará información detallada del usuario
            'hire_date',
            'specialty',
            'is_active'
        ]

    def get_user_data(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username,
            'email': obj.user.email
        }

    def validate_user_id(self, value):
        try:
            user = CustomUser.objects.get(id=value)
            # Verificar que el usuario sea staff
            if not user.is_staff:
                raise serializers.ValidationError(
                    "Solo los usuarios con privilegios de staff pueden ser empleados."
                )
            # Verificar que el usuario no esté ya asignado a otro empleado
            if Employee.objects.filter(user=user).exists():
                raise serializers.ValidationError(
                    "Este usuario ya está registrado como empleado."
                )
            return value
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Usuario no encontrado.")