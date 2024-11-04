# deliveries/admin.py
from django.contrib import admin
from .models import Delivery

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order', 'delivery_date', 'delivered_by', 'signature_received')
    list_filter = ('delivery_date', 'delivered_by')
    search_fields = ('order__number', 'delivered_by__user__username')

admin.site.register(Delivery, DeliveryAdmin)