# products/serializers.py
from rest_framework import serializers
from .models import DoorWindow, Furniture
from employees.models import Employee

class BaseProductSerializer(serializers.ModelSerializer):
    producer_id = serializers.IntegerField(write_only=True)

    class Meta:
        abstract = True
        fields = ['id', 'wood_type', 'cost_price', 'is_varnished', 'producer_id', 'created_at', 'updated_at']

    def validate_producer_id(self, value):
        # Verifica si el usuario con este ID es un productor
        if not Employee.objects.filter(id=value).exists():
            raise serializers.ValidationError("El productor no existe.")
        return value

class DoorWindowSerializer(BaseProductSerializer):
    product_type = serializers.ChoiceField(choices=DoorWindow.PRODUCT_TYPES)
    length = serializers.DecimalField(max_digits=10, decimal_places=2)
    width = serializers.DecimalField(max_digits=10, decimal_places=2)
    is_exterior = serializers.BooleanField()
    number_of_sheets = serializers.IntegerField()

    class Meta(BaseProductSerializer.Meta):
        model = DoorWindow
        fields = BaseProductSerializer.Meta.fields + ['product_type', 'length', 'width', 'is_exterior', 'number_of_sheets']

class FurnitureSerializer(BaseProductSerializer):
    piece_name = serializers.CharField(max_length=100)
    weight = serializers.DecimalField(max_digits=10, decimal_places=2)
    is_part_of_set = serializers.BooleanField()
    set_name = serializers.CharField(max_length=100, required=False)

    class Meta(BaseProductSerializer.Meta):
        model = Furniture
        fields = BaseProductSerializer.Meta.fields + ['piece_name', 'weight', 'is_part_of_set', 'set_name']
