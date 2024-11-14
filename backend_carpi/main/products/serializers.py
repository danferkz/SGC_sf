# products/serializers.py
from rest_framework import serializers
from .models import DoorWindow, Furniture
from users.models import CustomUser

class DoorPriceCalculationSerializer(serializers.ModelSerializer):
    length = serializers.DecimalField(max_digits=10, decimal_places=2)
    width = serializers.DecimalField(max_digits=10, decimal_places=2)
    is_exterior = serializers.BooleanField()
    number_of_sheets = serializers.IntegerField()
    is_varnished = serializers.BooleanField()
    wood_type = serializers.CharField()

    class Meta:
        model = DoorWindow
        fields = ['wood_type', 'is_varnished', 'length', 'width', 'is_exterior', 'number_of_sheets']

class WindowPriceCalculationSerializer(serializers.ModelSerializer):
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
        
        

class ProductDoorCreateSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    product_type = serializers.CharField(default='door')

    class Meta:
        model = DoorWindow
        fields = ['wood_type', 'product_type', 'is_varnished', 'length', 'width', 'is_exterior', 'number_of_sheets', 'cost_price', 'client']


class ProductWindowCreateSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    product_type = serializers.CharField(default='window')

    class Meta:
        model = DoorWindow
        fields = ['wood_type', 'product_type', 'is_varnished', 'length', 'width', 'is_exterior', 'number_of_sheets', 'cost_price', 'client']
        

class ProductFurnitureCreateSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    product_type = serializers.CharField(default='furniture')

    class Meta:
        model = Furniture
        fields = ['wood_type', 'product_type', 'is_varnished', 'piece_name', 'weight', 'is_part_of_set', 'set_name', 'cost_price', 'client']