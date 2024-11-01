# orders/admin.py
from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Número de ítems en blanco que se mostrarán

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'employee', 'status', 'promised_date', 'home_delivery')
    search_fields = ('client__username', 'employee__username', 'status')
    list_filter = ('status', 'promised_date', 'home_delivery')
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'product_furniture', 'quantity', 'price', 'total_price')
    search_fields = ('order__id', 'product__name', 'product_furniture__name')
    list_filter = ('order',)