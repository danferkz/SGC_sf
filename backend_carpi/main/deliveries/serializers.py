# deliveries/serializers.py
from rest_framework import serializers
from .models import Delivery
from products.models import DoorWindow, Furniture

class DeliverySerializer(serializers.ModelSerializer):
    door_window = serializers.UUIDField(write_only=True, required=False)  # ID del DoorWindow
    furniture = serializers.UUIDField(write_only=True, required=False)  # ID del Furniture
    door_window_detail = serializers.SerializerMethodField(read_only=True)  # Detalles del DoorWindow
    furniture_detail = serializers.SerializerMethodField(read_only=True)  # Detalles del Furniture

    class Meta:
        model = Delivery
        fields = [
            'delivery_id',
            'door_window',
            'furniture',
            'delivery_date',
            'delivery_notes',
            #'signature_received',
            'delivery_option',
            'additional_cost',
            'door_window_detail',
            'furniture_detail'
        ]

    def get_door_window_detail(self, obj):
        if obj.door_window:
            return {
                'product_id': str(obj.door_window.product_id),
                'product_type': obj.door_window.product_type,
                'wood_type': obj.door_window.wood_type,
                'cost_price': str(obj.door_window.cost_price),
                'is_varnished': obj.door_window.is_varnished,
                'length': str(obj.door_window.length),
                'width': str(obj.door_window.width),
                'is_exterior': obj.door_window.is_exterior,
                'number_of_sheets': obj.door_window.number_of_sheets,
            }
        return None

    def get_furniture_detail(self, obj):
        if obj.furniture:
            return {
                'product_id': str(obj.furniture.product_id),
                'product_type': obj.furniture.product_type,
                'wood_type': obj.furniture.wood_type,
                'cost_price': str(obj.furniture.cost_price),
                'is_varnished': obj.furniture.is_varnished,
                'piece_name': obj.furniture.piece_name,
                'weight': str(obj.furniture.weight),
                'is_part_of_set': obj.furniture.is_part_of_set,
                'set_name': obj.furniture.set_name,
            }
        return None