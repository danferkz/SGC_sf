# orders/urls.py
from django.urls import path
from .views import OrderCreateAPIView  # Importa la vista de creación

urlpatterns = [
    path('orders-create/', OrderCreateAPIView.as_view(), name='order-create'),
]
