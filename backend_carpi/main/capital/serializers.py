# capital/serializers.py
from rest_framework import serializers
from .models import Capital

class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = ['id', 'amount', 'date', 'description']
        read_only_fields = ['date']  # El campo `date` se genera automáticamente

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("El monto debe ser mayor a cero.")
        return value

    def validate_description(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("La descripción no puede exceder los 500 caracteres.")
        return value
