# orders/urls.py
from django.urls import path
from .views import OrderCreateAPIView ,OrderListAPIViewAdmin, OrderListAPIViewCliente # Importa la vista de creación

urlpatterns = [
    path('orders-create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('orders-list-admin/', OrderListAPIViewAdmin.as_view(), name='order-list'),
    path('orders-list-client/', OrderListAPIViewCliente.as_view(), name='order-list-client'),
]
