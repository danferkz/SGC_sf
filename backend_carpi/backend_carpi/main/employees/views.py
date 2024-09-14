# employees/views.py
from rest_framework import viewsets
from .models import Empleado
from .serializers import EmpleadoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
