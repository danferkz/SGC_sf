# productos/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import (
    DoorWindowPriceCalculationSerializer, 
    FurniturePriceCalculationSerializer,
    ProductDoorCreateSerializer,
    ProductWindowCreateSerializer,
    ProductFurnitureCreateSerializer
)
from .pricing import (
    calcular_precio_puerta,
    calcular_precio_ventana,
    calcular_precio_mueble
)

# Vistas de cálculo de precio (estas ya existen)
class CalcularPrecioPuertaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DoorWindowPriceCalculationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            cost_price = calcular_precio_puerta(data)
            return Response({'cost_price': cost_price})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CalcularPrecioVentanaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DoorWindowPriceCalculationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            cost_price = calcular_precio_ventana(data)
            return Response({'cost_price': cost_price})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CalcularPrecioMuebleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FurniturePriceCalculationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            cost_price = calcular_precio_mueble(data)
            return Response({'cost_price': cost_price})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vistas de creación de productos
class ProductDoorCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductDoorCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductWindowCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductWindowCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductFurnitureCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductFurnitureCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)