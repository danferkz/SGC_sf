# deliveries/urls.py
from django.urls import path
from .views import DeliveryCreateView  # Cambiado de CreateDeliveryView a DeliveryCreateView

urlpatterns = [
    path('create/', DeliveryCreateView.as_view(), name='create_delivery'),
]