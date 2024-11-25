# deliveries/urls.py
from django.urls import path
from .views import DeliveryCreateView, DeliveryDetailView  # Cambiado de CreateDeliveryView a DeliveryCreateView

urlpatterns = [
    path('create/', DeliveryCreateView.as_view(), name='create_delivery'),
    path('deliveries-detail/<uuid:delivery_id>/', DeliveryDetailView.as_view(), name='delivery-detail'),
]