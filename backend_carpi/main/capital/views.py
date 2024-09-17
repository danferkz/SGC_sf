# capital/views.py
from rest_framework import viewsets
from .models import Capital
from .serializers import CapitalSerializer

class CapitalViewSet(viewsets.ModelViewSet):
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer
