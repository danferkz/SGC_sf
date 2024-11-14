# orders/admin.py
from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'client', 
        'delivery', 
        'employee', 
        'status', 
        'promised_date', 
        'total_price'
    )
    list_filter = ('status', 'promised_date', 'employee')
    search_fields = ('id', 'client__username', 'delivery__id', 'employee__name')
    ordering = ('promised_date',)
    date_hierarchy = 'promised_date'
    list_per_page = 20

# Registro del modelo en el admin
admin.site.register(Order, OrderAdmin)