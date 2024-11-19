# products/admin.py
from django.contrib import admin
from .models import DoorWindow, Furniture

class DoorWindowAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_type', 'wood_type', 'cost_price', 'is_varnished', 'length', 'width', 'is_exterior', 'number_of_sheets', 'created_at', 'updated_at')
    list_filter = ('product_type', 'wood_type', 'is_varnished', 'is_exterior')
    search_fields = ('product_id', 'wood_type', 'length', 'width')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'piece_name', 'wood_type', 'cost_price', 'is_varnished', 'weight', 'is_part_of_set', 'set_name', 'created_at', 'updated_at')
    list_filter = ('is_part_of_set', 'wood_type', 'is_varnished')
    search_fields = ('product_id', 'piece_name', 'set_name', 'wood_type')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    prepopulated_fields = {'set_name': ('piece_name',)}  # Esto es útil para Furniture

# Registro de los modelos en el admin
admin.site.register(DoorWindow, DoorWindowAdmin)
admin.site.register(Furniture, FurnitureAdmin)