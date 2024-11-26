# products/serializers.py
from rest_framework import serializers
from .models import DoorWindow, Furniture


class DoorWindowPriceCalculationSerializer(serializers.ModelSerializer):
    length = serializers.DecimalField(max_digits=10, decimal_places=2)
    width = serializers.DecimalField(max_digits=10, decimal_places=2)
    is_exterior = serializers.BooleanField()
    number_of_sheets = serializers.IntegerField()
    is_varnished = serializers.BooleanField()
    wood_type = serializers.CharField()

    class Meta:
        model = DoorWindow
        fields = ['wood_type', 'is_varnished', 'length', 'width', 'is_exterior', 'number_of_sheets']

class FurniturePriceCalculationSerializer(serializers.ModelSerializer):
    piece_name = serializers.CharField()
    weight = serializers.DecimalField(max_digits=10, decimal_places=2)
    is_part_of_set = serializers.BooleanField()
    set_name = serializers.CharField(required=False, allow_null=True)
    is_varnished = serializers.BooleanField()
    wood_type = serializers.CharField()

    class Meta:
        model = Furniture
        fields = ['wood_type', 'is_varnished', 'piece_name', 'weight', 'is_part_of_set', 'set_name']

from rest_framework import serializers

class ProductDoorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorWindow
        fields = ['product_id', 'wood_type', 'is_varnished', 'length', 'width', 'is_exterior', 'number_of_sheets', 'cost_price']

    def create(self, validated_data):
        validated_data['product_type'] = 'door'  # Establecer el valor por defecto
        return super().create(validated_data)

class ProductWindowCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorWindow
        fields = ['product_id', 'wood_type', 'is_varnished', 'length', 'width', 'is_exterior', 'number_of_sheets', 'cost_price']

    def create(self, validated_data):
        validated_data['product_type'] = 'window'  # Establecer el valor por defecto
        return super().create(validated_data)

class ProductFurnitureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ['product_id', 'wood_type', 'is_varnished', 'piece_name', 'weight', 'is_part_of_set', 'set_name', 'cost_price']

    def create(self, validated_data):
        validated_data['product_type'] = 'furniture'  # Establecer el valor por defecto
        return super().create(validated_data)
    

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorWindow  # Puedes hacer esto para DoorWindow y Furniture
        fields = ['product_id', 'product_type', 'wood_type', 'is_varnished', 'length', 'width', 'is_exterior', 'number_of_sheets', 'cost_price']

class FurnitureDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ['product_id', 'product_type', 'wood_type', 'is_varnished', 'piece_name', 'weight', 'is_part_of_set', 'set_name', 'cost_price']