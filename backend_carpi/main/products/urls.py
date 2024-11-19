# products/urls.py
from django.urls import path
from .views import (
    CalcularPrecioPuertaView,
    CalcularPrecioVentanaView,
    CalcularPrecioMuebleView,
    ProductDoorCreateView,
    ProductWindowCreateView,
    ProductFurnitureCreateView
)

urlpatterns = [
    # ============ VISTAS DE CALCULO PRECIO ============
    path('calcular-precio-puerta/', CalcularPrecioPuertaView.as_view(), name='calcular-precio-puerta'),
    path('calcular-precio-ventana/', CalcularPrecioVentanaView.as_view(), name='calcular-precio-ventana'),
    path('calcular-precio-mueble/', CalcularPrecioMuebleView.as_view(), name='calcular-precio-mueble'),
    
    # ============ VISTAS DE CREACION PRODUCTOS ============
    path('product-door-create/', ProductDoorCreateView.as_view(), name='product-door-create'),
    path('product-window-create/', ProductWindowCreateView.as_view(), name='product-window-create'),
    path('product-furniture-create/', ProductFurnitureCreateView.as_view(), name='product-furniture-create'),
]