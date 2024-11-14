# deliveries/admin.py
from django.contrib import admin
from .models import Delivery

class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'door_window', 
        'furniture', 
        'delivery_date', 
        'signature_received', 
        'delivery_option', 
        'additional_cost'
    )
    list_filter = ('delivery_date', 'signature_received', 'delivery_option')
    search_fields = ('id', 'delivery_notes', 'door_window__wood_type', 'furniture__piece_name')
    ordering = ('delivery_date',)
    date_hierarchy = 'delivery_date'
    list_per_page = 20

# Registro del modelo en el admin
admin.site.register(Delivery, DeliveryAdmin)