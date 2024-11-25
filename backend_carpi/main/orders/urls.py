# orders/urls.py
from django.urls import path
from .views import OrderCreateAPIView ,OrderListAPIViewAdmin, OrderListAPIViewCliente, UpdateOrderAPIAdmin #OrderListByClientIDAPIView  Importa la vista de creación

urlpatterns = [
    path('orders-create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('orders-list-admin/', OrderListAPIViewAdmin.as_view(), name='order-list'),
    path('orders-list-client/', OrderListAPIViewCliente.as_view(), name='order-list-client'),
    path('orders-update/<uuid:pk>/update-status/', UpdateOrderAPIAdmin.as_view(), name='order-update'),
    #path('clients/<uuid:client_id>/orders/', OrderListByClientIDAPIView.as_view(), name='client-orders'),
]
