# deliveries/urls.py
from django.urls import path
from .views import CreateDeliveryView

app_name = 'deliveries'

urlpatterns = [
    path('create/', CreateDeliveryView.as_view(), name='delivery-create'),
]