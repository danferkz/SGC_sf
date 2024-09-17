# products/views.py
from rest_framework import viewsets
from .models import Puerta, Ventana, Mueble, ProductoPedido
from .serializers import PuertaSerializer, VentanaSerializer, MuebleSerializer, ProductoPedidoSerializer

class PuertaViewSet(viewsets.ModelViewSet):
    queryset = Puerta.objects.all()
    serializer_class = PuertaSerializer

class VentanaViewSet(viewsets.ModelViewSet):
    queryset = Ventana.objects.all()
    serializer_class = VentanaSerializer

class MuebleViewSet(viewsets.ModelViewSet):
    queryset = Mueble.objects.all()
    serializer_class = MuebleSerializer

class ProductoPedidoViewSet(viewsets.ModelViewSet):
    queryset = ProductoPedido.objects.all()
    serializer_class = ProductoPedidoSerializer
