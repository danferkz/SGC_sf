# deliveries/views.py
from rest_framework import viewsets
from .models import Entrega
from .serializers import EntregaSerializer

class EntregaViewSet(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer
