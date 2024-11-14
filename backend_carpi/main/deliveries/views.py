# deliveries/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import DeliverySerializer
from products.models import DoorWindow, Furniture
from .models import Delivery

class CreateDeliveryView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DeliverySerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            product = validated_data.pop('product_id')
            delivery_option = validated_data.pop('delivery_option')

            # Verificar si la orden ya tiene entrega
            if Delivery.objects.filter(order=product.order).exists():
                return Response(
                    {"error": "La orden ya tiene una entrega asociada"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Calcular precio ajustado
            cost_price = product.cost_price
            if delivery_option:
                cost_price += 10

            # Crear el registro de entrega
            delivery = Delivery.objects.create(
                order=product.order,
                delivery_date=validated_data['delivery_date'],
                delivered_by=validated_data['delivered_by'],
                delivery_notes=validated_data.get('delivery_notes', ''),
                signature_received=validated_data.get('signature_received', False)
            )

            return Response(
                {
                    "message": "Delivery creado exitosamente",
                    "delivery_id": delivery.id,
                    "adjusted_price": cost_price,
                    "created_by": request.user.username
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
