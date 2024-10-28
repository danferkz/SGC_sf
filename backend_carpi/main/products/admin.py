# products/admin.py

from django.contrib import admin
from .models import DoorWindow, Furniture

class DoorWindowAdmin(admin.ModelAdmin):
    list_display = ('id', 'wood_type', 'product_type', 'length', 'width', 'is_exterior', 'number_of_sheets', 'is_varnished', 'producer', 'created_at', 'updated_at')  # Cambiado a 'id'
    list_filter = ('product_type', 'is_exterior', 'is_varnished', 'producer')
    search_fields = ('wood_type', 'product_type', 'producer__name')  # Asumiendo que el modelo Producer tiene un campo 'name'

class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('id', 'wood_type', 'piece_name', 'weight', 'is_part_of_set', 'set_name', 'is_varnished', 'producer', 'created_at', 'updated_at')  # Cambiado a 'id'
    list_filter = ('is_part_of_set', 'is_varnished', 'producer')
    search_fields = ('wood_type', 'piece_name', 'producer__name')  # Asumiendo que el modelo Producer tiene un campo 'name'

admin.site.register(DoorWindow, DoorWindowAdmin)
admin.site.register(Furniture, FurnitureAdmin)