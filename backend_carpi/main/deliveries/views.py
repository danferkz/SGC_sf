# deliveries/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Delivery
from .serializers import DeliverySerializer
from products.models import DoorWindow, Furniture
from django.shortcuts import get_object_or_404

class DeliveryCreateView(generics.CreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Obtener los objetos relacionados
            door_window_id = serializer.validated_data.get('door_window')
            furniture_id = serializer.validated_data.get('furniture')

            # Validar que se proporcione al menos uno de los dos
            if not door_window_id and not furniture_id:
                return Response(
                    {"error": "Debe proporcionar door_window o furniture"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Validar que no se proporcionen ambos
            if door_window_id and furniture_id:
                return Response(
                    {"error": "No puede proporcionar both door_window y furniture"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Establecer additional_cost basado en delivery_option
            delivery_option = serializer.validated_data.get('delivery_option', False)
            additional_cost = 10 if delivery_option else 0

            # Crear el objeto Delivery
            delivery = Delivery(
                delivery_date=serializer.validated_data.get('delivery_date'),
                delivery_notes=serializer.validated_data.get('delivery_notes', ''),
                signature_received=serializer.validated_data.get('signature_received', False),
                delivery_option=delivery_option,
                additional_cost=additional_cost
            )

            # Asignar el objeto relacionado correspondiente
            if door_window_id:
                door_window = get_object_or_404(DoorWindow, product_id=door_window_id)
                delivery.door_window = door_window
            elif furniture_id:
                furniture = get_object_or_404(Furniture, product_id=furniture_id)
                delivery.furniture = furniture

            delivery.save()
            
            # Serializar la respuesta
            response_serializer = self.get_serializer(delivery)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)